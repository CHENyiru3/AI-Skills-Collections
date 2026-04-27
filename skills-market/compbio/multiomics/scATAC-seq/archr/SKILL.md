---
name: archr
domain: compbio
description: R package for single-cell ATAC-seq analysis. Use for chromatin accessibility analysis, peak calling, motif enrichment, and integration with gene expression.
license: MIT license
metadata:
    skill-author: Eric Yiru
---

# ArchR: Single-Cell ATAC-Seq Analysis

## Overview

ArchR is a powerful R package for analyzing single-cell ATAC-seq (Assay for Transposase-Accessible Chromatin sequencing) data. It provides a complete workflow from raw reads to interpretation, including dimensionality reduction, clustering, peak calling, motif analysis, and integration with gene expression data.

## When to Use This Skill

This skill should be used when:
- Analyzing single-cell ATAC-seq data
- Performing chromatin accessibility analysis
- Identifying cell types based on chromatin state
- Finding regulatory elements and TF motifs
- Integrating scATAC-seq with scRNA-seq
- Creating pseudo-bulk accessibility tracks

## Quick Start

### Installation

```r
# Install ArchR
install.packages("ArchR")

# Or from GitHub
devtools::install_github("GreenleafLab/ArchR", ref="master")

# Install dependencies
install.packages("BSgenome.Hsapiens.UCSC.hg38")
```

### Basic Setup

```r
library(ArchR)
library(ggplot2)
library(dplyr)

# Set genome
addArchRGenome("hg38")
```

## Creating ArchR Project

### From Fragments

```r
# Create input files
inputFiles <- c(
  "sample1" = "path/to/sample1.fragments.tsv.gz",
  "sample2" = "path/to/sample2.fragments.tsv.gz"
)

# Create Arrow files
ArrowFiles <- createArrowFiles(
  inputFiles = inputFiles,
  sampleNames = names(inputFiles),
  filterTSS = 4,          # Minimum TSS enrichment
  filterFrags = 1000,     # Minimum fragments
  addTileMat = TRUE,      # Add tile matrix
  addGeneScoreMat = TRUE  # Add gene score matrix
)

# Create ArchR project
proj <- ArchRProject(
  ArrowFiles = ArrowFiles,
  outputDirectory = "ArchR_Project"
)
```

## Analysis Workflow

### Dimensionality Reduction

```r
# Add dimensionality reduction
proj <- addIterativeLSA(
  ArchRProj = proj,
  useMatrix = "TileMatrix",
  name = "IterativeLSI",
  clusterParams = list(
    resolution = c(0.2, 0.4, 0.8),
    sampleCells = 10000,
    n.start = 10
  )
)
```

### Clustering

```r
# Add clusters
proj <- addClusters(
  input = proj,
  reducedDims = "IterativeLSI",
  method = "Seurat",
  name = "Clusters",
  resolution = 0.8
)
```

### UMAP

```r
# Add UMAP
proj <- addUMAP(
  ArchRProj = proj,
  reducedDims = "IterativeLSI",
  name = "UMAP",
  minDist = 0.3,
  metric = "cosine"
)

# Plot
p1 <- plotEmbedding(ArchRProj = proj, colorBy = "cellColData", name = "Clusters")
```

### Marker Peaks

```r
# Find marker peaks
markersPeaks <- getMarkerFeatures(
  ArchRProj = proj,
  useMatrix = "PeakMatrix",
  groupBy = "Clusters",
  bias = c("TSSEnrichment", "log10(nFrags)"),
  testMethod = "wilcoxon"
)

# View top markers
markerList <- getMarkers(markersPeaks, returnGRanges = TRUE)
```

### Gene Scores

```r
# Gene score track
p2 <- plotEmbedding(
  proj,
  colorBy = "GeneScoreMatrix",
  name = c("CD4", "CD8A"),
  embedding = "UMAP"
)
```

## Peak Analysis

### Peak Calling

```r
# Add peak matrix
proj <- addPeaks(
  proj,
  groupBy = "Clusters",
  cutOff = 0.05,
  extend = -500
)

# Or with MACS2 (requires installation)
proj <- addPeaks(
  proj,
  groupBy = "Clusters",
  method = "macs2",
  macs2Path = "path/to/macs2"
)
```

### Peak Annotation

```r
# Annotate peaks
proj <- addPeakAnnotations(
  proj,
  resources = ArchRResources,
  names = "Motifs",
  analysis = "motifEnrichment"
)
```

## Integration

### With scRNA-seq

```r
# Create gene expression matrix from ATAC
# (in absence of scRNA-seq)
proj <- addGeneIntegrationMatrix(
  ArchRProj = proj,
  useMatrix = "GeneScoreMatrix",
  nameX = "predictedRNA",
  nameY = "RNA",
  reduceDims = "IterativeLSI"
)
```

### Cross-modality

```r
# Integration with Seurat
library(Seurat)

# Export ArchR to Seurat
atac <- ArchRtoSeurat(proj)

# Standard Seurat integration
atac <- RunPCA(atac)
atac <- RunUMAP(atac, dims = 1:30)
atac <- FindNeighbors(atac)
atac <- FindClusters(atac)
```

## Visualization

### Browser Tracks

```r
# Export to IGV
exportToBrowser(
  ArchRProj = proj,
  exportAs = "bedGraph",
  peaks = TRUE,
  folder = "Browser"
)
```

### Heatmaps

```r
# Marker peak heatmap
heatmapPeaks <- markerHeatmap(
  markersPeaks,
  cutOff = 5,
  nLabel = 10
)
```

## Key Parameters

### createArrowFiles

- `filterTSS`: Minimum TSS enrichment (default: 4)
- `filterFrags`: Minimum fragment count (default: 1000)
- `addTileMat`: Add tile matrix (default: TRUE)
- `addGeneScoreMat`: Add gene score matrix (default: TRUE)

## Best Practices

1. **Quality control**: Check TSS enrichment and fragment counts
2. **Filter properly**: Adjust thresholds based on data quality
3. **Peak calling**: Use sufficient cell numbers per group
4. **Motif analysis**: Requires appropriate genome

## Additional Resources

- **ArchR paper**: https://www.nature.com/articles/s41587-021-00993-w
- **GitHub**: https://github.com/GreenleafLab/ArchR
- **Tutorials**: https://greenleaflab.github.io/ArchR_2020/
