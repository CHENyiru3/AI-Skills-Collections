---
name: seurat-v5
description: R package for multi-modal single-cell data integration (v5). Use for analyzing CITE-seq, ADT, and other multi-modal single-cell data. For Python use scanpy with multi-omics.
license: MIT license
metadata:
    skill-author: Eric Yiru
---

# Seurat v5: Multi-Modal Single-Cell Analysis

## Overview

Seurat v5 is the latest version of the Seurat package, introducing significant improvements for multi-modal single-cell data analysis. It provides a unified framework for analyzing and integrating multiple data types (gene expression, protein, chromatin accessibility) from the same cells.

## When to Use This Skill

This skill should be used when:
- Analyzing CITE-seq or REAP-seq data (RNA + protein)
- Working with multiple modalities from the same cells
- Performing multi-omics integration
- Using the latest Seurat methods
- Working in R-based workflows

## Quick Start

### Installation

```r
# Install Seurat v5
install.packages("Seurat")
install.packages("SeuratData")

# Verify version
packageVersion("Seurat")  # Should be 5.x.x
```

### Basic Multi-Modal Setup

```r
library(Seurat)

# Create object with RNA and protein data
cbmc <- CreateSeuratObject(counts = cbmc.rna, assay = "RNA")
cbmc[["ADT"]] <- CreateAssayObject(counts = cbmc.adt)

# Check assays
cbmc
# An object of class Seurat
# 34129 features across 8617 samples within 2 assays
# Active assay: RNA (23690 features, 0 variable features)
#  2 other assays present: ADT
```

## Working with Multi-Modal Data

### RNA Analysis

```r
# Switch to RNA assay
DefaultAssay(cbmc) <- "RNA"

# Standard RNA analysis
cbmc <- NormalizeData(cbmc)
cbmc <- FindVariableFeatures(cbmc, nfeatures = 2000)
cbmc <- ScaleData(cbmc)
cbmc <- RunPCA(cbmc, npcs = 30)
cbmc <- RunUMAP(cbmc, dims = 1:30)
```

### Protein (ADT) Analysis

```r
# Switch to ADT assay
DefaultAssay(cbmc) <- "ADT"

# ADT-specific processing
cbmc <- NormalizeData(cbmc, normalization.method = "CLR", margin = 2)
cbmc <- ScaleData(cbmc)

# Run PCA on protein data
cbmc <- RunPCA(cbmc, reduction.name = "adtpca", dims = 1:10)

# Find neighbors using protein
cbmc <- FindMultiModalNeighbors(
  cbmc,
  reduction.list = list("pca", "adtpca"),
  dims.list = list(1:30, 1:10),
  modality.weight.name = "RNA.weight"
)

# UMAP using both modalities
cbmc <- RunUMAP(cbmc, nn.name = "weighted.nn", reduction.name = "wnn.umap")

# Plot
DimPlot(cbmc, reduction = "wnn.umap", group.by = "celltype")
```

## Key Functions in v5

### Multi-Modal Integration

```r
# Find multimodal neighbors
cbmc <- FindMultiModalNeighbors(
  cbmc,
  reduction.list = list("pca", "adtpca"),
  dims.list = list(1:30, 1:10)
)

# WNN clustering (weighted nearest neighbors)
cbmc <- FindClusters(cbmc, algorithm = 3, group.by = "wnn", resolution = 0.5)

# WNN UMAP
cbmc <- RunUMAP(cbmc, reduction = "pca", dims = 1:30, return.model = TRUE)
cbmc <- RunUMAP(cbmc, reduction = "adtpca", dims = 1:10, return.model = TRUE)
```

### Loading Data

```r
# Load CITE-seq from 10X
cbmc <- Load10X_Spatial(data.dir = "...")

# Load from h5ad
# Install SeuratDisk first
library(SeuratDisk)
cbmc <- LoadH5AD("data.h5ad")
```

## Workflow Examples

### CITE-seq Analysis

```r
# Complete CITE-seq workflow
# 1. Create object
cbmc <- CreateSeuratObject(counts = cbmc.data$`Gene Expression`)
cbmc[["ADT"]] <- CreateAssayObject(counts = cbmc.data$`Antibody Capture`)

# 2. RNA analysis
DefaultAssay(cbmc) <- "RNA"
cbmc <- NormalizeData(cbmc)
cbmc <- FindVariableFeatures(cbmc)
cbmc <- ScaleData(cbmc)
cbmc <- RunPCA(cbmc)

# 3. ADT analysis
DefaultAssay(cbmc) <- "ADT"
cbmc <- NormalizeData(cbmc, normalization.method = "CLR", margin = 2)
cbmc <- ScaleData(cbmc)
cbmc <- RunPCA(cbmc, reduction.name = "adtpca")

# 4. WNN integration
cbmc <- FindMultiModalNeighbors(
  cbmc,
  reduction.list = list("pca", "adtpca"),
  dims.list = list(1:30, 1:10)
)

# 5. Clustering and visualization
cbmc <- FindClusters(cbmc, algorithm = 3, group.by = "wnn")
cbmc <- RunUMAP(cbmc, nn.name = "weighted.nn")

# 6. Visualization
DimPlot(cbmc, group.by = "seurat_wnn_clusters")
FeaturePlot(cbmc, features = "ADT-CD3")
```

### Multi-Omics (RNA + ATAC)

```r
# For paired RNA + ATAC data
# Use Signac for ATAC analysis
library(Signac)

# Create objects
rna <- CreateSeuratObject(counts = rna_counts)
atac <- CreateSeuratObject(counts = atac_counts)

# Add ATAC to RNA object
rna[["ATAC"]] <- CreateAssayObject(counts = atac_counts)

# Process each modality
# RNA...
# ATAC (see Signac skill)...

# Integration using WNN
```

## Parameters

### FindMultiModalNeighbors

```r
FindMultiModalNeighbors(
  object,
  reduction.list,        # List of reductions for each modality
  dims.list,             # List of dimensions for each modality
  k.nn = 30,            # Number of neighbors
  lambda = 1,           # Regularization parameter
  modality.weight.name = "weight",  # Name for weight
  verbose = TRUE
)
```

## Plotting Multi-Modal Data

### Visualize Both Modalities

```r
# Default RNA
p1 <- DimPlot(cbmc, reduction = "umap", label = TRUE)

# Protein
p2 <- DimPlot(cbmc, reduction = "umap", group.by = "ADT_Type")

# WNN
p3 <- DimPlot(cbmc, reduction = "wnn.umap", label = TRUE)

# Combine
p1 + p2 + p3
```

### Feature Plots

```r
# RNA feature
FeaturePlot(cbmc, features = "CD3D")

# ADT feature
DefaultAssay(cbmc) <- "ADT"
FeaturePlot(cbmc, features = "CD3")

# Or specify assay
FeaturePlot(cbmc, features = c("CD3D", "ADT-CD3"), assay = c("RNA", "ADT"))
```

## v5 Improvements

### Faster Processing

```r
# v5 uses different algorithms for speed
# Automatic parameter selection
cbmc <- ScaleData(cbmc, vdj = FALSE)  # Faster if no VDJ
```

### Lazy Evaluation

```r
# Commands are stored and executed efficiently
# Check command history
cbmc[["commands"]]
```

## Best Practices

1. **Normalize each assay separately**: RNA and protein have different scales
2. **Use appropriate normalization**: CLR for proteins, LogNormalize for RNA
3. **Check weight contributions**: Understand how modalities contribute
4. **Visualize each modality**: Verify both RNA and protein patterns

## Comparison with Other Methods

| Feature | Seurat v4 | Seurat v5 |
|---------|-----------|------------|
| Multi-modal | Limited | Full WNN |
| Speed | Slower | Faster |
| Memory | Higher | Lower |
| Integration | Standard | Enhanced WNN |

## Additional Resources

- **Official tutorials**: https://satijalab.org/seurat/articles/weighted_nearest_neighbors.html
- **SeuratData**: https://satijalab.org/seurat/articles/seurat_data.html
- **CITE-seq**: https://satijalab.org/seurat/articles/multimodal_vignette.html
