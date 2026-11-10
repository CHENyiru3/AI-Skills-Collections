---
name: monocle3
domain: compbio
description: Implement or review Monocle 3 cell_data_set preprocessing, graph learning, partition-aware rooting/pseudotime, trajectory-associated genes, and model-based expression tests.
license: MIT license
metadata:
  version: "1.0.1"
  skill-author: Eric Yiru
---

# Monocle 3 trajectories

Inspect the installed Monocle 3 version, input counts, cell/gene metadata, sampling times, replicate/batch structure, and intended lineage question. Use its supported installation instructions; do not combine Monocle 2 and 3 APIs.

## Establish the trajectory

1. Build `new_cell_data_set` from aligned genes-by-cells expression and metadata. Preserve stable IDs, appropriate gene display names, counts, and donor/sample identity. Verify conversions from other objects explicitly.
2. Preprocess with justified dimensions and a compatible normalization/reduction path. Align technical batches only when needed, with real covariates and a design that does not remove the biological trajectory.
3. Build the supported reduction, cluster/partition structure, and principal graph through the documented `reduce_dimension`, `cluster_cells`, and `learn_graph` sequence. Inspect graph coverage, disconnected populations, batch/depth effects, and sensitivity to choices.
4. Choose root cells or existing principal-graph nodes from time points, known progenitors, or other evidence. Do not hardcode `Y_1`/`Y_2` or select the first arbitrary cluster. Preserve the mapping between root evidence and actual IDs.
5. Run `order_cells` with explicit roots for reproducible headless work. Inspect finite/infinite pseudotime by partition; disconnected components without a relevant root should not be forced into one lineage.

## Expression tests and branches

Use supported `graph_test` with the intended neighbor/principal graph for graph-associated expression, or `fit_models` with an explicit estimable formula for covariate-dependent expression. These answer different questions; a graph-autocorrelation result is not a generic causal pseudotime effect.

Report effect measures, corrected significance, model family, covariates, filtering, and biological replication. Use supported gene-module/aggregation and lineage subsetting operations with aligned metadata. Do not copy Monocle 2 `BEAM`/branched plotting calls or the unverified `find_genes_that_differ_with_pseudotime` example into a Monocle 3 pipeline.

## Interpretation and validation

Pseudotime is an ordering inferred from the measured manifold and chosen root. It does not establish actual elapsed time, lineage ancestry, fate decisions, or causation without independent evidence. Examine branch markers, sampling-time consistency, alternative roots, and donor/sample reproducibility where those claims matter.

Save the object, graph/root IDs, parameters/seeds, versions, test tables, and plots. Reopen and verify graph/root membership, observation coverage, and pseudotime values. Distinguish a programmatic analysis from a GUI root/segment selection that was not performed.

Use [official trajectories](https://cole-trapnell-lab.github.io/monocle3/docs/trajectories/) and [differential analysis](https://cole-trapnell-lab.github.io/monocle3/docs/differential/) documentation for current functions and input requirements.
