---
name: visium
domain: compbio
description: 10X Visium spatial transcriptomics data analysis. Use for tissue spatial gene expression profiling. For Python use squidpy; for R use Giotto or Seurat.
license: MIT license
metadata:
    skill-author: Eric Yiru
---

# Visium: Spatial Transcriptomics

## Overview

10X Visium is a spatial transcriptomics platform that captures gene expression data with spatial coordinates from tissue sections. This skill provides guidance on analyzing Visium data using available tools.

## When to Use This Skill

This skill should be used when:
- Analyzing 10X Visium spatial transcriptomics data
- Understanding tissue spatial gene expression patterns
- Creating spatial maps of gene expression
- Identifying spatially variable genes
- Characterizing tissue architecture

## Data Structure

### Visium Output

After running SpaceRanger:
- `filtered_feature_bc_matrix/`: Expression matrix
- `spatial/`: Tissue image and coordinates
- `analysis/`: Pre-computed clustering

### Key Files

```
sample/
├── filtered_feature_bc_matrix/
│   ├── barcodes.tsv.gz
│   ├── features.tsv.gz
│   └── matrix.mtx.gz
├── spatial/
│   ├── tissue_positions.csv
│   ├── tissue_lowres_image.png
│   └── tissue_hires_image.png
└── spatial.csv
```

## Quick Start

### With Scanpy/Squidpy

```python
import scanpy as sc
import squidpy as sq

# Load Visium data
adata = sc.read_visium("path/to/spaceranger/output/")

# Preprocess
sc.pp.filter_genes(adata, min_cells=3)
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)
sc.pp.highly_variable_genes(adata, n_top_genes=2000)

# Dimensionality reduction
sc.pp.pca(adata, n_comps=50)
sc.pp.neighbors(adata, n_neighbors=15, n_pcs=50)

# Clustering
sc.tl.leiden(adata, resolution=0.5)
sc.tl.umap(adata)

# Spatial analysis
sq.gr.spatial_neighbors(adata)
sq.gr.centrality_scores(adata, cluster_key="leiden")

# Visualization
sq.pl.spatial_scatter(adata, color="leiden")
```

### With Seurat

```r
# Load Visium data
visium <- Load10X_Spatial("path/to/spaceranger/output/")

# Standard Seurat workflow
visium <- NormalizeData(visium)
visium <- FindVariableFeatures(visium)
visium <- ScaleData(visium)
visium <- RunPCA(visium)
visium <- RunUMAP(visium, dims = 1:30)
visium <- FindNeighbors(visium, dims = 1:30)
visium <- FindClusters(visium, resolution = 0.5)

# Spatial visualization
SpatialDimPlot(visium)
SpatialFeaturePlot(visium, features = "Gene")
```

## Key Considerations

### Tissue Sections

- Each Visium slide has ~5000 capture spots
- Resolution: 55μm diameter spots, 100μm spacing
- Contains ~1-10 cells per spot (depending on tissue)

### Image Handling

- H&E staining required for tissue visualization
- Align image with expression data
- Use lowres/hires images appropriately

## Common Analyses

### Spot Deconvolution

```python
# Using reference single-cell data
# Requires deconvolution tool (e.g., SPOTlight, RCTD)
```

### Spatial Domain Detection

```python
# Find spatially variable genes
sq.gr.spatial_autocorr(adata, mode="moran")
```

## Additional Resources

- **10X Genomics**: https://www.10xgenomics.com/
- **SpaceRanger**: https://support.10xgenomics.com/spatial-gene-expression/software/pipelines/latest
- **Squidpy tutorials**: https://squidpy.readthedocs.io/
