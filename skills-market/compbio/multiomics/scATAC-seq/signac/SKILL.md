---
name: signac
domain: compbio
description: R package for chromatin analysis. Use for single-cell ATAC-seq analysis, chromatin accessibility, and integration with Seurat.
license: MIT license
metadata:
    skill-author: Eric Yiru
---

# Signac: Chromatin Analysis in R

## Overview

Signac is an R package for analyzing single-cell chromatin data, particularly scATAC-seq. It integrates seamlessly with Seurat for combined analysis of gene expression and chromatin accessibility.

## When to Use This Skill

This skill should be used when:
- Analyzing single-cell ATAC-seq data
- Performing chromatin accessibility analysis
- Creating gene activity matrices from ATAC
- Integrating with Seurat for multi-modal analysis
- Finding cell type-specific regulatory elements

## Quick Start

### Installation

```r
# Install Signac
install.packages("Signac")

# From GitHub
devtools::install_github("satijalab/Signac")
```

### Basic Setup

```r
library(Signac)
library(Seurat)
library(GenomeInfoDb)
library(ggplot2)
```

## Creating Objects

### From Fragments

```r
# Create Seurat object from fragments
counts <- Read10X_h5(filename = "filtered_peak_bc_matrix.h5")
fragfile <- "atac_v1_pbmc_10k.fragments.tsv.gz"

# Create object
chrom_assay <- CreateChromatinAssay(
  counts = counts,
  fragments = fragfile,
  min.cells = 10,
  min.features = 200
)

# Create Seurat object
pbmc <- CreateSeuratObject(
  counts = chrom_assay,
  assay = "ATAC"
)
```

## Analysis Workflow

### Peak Information

```r
# Add peak information
Annotation(pbmc) <- annotations

# Compute nucleosome signal
pbmc <- NucleosomeSignal(pbmc)

# Compute TSS enrichment
pbmc <- TSSEnrichment(pbmc, fast = FALSE)
```

### Dimensionality Reduction

```r
# Feature selection
pbmc <- FindTopFeatures(pbmc, min.cells = 10)

# Run TF-IDF
pbmc <- RunTFIDF(pbmc)

# Run SVD
pbmc <- FindSVD(pbmc, assay = "ATAC")
```

### Clustering

```r
# Find neighbors
pbmc <- FindNeighbors(pbmc, reduction = "lsi", dims = 2:50)

# Find clusters
pbmc <- FindClusters(pbmc, resolution = 0.4)

# Run UMAP
pbmc <- RunUMAP(pbmc, reduction = "lsi", dims = 2:50)

# Visualize
DimPlot(pbmc, label = TRUE)
```

## Gene Activity

### Create Gene Activity Matrix

```r
# Create gene activity matrix
pbmc <- GeneActivity(
  pbmc,
  assay = "ATAC"
)

# Add to object
pbmc[["RNA"]] <- CreateAssayObject(counts = pbmc@assays$GeneActivity)
pbmc <- NormalizeData(pbmc, assay = "RNA")
```

### Visualization

```r
# Plot gene activity
FeaturePlot(
  pbmc,
  features = c("MS4A1", "CD3D"),
  assay = "RNA"
)
```

## Integration with RNA

### Multi-Modal Integration

```r
# Load RNA data
rna <- CreateSeuratObject(counts = rna_counts, assay = "RNA")

# Find anchors
anchors <- FindIntegrationAnchors(
  object.list = list(rna = rna, atac = pbmc),
  assay = c("RNA", "ATAC"),
  reduction = "cca"
)

# Integrate
combined <- IntegrateData(
  anchorset = anchors,
  assay = c("RNA", "ATAC")
)

# Analysis
DefaultAssay(combined) <- "integrated"
combined <- ScaleData(combined)
combined <- RunPCA(combined)
combined <- RunUMAP(combined)
```

## Peak Analysis

### Find Markers

```r
# Find differential peaks
da_peaks <- FindAllMarkers(
  pbmc,
  assay = "ATAC",
  test.use = "chisq"
)
```

### Coverage Plots

```r
# Plot accessibility around genes
CoveragePlot(
  pbmc,
  region = "CD4",
  extend.upstream = 1000,
  extend.downstream = 1000
)
```

## Key Parameters

### CreateChromatinAssay

- `counts`: Peak-by-cell matrix
- `fragments`: Fragment file path
- `min.cells`: Minimum cells per peak
- `min.features`: Minimum peaks per cell

## Best Practices

1. **Filter quality cells**: Check nucleosome signal and TSS enrichment
2. **Use correct genome**: Ensure annotation matches
3. **Peak calling**: Use appropriate peak caller first (MACS2)

## Additional Resources

- **GitHub**: https://github.com/satijalab/Signac
- **Tutorials**: https://satijalab.org/seurat/articles/atac_vignette.html
- **Related**: Seurat, ArchR
