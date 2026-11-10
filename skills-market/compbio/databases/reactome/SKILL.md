---
name: reactome-database
domain: compbio
description: Retrieve Reactome pathways/entities or submit and interpret Reactome pathway enrichment/expression analyses, with identifier coverage, species, background, FDR, and database-version provenance.
license: Unknown
metadata:
  version: "1.0.1"
  skill-author: K-Dense Inc.
---

# Reactome pathway analysis

Define species, identifier namespace, list/quantitative input, biological comparison, measured background, and output. Query the database version/retrieval date instead of hardcoding current pathway counts.

## Retrieve versus analyze

Use Content Service for entities, pathways, hierarchies and relationships; use Analysis Service for supported list/expression/projection analyses. Their schemas and semantics differ. Inspect current endpoint documentation and returned structure rather than assuming flat `stId`/`name` fields in every result.

For REST requests use explicit timeouts, status/content checks, encoded identifiers, and bounded retries. If using a wrapper, verify its installed signature and behavior against the service; do not infer current maintenance status from an old release note alone.

## Analysis contract

1. Check organism and actual gene/protein/metabolite identifiers. Preserve original IDs, deduplicate using a stated rule, and inspect one-to-many, ambiguous and unmapped identifiers.
2. Choose the correct operation and input schema. For quantitative values, label the transformation/units and sample columns. Species projection must be an explicit choice with its limitations.
3. Specify the measured/testable universe. Use a supported custom-background workflow where needed, or state the service's actual default and resulting limitation; do not claim all submitted genes were measured in every assay.
4. Submit only the requested identifier/expression payload. Preserve the request and returned token/job reference, service parameters and version. Treat remotely submitted unpublished data according to the requested access context.
5. Parse the actual nested response, follow supported paging, and retain mapping coverage, pathway sizes, overlap/effect measures, p-values and FDR. A returned pathway is not automatically significantly enriched.
6. Interpret related/hierarchical pathways with overlap and multiple testing in mind. Enrichment does not establish pathway activation, inhibition, a new interaction, or causal mechanism by itself.

## Verify and deliver

Use a small known response or returned schema to verify parsing, then inspect selected pathways/IDs and token/browser links. Report the analysis type, species, background, database version, thresholds, coverage, exclusions and any partial/expired result. Token lifetimes are service-dependent; do not treat a saved URL as permanent evidence.

Consult [API lookup notes](references/api_reference.md), the [local helper](scripts/reactome_query.py), and [official developer documentation](https://reactome.org/dev). Inspect helper output/schema before treating it as a complete analysis report.
