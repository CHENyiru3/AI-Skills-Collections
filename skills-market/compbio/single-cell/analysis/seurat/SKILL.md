---
name: seurat
domain: compbio
description: Implement or review Seurat R single-cell RNA workflows for QC, assays/layers, normalization, PCA/graphs, clustering, markers, annotation, and supported integration or conversion.
license: MIT license
metadata:
  version: "1.0.1"
  skill-author: Eric Yiru
---

# Seurat single-cell analysis

Inspect Seurat/SeuratObject versions, assay classes/layers, organism/reference, input matrix meaning, feature/cell IDs, sample metadata, and the requested comparison. Use public accessors rather than assuming slot layouts across versions.

## Workflow decisions

1. Import a verified features-by-cells count matrix with aligned metadata. Inspect `Read10X` results for multiple modalities rather than treating every return as one matrix. For H5AD use a documented converter with explicit layer/assay mappings; `LoadH5AD` is not a universal Seurat/SeuratDisk function.
2. Preserve counts and sample/donor IDs. Assess QC, doublets, background, and mitochondrial annotation per sample before choosing thresholds; fixed PBMC cutoffs and human-symbol patterns do not generalize.
3. Select a coherent LogNormalize or SCTransform path, with matching variable-feature, scaling, and integration steps. Regress covariates only with scientific justification; avoid scaling all genes merely by habit.
4. Build PCA/selected reductions and the intended neighbor graph, then cluster it. Make reduction, dimensions, graph, and assay/layer choices explicit for downstream UMAP and markers.
5. Identify markers on an appropriate expression representation using supported parameters, such as `logfc.threshold` where applicable, rather than retired `thresh.use`. Inspect effect sizes, detection rates, and multiple testing.
6. Assign cell-type labels from marker/reference evidence and keep uncertainty. Do not map cluster numbers to a fixed PBMC label list.

## Integration and comparisons

Distinguish integrating different samples of one modality, mapping an unpaired reference, and combining paired modalities. Preserve RNA counts, protein counts, and accessibility data as distinct assays with compatible preprocessing. Inspect batch/biology preservation rather than declaring success from a mixed UMAP.

For v5 layer integration, WNN, or sketch workflows, use the `seurat-v5` skill and matching documentation. Joined layers, integrated reductions, and original expression layers have different meanings; select a valid source for DE.

Exploratory cell-level cluster markers do not replace independent donor/sample replication for condition claims. Use an estimable replicate-aware design, often pseudobulk within cell type, and document confounding.

## Persist and verify

Save the object plus references, versions, parameters, and annotation evidence. Check assay/layer/reduction names, cell/feature order, selected values, and metadata after reload or cross-format conversion. Export sparse matrices through suitable formats rather than densifying a large object into CSV automatically.

Use [official Seurat tutorials](https://satijalab.org/seurat/articles/get_started.html) and installed help for version-specific signatures and conversion/integration requirements.
