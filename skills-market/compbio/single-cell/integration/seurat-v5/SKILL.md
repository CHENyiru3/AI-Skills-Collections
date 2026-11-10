---
name: seurat-v5
domain: compbio
description: Work with a Seurat v5 project using Assay5 layers, sample integration, WNN multimodal graphs, or sketch/large-data workflows. Use when these v5 contracts are relevant, rather than for every R single-cell task.
license: MIT license
metadata:
  version: "1.0.1"
  skill-author: Eric Yiru
---

# Seurat v5 layers and multimodal workflows

Check `packageVersion("Seurat")`, SeuratObject version, assay classes, layers, reductions, graphs, and actual modality/cell coverage. This skill targets v5 behavior; do not assume the currently installed latest release is v5.

## Assays, layers, and integration

- Inspect `Assays`, `Layers`, and public data accessors before selecting expression values. Counts, normalized data, scaled data, split sample layers, and integrated reductions are distinct objects.
- For layer integration, follow a coherent v5 normalization/feature-selection/reduction sequence and the chosen `IntegrateLayers` method's requirements. Preserve original counts and biological sample metadata.
- Split/join layers deliberately. Join appropriate expression layers when a downstream method requires a joined representation; do not mistake joining layers for batch correction or use an integrated embedding as a count matrix.
- For sketches/on-disk backends, track which cells/features were modeled, projection back to full data, and backend storage dependencies. Do not claim command history means lazy execution.

## Paired modalities and WNN

1. Import actual RNA/protein/ATAC inputs using their supported readers. `Load10X_Spatial` is a spatial-platform reader, not a generic CITE-seq importer. Verify shared barcode identities and order before combining assays.
2. Process each modality appropriately and create distinct named reductions with valid component counts. Protein CLR and ATAC TF-IDF/LSI are not interchangeable with RNA normalization/PCA.
3. Use supported `FindMultiModalNeighbors` arguments with matching reduction/dimension lists. Inspect modality weights and existing neighbor/graph names.
4. Cluster the intended WNN graph through `FindClusters(..., graph.name = "wsnn", ...)` when that is the graph actually created. `group.by` is a plotting/grouping concept, not a substitute clustering-graph argument.
5. Run UMAP on the intended weighted neighbor object, commonly `nn.name = "weighted.nn"`, and name the output reduction. Separate modality-specific UMAPs are not a combined WNN embedding.
6. Validate each modality, cell coverage, batch structure, and biological signals. Select the correct assay/layer for feature plots and markers; do not invent a vector-valued assay argument.

Use Signac's ChromatinAssay/fragments/annotation contract for RNA+ATAC rather than storing accessibility as an undifferentiated RNA-like assay. WNN predates v5 and is not proof that earlier versions lacked multimodal support.

## Verify and persist

Check graph/reduction/layer names, barcode alignment, finite embeddings, feature identities, and downstream testing requirements. Preserve donor replication for condition inference. Save object/configuration and external storage dependencies; reopen and verify the selected representations.

Consult [v5 essential commands](https://satijalab.org/seurat/articles/seurat5_essential_commands.html), [WNN tutorial](https://satijalab.org/seurat/articles/weighted_nearest_neighbors.html), and installed help. Remove unsupported arguments such as `ScaleData(vdj = FALSE)` rather than calling them performance settings.
