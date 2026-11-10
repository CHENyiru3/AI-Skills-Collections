"""
KEGG REST API Helper Functions

This module provides Python functions for interacting with the KEGG REST API.
Functions return response text, except image retrieval returns bytes. HTTP errors
retain the legacy Error: text result; callers must check it before parsing.

API Base URL: https://rest.kegg.jp
Documentation: https://www.kegg.jp/kegg/rest/keggapi.html

IMPORTANT: KEGG API is made available only for academic use by academic users.
"""

from __future__ import annotations

import threading
import time
import urllib.request
import urllib.parse
import urllib.error
from typing import Optional, List, Union


KEGG_BASE_URL = "https://rest.kegg.jp"


_REQUEST_LOCK = threading.Lock()
_LAST_REQUEST = None


def _open(url):
    """Pace this process to <=3 starts/second. Separate processes must coordinate."""
    global _LAST_REQUEST
    with _REQUEST_LOCK:
        if _LAST_REQUEST is not None:
            delay = 0.34 - (time.monotonic() - _LAST_REQUEST)
            if delay > 0:
                time.sleep(delay)
        _LAST_REQUEST = time.monotonic()
    return urllib.request.urlopen(url, timeout=30)


def _entry_ids(entries, limit=None):
    ids = entries if isinstance(entries, list) else entries.split("+")
    if not ids or any(not entry.strip() for entry in ids):
        raise ValueError("At least one nonempty entry is required")
    if limit is not None and len(ids) > limit:
        raise ValueError(f"This request accepts at most {limit} entries; batch explicitly")
    return "+".join(ids)


def kegg_info(database: str) -> str:
    """
    Get database metadata and statistics.

    Args:
        database: KEGG database name (e.g., 'kegg', 'pathway', 'enzyme', 'genes')

    Returns:
        str: Database information and statistics

    Example:
        info = kegg_info('pathway')
    """
    url = f"{KEGG_BASE_URL}/info/{database}"
    try:
        with _open(url) as response:
            return response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        return f"Error: {e.code} - {e.reason}"


def kegg_list(database: str, org: Optional[str] = None) -> str:
    """
    List entry identifiers and associated names.

    Args:
        database: KEGG database name or specific entry (e.g., 'pathway', 'enzyme', 'hsa:10458')
        org: Optional organism code for pathway/module listings (e.g., 'hsa' for human)

    Returns:
        str: Tab-delimited list of entries

    Examples:
        pathways = kegg_list('pathway')  # List all reference pathways
        hsa_pathways = kegg_list('pathway', 'hsa')  # List human pathways
        genes = kegg_list('hsa:10458+ece:Z5100')  # List specific genes
    """
    if org:
        url = f"{KEGG_BASE_URL}/list/{database}/{org}"
    else:
        url = f"{KEGG_BASE_URL}/list/{database}"

    try:
        with _open(url) as response:
            return response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        return f"Error: {e.code} - {e.reason}"


def kegg_find(database: str, query: str, option: Optional[str] = None) -> str:
    """
    Search for entries by keywords or molecular properties.

    Args:
        database: Database to search ('genes', 'compound', 'drug', etc.)
        query: Search term or molecular property
        option: Optional parameter for molecular searches:
                'formula' - exact match to chemical formula
                'exact_mass' - range search by exact mass (e.g., '174.05-174.15')
                'mol_weight' - range search by molecular weight

    Returns:
        str: Tab-delimited search results

    Examples:
        # Keyword search
        results = kegg_find('genes', 'shiga toxin')

        # Formula search
        compounds = kegg_find('compound', 'C7H10N4O2', 'formula')

        # Mass range search
        drugs = kegg_find('drug', '300-310', 'exact_mass')
    """
    query_encoded = urllib.parse.quote(query)

    if option:
        url = f"{KEGG_BASE_URL}/find/{database}/{query_encoded}/{option}"
    else:
        url = f"{KEGG_BASE_URL}/find/{database}/{query_encoded}"

    try:
        with _open(url) as response:
            return response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        return f"Error: {e.code} - {e.reason}"


def kegg_get(entries: Union[str, List[str]], option: Optional[str] = None) -> Union[str, bytes]:
    """
    Retrieve full database entries or specific data formats.

    Args:
        entries: Single entry ID or list of entry IDs (max 10)
        option: Optional output format:
                'aaseq' or 'ntseq' - FASTA sequence
                'mol' - MOL format (for compounds)
                'kcf' - KCF format (for compounds)
                'image' - PNG image (pathway maps, single entry only)
                'kgml' - KGML format (pathway XML, single entry only)
                'json' - JSON format (pathway only, single entry only)

    Returns:
        str: Entry data in requested format

    Examples:
        # Get pathway entry
        pathway = kegg_get('hsa00010')

        # Get multiple entries
        genes = kegg_get(['hsa:10458', 'ece:Z5100'])

        # Get sequence
        sequence = kegg_get('hsa:10458', 'aaseq')

        # Get pathway as JSON
        pathway_json = kegg_get('hsa05130', 'json')
    """
    limit = 1 if option in ("image", "image2x", "kgml", "json") else 10
    entries_str = _entry_ids(entries, limit=limit)

    if option:
        url = f"{KEGG_BASE_URL}/get/{entries_str}/{option}"
    else:
        url = f"{KEGG_BASE_URL}/get/{entries_str}"

    try:
        with _open(url) as response:
            payload = response.read()
            return payload if option in ('image', 'image2x') else payload.decode('utf-8')
    except urllib.error.HTTPError as e:
        return f"Error: {e.code} - {e.reason}"


def kegg_conv(target_db: str, source_db: str) -> str:
    """
    Convert identifiers between KEGG and external databases.

    Args:
        target_db: Target database (e.g., 'ncbi-geneid', 'uniprot', 'pubchem')
        source_db: Source database or entry (e.g., 'hsa', 'compound', 'hsa:10458')

    Returns:
        str: Tab-delimited conversion table

    Examples:
        # Convert all human genes to NCBI Gene IDs
        conversions = kegg_conv('ncbi-geneid', 'hsa')

        # Convert specific gene
        gene_id = kegg_conv('ncbi-geneid', 'hsa:10458')

        # Convert compounds to PubChem IDs
        pubchem = kegg_conv('pubchem', 'compound')
    """
    url = f"{KEGG_BASE_URL}/conv/{target_db}/{source_db}"
    try:
        with _open(url) as response:
            return response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        return f"Error: {e.code} - {e.reason}"


def kegg_link(target_db: str, source_db: str) -> str:
    """
    Find related entries across KEGG databases.

    Args:
        target_db: Target database (e.g., 'pathway', 'enzyme', 'genes')
        source_db: Source database or entry (e.g., 'hsa', 'pathway', 'hsa:10458')

    Returns:
        str: Tab-delimited list of linked entries

    Examples:
        # Find pathways linked to human genes
        links = kegg_link('pathway', 'hsa')

        # Find genes in a specific pathway
        genes = kegg_link('genes', 'hsa00010')

        # Find pathways for a specific gene
        pathways = kegg_link('pathway', 'hsa:10458')
    """
    url = f"{KEGG_BASE_URL}/link/{target_db}/{source_db}"
    try:
        with _open(url) as response:
            return response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        return f"Error: {e.code} - {e.reason}"


def kegg_ddi(drug_entries: Union[str, List[str]]) -> str:
    """
    Check drug-drug interactions.

    Args:
        drug_entries: Single drug entry or list of drug entries (max 10)

    Returns:
        str: Drug interaction information

    Example:
        interactions = kegg_ddi(['D00001', 'D00002'])
    """
    # No silent truncation. The provider documents operation-specific limits.
    entries_str = _entry_ids(drug_entries)

    url = f"{KEGG_BASE_URL}/ddi/{entries_str}"
    try:
        with _open(url) as response:
            return response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        return f"Error: {e.code} - {e.reason}"


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="KEGG REST helper; import functions for normal use")
    parser.add_argument("--demo", action="store_true", help="Run three live example requests")
    args = parser.parse_args()
    if args.demo:
        print(kegg_info("pathway"))
        print(kegg_list("pathway"))
        print(kegg_find("genes", "p53"))
