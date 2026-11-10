---
name: cellxgene-census
domain: compbio
description: Query a versioned CZ CELLxGENE Census release for cell/gene metadata or expression, including bounded AnnData/SOMA access, dataset feature presence, sparse statistics, and study-aware evaluation splits.
license: Unknown
metadata:
  version: "1.0.1"
  skill-author: K-Dense Inc.
---

# CZ CELLxGENE Census

Inspect installed client/TileDB-SOMA versions and choose an explicit Census release. Discover that release's schema, available organisms, dataset inventory, fields, and query interfaces; do not hardcode a current cell count or call it an exhaustive atlas of all biology.

## Query contract

1. Define cell/feature selection, row unit, metadata required downstream, intended count/normalized layer, and output/memory budget.
2. Explore metadata before expression. Select every field later used for grouping, including tissue/donor/dataset identifiers, rather than requesting only `cell_type` and then grouping by an absent tissue column.
3. Use supported `get_obs`/`get_var`/`get_anndata` or SOMA axis-query signatures for the installed version. Check actual values/ontology IDs and filter syntax before a broad query.
4. For ordinary unique-cell analyses apply the release's `is_primary_data` selection where appropriate. Document that policy and inspect study/donor relationships; it is not a substitute for all possible duplicate/provenance checks.
5. Inspect feature-presence metadata. A missing measured feature and an observed zero are different; restrict statistics to the eligible measurement population.
6. Use context managers or close both Census and axis-query resources. Estimate returned cells/features/nonzeros before materialization; use chunked SOMA access for the actual memory budget, not a fixed 100k-cell threshold.

## Sparse summaries

Sparse expression tables normally enumerate stored entries rather than every cell-feature pair. Dividing a sum by the number of stored/nonzero entries yields a nonzero-only mean, not mean expression across eligible cells. Use the intended number of eligible observations (and features, for a scalar matrix-wide summary) including implicit zeros. For per-gene summaries, accumulate by feature ID and use the correct measured-cell denominator per feature.

Track join IDs and map results back to selected observation/feature identifiers. Handle empty queries, absent features, zero denominators, and chunk boundaries explicitly. Do not interpret missing values as measured zero automatically.

## Analysis and delivery

Split ML evaluation by the intended independent donor/study/dataset unit and check duplicates before training. A random cell split can leak study effects or the same donor. Inspect the experimental loader API rather than asserting an unverified batch/split interface.

Preserve original counts before downstream normalization. Use donor-aware condition comparisons and separate atlas labels from independently validated truth. Report selected release/query, included/excluded datasets, measurement coverage, IDs, schema/client versions, output meanings, and any truncated/partial query.

Read [schema](references/census_schema.md) and [query patterns](references/common_patterns.md) selectively and check code against the [official Census documentation](https://chanzuckerberg.github.io/cellxgene-census/). Avoid broad downloads or training unless requested.
