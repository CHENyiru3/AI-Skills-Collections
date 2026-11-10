---
name: scanorama
domain: compbio
description: Integrate or correct single-cell datasets with Scanorama, handling its matrix/AnnData APIs, gene alignment, corrected embeddings, and biological-preservation checks.
license: BSD license
metadata:
  version: "1.0.1"
  skill-author: Eric Yiru
---

# Scanorama

Inspect the installed version, selected API, per-dataset preprocessing, gene identifiers, batch/sample IDs, and degree of shared biology. Preserve original expression and counts.

## Choose the API and representation

- Native matrix APIs take expression matrices plus corresponding gene-name lists. Scanpy wrappers take a list of compatible AnnData objects; a single combined AnnData is not interchangeable with that list.
- Distinguish low-dimensional integration (`integrate`/`integrate_scanpy`) from corrected expression (`correct`/`correct_scanpy`). Check return values and in-place mutation for the installed version before assignment or concatenation.
- Align feature IDs and inspect the output feature set. Track observation order, unique sample-prefixed IDs, and batch labels before combining results. Adding metadata after concatenation does not retroactively update the combined object.
- Use exact supported parameter names, including lowercase `approx` where supported. Do not copy invented `Approximate`, generic iteration, reference, or gene-correlation arguments.

## Analysis

Preprocess consistently with the documented recipe, selecting an appropriate feature space without destroying original counts. Inspect sparse/dense memory requirements and expected output size before correction.

For embedding integration, verify the wrapper's output key (commonly `X_scanorama`) and construct downstream neighbors explicitly from that representation. For corrected expression, retain its meaning as model-derived values; it is not raw count input for count-based DE.

Assess both batch mixing and preservation of cell types/rare or dataset-specific populations. Partial overlap does not guarantee that unmatched populations are preserved correctly. Check anchors/matches, representative markers, and sample composition rather than accepting a mixed UMAP alone.

## Verify and save

Check output gene/order mapping, observation coverage, finite values, batch labels, and downstream graph source. Evaluate condition effects with biological replication and the appropriate original measurements. Save versions, parameters, feature selection, output meanings, and diagnostics; verify reload.

Use the [authoritative Scanorama repository](https://github.com/brianhie/scanorama) for matrix versus AnnData examples and the correct publication. Do not cite the Harmony paper as the Scanorama method.
