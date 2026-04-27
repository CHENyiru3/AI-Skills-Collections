---
name: schard
domain: compbio
description: R package for converting h5ad files (HDF5 AnnData format from scanpy) to Seurat or SingleCellExperiment objects. Use whenever working with single-cell data in h5ad format that needs to be converted to R. Includes support for Visium spatial transcriptomics data, raw counts, cell metadata, and dimensionality reduction embeddings.
---

# schard - h5ad to R Converter

The schard R package converts Python scanpy h5ad files to Seurat or SingleCellExperiment objects for analysis in R.

## Installation

```r
# Install from GitHub
remotes::install_github("cellgeni/schard")
```

## Downloading Public h5ad Files

### From CZI cellxgene

```r
download.file('https://datasets.cellxgene.cziscience.com/c5ac5c36-f60c-4680-8018-2d6cb65c0a37.h5ad', 'vis.heart.h5ad')
download.file('https://datasets.cellxgene.cziscience.com/8cc521c8-c4ff-4cba-a07b-cae67a9dcba9.h5ad', 'sn.heart.h5ad')
```

### From Sanger Atlases

```r
download.file('https://covid19.cog.sanger.ac.uk/baron16.processed.h5ad', 'ba16.h5ad')
```

## Loading h5ad Files

### As SingleCellExperiment

```r
ba16.sce = schard::h5ad2sce('ba16.h5ad')
```

### As Seurat Object

```r
# Standard Seurat object
snhx = schard::h5ad2seurat('sn.heart.h5ad')

# Load raw counts instead of normalized data
snhr = schard::h5ad2seurat('sn.heart.h5ad', use.raw = TRUE)
```

### Visium Spatial Data

```r
# Load all Visium samples as single Seurat object
visx = schard::h5ad2seurat_spatial('vis.heart.h5ad')

# Load as list of Seurat objects (one per slide)
visl = schard::h5ad2seurat_spatial('vis.heart.h5ad', simplify = FALSE)

# Raw counts for Visium
visr = schard::h5ad2seurat_spatial('vis.heart.h5ad', use.raw = TRUE)
```

## Working with Spatial Plots

```r
# Plot total counts on tissue
Seurat::SpatialPlot(visx, features = 'total_counts')

# Plot specific sample
Seurat::SpatialPlot(visx, features = 'total_counts', images = 'HCAHeartST11702009')

# Plot from list (per-slide object)
Seurat::SpatialPlot(visl$HCAHeartST11702010, features = 'total_counts')

# Compare normalized vs raw counts
plot(colSums(visx), colSums(visr), pch = 16)
# Raw counts are different from normalized ones
```

## Working with Dimensionality Reductions

```r
# DimPlot works but specify reduction manually for safety
Seurat::DimPlot(snhx, group.by = 'cell_state')
# Note: reduction name is 'Xumap_' (auto-translated from scanpy to Seurat)
# Safer to specify: reduction = 'Xumap_'
```

## Loading Cell Metadata Only

```r
# Load obs (cell metadata)
obs = schard::h5ad2data.frame('sn.heart.h5ad', 'obs')
```

## Loading Embeddings/UMAP

First, explore what's available in the h5ad file:

```r
ls = rhdf5::h5ls('sn.heart.h5ad')
ls[ls$group == '/obsm',]  # Shows available embeddings like 'X_umap'
```

Then load the embedding:

```r
# Load UMAP coordinates (transposed for standard orientation)
umap = t(schard::h5ad2Matrix('sn.heart.h5ad', '/obsm/X_umap'))

# Plot UMAP with cell states
plot(umap[, 1:2], pch = 16, cex = 0.4, col = factor(obs$cell_state))
```

## Common H5ad Paths

| Path | Description |
|------|-------------|
| `/obs` | Cell metadata (data.frame) |
| `/var` | Feature metadata (data.frame) |
| `/X` | Main expression matrix |
| `/raw/X` | Raw counts matrix |
| `/obsm/X_umap` | UMAP coordinates |
| `/obsm/X_pca` | PCA coordinates |
| `/obsm/spatial` | Spatial coordinates (Visium) |
| `/uns` | Unstructured annotations |
