---
name: kegg-database
domain: compbio
description: Retrieve KEGG entries, pathways, links, sequences, maps, or identifier conversions with the documented REST API, respecting provider access terms, request rate, and operation-specific limits.
license: Non-academic use of KEGG requires a commercial license
metadata:
  version: "1.0.1"
  skill-author: K-Dense Inc.
---

# KEGG REST access

Define the organism/database, identifier types, operation, requested format, scope, and intended use. The provider restricts its public REST service to academic use by academic users; check the current [access instructions](https://www.kegg.jp/kegg/rest/) for the actual use context.

## Operation and identifier contract

- Select `info`, `list`, `find`, `get`, `conv`, `link`, or `ddi` from the current reference. Gene IDs are organism-qualified; reference maps, organism pathways, KO entries, compounds, drugs, and enzymes are different namespaces.
- Retrieve database/release information when reproducibility matters. Keep source IDs and organism identity through conversions; mappings can be absent or one-to-many.
- Apply limits by operation and option. `get` has a multi-entry limit, while image/KGML/JSON and other options have their own supported cardinality. Do not generalize a 10-entry limit to every operation or silently truncate inputs.
- Respect the provider's limit of at most **3 requests per second**, including loops/retries. Share pacing across workers; a local helper's process-level pacing cannot coordinate independent processes.
- Use encoded URLs, HTTPS, bounded timeouts, and explicit handling of HTTP/error/empty responses. Save images as bytes; do not decode PNG data as UTF-8 text.

## Pathway analysis

Distinguish pathway membership/link retrieval from enrichment testing. For enrichment, specify the tested/measured background, organism, ID mapping coverage, duplicate handling, database snapshot, test, and multiple-testing correction.

Mapping an input to a pathway does not prove activity, direction, regulation, or causation. Preserve ambiguity between orthology-level reference maps and organism-specific evidence. Drug-interaction entries are database records for research interpretation, not a standalone clinical recommendation.

## Resources and verification

Use [helper functions](scripts/kegg_api.py) for supported operations and [lookup notes](references/kegg_reference.md) selectively. Verify signatures/limits against the [official API reference](https://www.kegg.jp/kegg/rest/keggapi.html).

Check request/response format, requested versus returned IDs, mapping coverage, output files, and partial failures. Record request parameters, organism, release/retrieval date, access scope, and any excluded or unmapped entries. Bound requests to the task rather than retrieving every pathway automatically.
