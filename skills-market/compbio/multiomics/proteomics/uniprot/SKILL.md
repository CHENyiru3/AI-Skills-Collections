---
name: uniprot-database
domain: compbio
description: Query UniProt entries, sequences, annotations, searches, or cross-database ID mapping through the REST API, including pagination, isoforms, evidence, and mapping-job status.
license: Unknown
metadata:
  version: "1.1.0"
  skill-author: K-Dense Inc.
---

# UniProt REST access

Identify organism/taxonomy, accession versus symbol, isoform/canonical requirement, requested annotation/sequence fields, source/target ID types, output format, and completeness needs.

## Queries and retrieval

- Use structured search fields supported by the current API, with encoded query parameters. Restrict taxonomy and inspect accession/entry identity rather than accepting the first gene-name match.
- Distinguish reviewed/unreviewed status, annotation evidence, predicted versus experimental features, sequence version, isoforms, and protein/gene identifiers. Reviewed status does not make every annotation experimentally established.
- Select fields and a bounded result size. Search endpoints paginate; follow the returned next-page links for a complete inventory and compare totals where provided. Explicitly label a first-page sample.
- Use stream/download endpoints for intentionally large outputs, with timeouts, HTTP checks, resource cleanup, and incremental writes. Binary formats must be saved as bytes, not decoded as text.

## ID mapping

Validate current source/target database codes and job limits. Deduplicate inputs without losing original order/provenance, submit the mapping job, and retain its ID. Poll with a finite deadline; recognize running, completion, terminal failure, malformed status, HTTP errors and timeouts.

Retrieve all result pages and preserve one-to-many mappings and failed/unmapped IDs. A successful job or first page is not proof that every input mapped. Do not coerce many protein/isoform records into one gene without a stated aggregation rule.

## Local helper and references

The [helper](scripts/uniprot_client.py) provides entry retrieval, paged search, bounded mapping, and streaming. Its search defaults to one page; select the all-pages option or iterator when completeness is required. Inspect supported output formats and report any explicit bounds.

Consult [fields](references/api_fields.md), [mapping databases](references/id_mapping_databases.md), [query syntax](references/query_syntax.md), or [examples](references/api_examples.md) only for the needed operation. Verify these lookup notes against [official API documentation](https://www.uniprot.org/help/api) for changing limits/fields.

## Verify and report

Record the query, taxonomy, database release/retrieval date, requested fields, page/record counts, mapping coverage, and original IDs. Validate selected sequence lengths/headers or annotations and inspect HTTP/content errors. Report partial retrieval, ambiguity, and unknown evidence; database annotations do not establish a new causal mechanism.
