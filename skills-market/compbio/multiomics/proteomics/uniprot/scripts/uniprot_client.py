#!/usr/bin/env python3
"""UniProt REST helpers. Search defaults to one page; request all_pages explicitly.

JSON pages are merged without discarding failedIds. TSV/FASTA/plain-text pages can
be joined; paginated XML/RDF/binary output must use a dedicated download workflow.
Every request has a timeout, mapping polling has a deadline, and paging is bounded.
"""
from __future__ import annotations

import json
import sys
import time
from typing import Dict, Generator, List, Optional

import requests

BASE_URL = "https://rest.uniprot.org"
POLLING_INTERVAL = 3
REQUEST_TIMEOUT = 30
MAX_PAGES = 1000


def _decode(response, format):
    if format == "json":
        return response.json()
    if format == "xlsx":
        raise ValueError("Use an explicit binary download for XLSX; this helper returns JSON/text")
    return response.text


def _pages(endpoint, params, max_pages=MAX_PAGES):
    """Yield responses; next links already contain their cursor/query parameters."""
    seen = set()
    for _ in range(max_pages):
        if endpoint in seen:
            raise RuntimeError("Repeated next-page URL; retrieval incomplete")
        seen.add(endpoint)
        response = requests.get(endpoint, params=params, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        yield response
        endpoint = response.links.get("next", {}).get("url")
        if not endpoint:
            return
        if not endpoint.startswith(BASE_URL + "/"):
            raise RuntimeError("Unexpected pagination host")
        params = None
    raise RuntimeError(f"Page limit {max_pages} reached; retrieval incomplete")


def _collect_pages(endpoint, params, format):
    combined = None
    text_parts = []
    header = None
    for response in _pages(endpoint, params):
        page = _decode(response, format)
        if format == "json":
            if not isinstance(page, dict):
                raise ValueError("Expected a JSON object page")
            if combined is None:
                combined = dict(page)
                for key in ("results", "failedIds"):
                    if key in page:
                        combined[key] = list(page[key])
            else:
                for key in ("results", "failedIds"):
                    if key in page:
                        combined.setdefault(key, []).extend(page[key])
        elif format in ("tsv", "fasta", "txt"):
            if format == "tsv":
                lines = page.splitlines()
                if not lines:
                    continue
                if header is None:
                    header = lines[0]
                elif lines[0] != header:
                    raise ValueError("TSV page headers differ")
                else:
                    lines = lines[1:]
                text_parts.append("\n".join(lines))
            else:
                text_parts.append(page.rstrip("\n"))
        else:
            raise ValueError("All-pages merging supports JSON, TSV, FASTA and TXT only")
    return combined if format == "json" else "\n".join(text_parts) + ("\n" if text_parts else "")


def iter_search_pages(query: str, format: str = "json",
                      fields: Optional[List[str]] = None, size: int = 500):
    """Yield all search pages. Inspect/stream pages rather than materializing huge queries."""
    if not 1 <= size <= 500:
        raise ValueError("size must be between 1 and 500")
    params = {"query": query, "format": format, "size": size}
    if fields:
        params["fields"] = ",".join(fields)
    for response in _pages(f"{BASE_URL}/uniprotkb/search", params):
        yield _decode(response, format)


def search_proteins(query: str, format: str = "json", fields: Optional[List[str]] = None,
                    size: int = 25, all_pages: bool = False):
    """Return one page by default, or merge all supported-format pages explicitly."""
    if not 1 <= size <= 500:
        raise ValueError("size must be between 1 and 500")
    params = {"query": query, "format": format, "size": size}
    if fields:
        params["fields"] = ",".join(fields)
    endpoint = f"{BASE_URL}/uniprotkb/search"
    if all_pages:
        return _collect_pages(endpoint, params, format)
    response = requests.get(endpoint, params=params, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    return _decode(response, format)


def get_protein(accession: str, format: str = "json"):
    response = requests.get(f"{BASE_URL}/uniprotkb/{accession}.{format}", timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    return _decode(response, format)


def batch_retrieve(accessions: List[str], format: str = "json", fields: Optional[List[str]] = None):
    """Bound query size and retrieve all matching pages. Preserve absent-ID accounting yourself."""
    if not accessions or len(accessions) > 500:
        raise ValueError("Use nonempty batches of at most 500 accessions; combine by ID explicitly")
    query = " OR ".join(f"accession:{accession}" for accession in accessions)
    return search_proteins(query, format=format, fields=fields, size=500, all_pages=True)


def stream_results(query: str, format: str = "fasta", fields: Optional[List[str]] = None,
                   chunk_size: int = 8192) -> Generator[str, None, None]:
    params = {"query": query, "format": format}
    if fields:
        params["fields"] = ",".join(fields)
    if format == "xlsx":
        raise ValueError("Use an explicit binary download for XLSX")
    with requests.get(f"{BASE_URL}/uniprotkb/stream", params=params, stream=True,
                      timeout=REQUEST_TIMEOUT) as response:
        response.raise_for_status()
        response.encoding = response.encoding or "utf-8"
        for chunk in response.iter_content(chunk_size=chunk_size, decode_unicode=True):
            if chunk:
                yield chunk


def map_ids(ids: List[str], from_db: str, to_db: str, format: str = "json",
            max_wait: float = 300):
    """Submit once, poll with a deadline, preserve failed IDs, and retrieve all result pages."""
    if not ids or len(ids) > 100000 or max_wait <= 0:
        raise ValueError("Use 1..100000 IDs and a positive polling deadline")
    response = requests.post(f"{BASE_URL}/idmapping/run",
                             data={"from": from_db, "to": to_db, "ids": ",".join(ids)},
                             timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    job_id = response.json()["jobId"]
    deadline = time.monotonic() + max_wait
    while True:
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise TimeoutError(f"Mapping job {job_id} did not finish before the deadline")
        response = requests.get(f"{BASE_URL}/idmapping/status/{job_id}",
                                timeout=min(REQUEST_TIMEOUT, remaining))
        response.raise_for_status()
        status = response.json()
        job_status = status.get("jobStatus")
        if job_status == "FINISHED" or (job_status is None and
                                                ("results" in status or "failedIds" in status)):
            break
        if job_status not in ("NEW", "RUNNING"):
            raise RuntimeError(f"Mapping job {job_id} returned terminal/unknown status: {job_status!r}")
        time.sleep(min(POLLING_INTERVAL, max(0, deadline - time.monotonic())))
    details = requests.get(f"{BASE_URL}/idmapping/details/{job_id}", timeout=REQUEST_TIMEOUT)
    details.raise_for_status()
    endpoint = details.json()["redirectURL"]
    if not endpoint.startswith(BASE_URL + "/"):
        raise RuntimeError("Unexpected mapping results host")
    result = _collect_pages(endpoint, {"format": format, "size": 500}, format)
    if format == "json" and status.get("failedIds"):
        result["failedIds"] = list(dict.fromkeys(result.get("failedIds", []) + status["failedIds"]))
    return result


def get_available_fields() -> List[Dict]:
    response = requests.get(f"{BASE_URL}/configure/uniprotkb/result-fields", timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    return response.json()


def get_id_mapping_databases() -> Dict:
    response = requests.get(f"{BASE_URL}/configure/idmapping/fields", timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    return response.json()


def main():
    """Command-line interface for UniProt database queries."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Query UniProt database using REST API',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Search for proteins
  %(prog)s --search "insulin AND organism_name:human" --format json

  # Get a specific protein
  %(prog)s --get P01308 --format fasta

  # Map IDs from UniProt to PDB
  %(prog)s --map P01308,P04637 --from UniProtKB_AC-ID --to PDB

  # Stream large results
  %(prog)s --stream "taxonomy_id:9606 AND reviewed:true" --format fasta

  # List available fields
  %(prog)s --list-fields

  # List mapping databases
  %(prog)s --list-databases
        """
    )

    # Main operation arguments (mutually exclusive)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--search', '-s', help='Search query string')
    group.add_argument('--get', '-g', help='Get protein by accession number')
    group.add_argument('--map', '-m', help='Map IDs (comma-separated)')
    group.add_argument('--stream', help='Stream large result sets')
    group.add_argument('--list-fields', action='store_true',
                      help='List all available query fields')
    group.add_argument('--list-databases', action='store_true',
                      help='List all ID mapping databases')

    # Format options
    parser.add_argument('--format', '-f', default='json',
                       help='Output format (json, tsv, xlsx, xml, fasta, txt, rdf)')

    # Search-specific options
    parser.add_argument('--fields', help='Comma-separated list of fields to return')
    parser.add_argument('--size', type=int, default=25,
                       help='Number of results (default: 25, max: 500)')

    # Mapping-specific options
    parser.add_argument('--from', dest='from_db',
                       help='Source database for ID mapping')
    parser.add_argument('--to', dest='to_db',
                       help='Target database for ID mapping')

    parser.add_argument('--all-pages', action='store_true', help='Retrieve all search pages (bounded to 1000 pages)')
    args = parser.parse_args()

    try:
        if args.list_fields:
            fields = get_available_fields()
            print(json.dumps(fields, indent=2))

        elif args.list_databases:
            databases = get_id_mapping_databases()
            print(json.dumps(databases, indent=2))

        elif args.search:
            fields_list = args.fields.split(',') if args.fields else None
            results = search_proteins(
                args.search,
                format=args.format,
                fields=fields_list,
                size=args.size,
                all_pages=args.all_pages
            )
            if args.format == 'json':
                print(json.dumps(results, indent=2))
            else:
                print(results)

        elif args.get:
            protein = get_protein(args.get, format=args.format)
            if args.format == 'json':
                print(json.dumps(protein, indent=2))
            else:
                print(protein)

        elif args.map:
            if not args.from_db or not args.to_db:
                parser.error("--map requires --from and --to arguments")

            ids = [id.strip() for id in args.map.split(',')]
            mapping = map_ids(ids, args.from_db, args.to_db, format=args.format)
            if args.format == 'json':
                print(json.dumps(mapping, indent=2))
            else:
                print(mapping)

        elif args.stream:
            fields_list = args.fields.split(',') if args.fields else None
            for chunk in stream_results(args.stream, format=args.format, fields=fields_list):
                print(chunk, end='')

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
