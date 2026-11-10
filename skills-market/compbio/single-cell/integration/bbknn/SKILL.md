---
name: bbknn
domain: compbio
description: Build or evaluate a batch-balanced neighbor graph with BBKNN in a Scanpy/AnnData workflow, including batch labels, per-batch neighbors, representation choice, and biological-preservation checks.
license: MIT license
metadata:
  version: "1.0.1"
  skill-author: Eric Yiru
---

# BBKNN graph integration

Inspect BBKNN/Scanpy versions, the combined AnnData, batch metadata, input representation, cell-type overlap, and sample sizes. Preserve original counts, processed expression, and any unintegrated graph needed for comparison.

## Build the graph

- BBKNN balances neighbor contributions across batches in a chosen representation, commonly PCA. It changes the neighbor graph; it does not itself replace expression with corrected counts.
- Verify batch labels exist, contain no unintended missing values, and align to observations. Check whether batches have enough cells and shared populations for the requested per-batch neighbor count.
- Use documented arguments such as `batch_key`, `use_rep`, `n_pcs`, `neighbors_within_batch`, `trim`, `metric`, and supported approximation/backend options. Do not use fabricated `k`, `kr`, `lam`, `sigma`, `ref_batch`, or an embedded `ridge_factor` argument.
- Select the representation and components deliberately. Any optional ridge-regression preprocessing is a separate supported procedure with its own data/biological assumptions.
- Construct the BBKNN graph instead of an ordinary expression neighbor graph, then run UMAP/clustering on that intended graph. Do not overwrite it later with `sc.pp.neighbors` unintentionally.

## Assess and interpret

Inspect graph degree/connectivity, contributions by batch, rare populations, and unexpected cross-type neighbors. Balanced-neighbor construction can force inappropriate links when batches have different biology or absent populations; stronger balancing is not universally better correction.

Compare batch structure and known biological markers before/after, including per-sample composition and disconnected/unmatched populations. Avoid ranking integration methods by a generic speed/accuracy table without a workload-specific comparison.

Use original appropriate expression for markers and donor-aware condition tests. Graph integration does not remove confounding, create missing controls, or justify cell-level pseudoreplication.

## Verify and save

Check graph keys/shapes, cell order, finite embeddings, selected representation, and metadata. Save graph, preprocessing/version/parameter details, counts/processed-layer meanings, and assessment results. A full H5AD write saves available object components, not only the neighbor graph.

Consult the [official BBKNN API](https://bbknn.readthedocs.io/en/latest/bbknn.bbknn.html) for exact parameter names and the [repository](https://github.com/Teichlab/bbknn) for optional preprocessing.
