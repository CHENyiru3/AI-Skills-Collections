---
name: archr
domain: compbio
description: 'Build or debug an ArchR scATAC-seq workflow: Arrow files, project QC, iterative LSI, clusters, reproducible peaks, motif analysis, or RNA reference integration.'
license: MIT license
metadata:
  version: "1.0.1"
  skill-author: Eric Yiru
---

# ArchR scATAC-seq

Identify ArchR/R versions, fragment/Arrow inputs, sample/barcode mapping, organism/genome assembly, annotation, and project output directory. Use the official installation route and matching Bioconductor genome dependencies; do not treat all dependencies as CRAN packages.

## Analysis order and data contracts

1. Validate indexed fragments and unique sample-prefixed cell IDs. Build Arrow files/project using supported APIs, preserving source locations and disk requirements.
2. Assess TSS enrichment, fragments, nucleosome/blacklist metrics and doublets per sample. Choose QC thresholds from observed distributions and assay context, not a universal PBMC cutoff.
3. Use `addIterativeLSI` on the intended matrix, inspect depth-correlated components, then select reductions for clustering/UMAP. Do not call the nonexistent `addIterativeLSA` example.
4. For peak analysis, create suitable group coverages, call a reproducible peak set with the configured supported caller, and add the peak matrix before requesting `PeakMatrix` markers. In the documented MACS2 path this involves `addGroupCoverages`, `addReproduciblePeakSet`, then `addPeakMatrix`; inspect installed signatures and caller executable.
5. Check genome/peak coordinates and annotation compatibility before motif annotations, deviations/enrichment, or regulatory links. Use bias-aware marker testing and relevant background features.
6. For RNA reference integration, supply the actual compatible RNA reference and supported group/feature mappings. A gene-score matrix is an accessibility-derived proxy, not measured RNA expression; it cannot generate a validated transcriptomic reference by itself.

## Interpretation and persistence

Track which matrix and reductions each result uses. Separate motif presence, motif accessibility, TF expression, and evidence of regulatory activity. Peak-gene correlation and transferred labels are hypotheses with uncertainty, not causal regulation or measured expression.

Use donor/sample-aware analysis for condition claims; cells and pseudobulk subdivisions are not substitutes for independent biological replicates. Inspect depth/batch and biological preservation in embeddings and markers.

Save through supported ArchR project operations, retaining required Arrow/coverage files and explicit output paths. Reopen the project and verify IDs, matrix/reduction availability, peak set, selected genomic tracks, and exported file formats. Do not assume an invented generic ArchR-to-Seurat/export helper exists.

Consult the [ArchR book](https://www.archrproject.com/bookdown/) and [peak-calling workflow](https://www.archrproject.com/bookdown/calling-peaks-w-macs2.html) for the installed version's sequence and APIs.
