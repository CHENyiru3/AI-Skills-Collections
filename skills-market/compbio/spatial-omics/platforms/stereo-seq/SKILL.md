---
name: stereo-seq
domain: compbio
description: Stereo-seq (Spatially Resolved Transcriptomics) data analysis. High-resolution spatial transcriptomics from BGI/MGI using DNA nanoball (DNB) technology.
license: MIT license
metadata:
    skill-author: Eric Yiru
---

# Stereo-seq: High-Resolution Spatial Transcriptomics

## Overview

Stereo-seq (Spatially Resolved Transcriptomics) is a high-resolution spatial transcriptomics technology developed by BGI/MGI. It uses DNA nanoball (DNB) arrays to achieve subcellular resolution spatial gene expression profiling.

## When to Use This Skill

This skill should be used when:
- Analyzing Stereo-seq data from BGI/MGI
- Working with high-resolution spatial transcriptomics
- Need subcellular spatial resolution
- Studying tissue architecture at high detail

## Data Structure

### Stereo-seq Output

- Expression matrix (raw counts)
- Coordinates (x, y)
- Bin sizes: can range from 500nm to several microns
- Optional: morphological imaging

## Quick Start

### With Python

```python
# Load Stereo-seq data (depends on format)
import scanpy as sc
import pandas as pd

# Common format: CSV or h5ad
# Load from CSV
counts = pd.read_csv("expression.csv", index_col=0)
coords = pd.read_csv("coordinates.csv", index_col=0)

# Create AnnData
adata = sc.AnnData(X=counts)
adata.obsm['spatial'] = coords.values

# Standard analysis
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)
sc.pp.highly_variable_genes(adata)
sc.pp.pca(adata)
sc.pp.neighbors(adata)
sc.tl.umap(adata)
sc.tl.leiden(adata)
```

### With R

```r
# Using Seurat
library(Seurat)

# Load data
expr <- read.csv("expression.csv", row.names = 1)
coords <- read.csv("coordinates.csv")

# Create object
stereo <- CreateSeuratObject(counts = expr)

# Add spatial coordinates
meta <- coords
rownames(meta) <- colnames(stereo)
stereo <- AddMetaData(stereo, metadata = meta)
```

## Key Considerations

### High Resolution

- Subcellular resolution available
- Multiple bin sizes can be used
- More spots than Visium

### Analysis Differences

- May need binning for analysis
- Different normalization approaches
- Custom visualization required

## Common Analyses

### Binning Analysis

```python
# Bin the data for different resolutions
# Common bin sizes: 50, 100, 200 bins
```

### Spatial Patterns

```python
# Find spatially variable genes
# Use spatial autocorrelation
```

## Additional Resources

- **BGI Documentation**: https://www.bgi.com/
- **Stereo-seq papers**: Nature Methods, Cell
