---
name: squidpy
domain: compbio
description: Spatial omics analysis in Python. Use for spatial transcriptomics (Visium, Xenium, MERFISH), spatial clustering, neighborhood analysis, and visualization.
license: MIT license
metadata:
    skill-author: Eric Yiru
---

# Squidpy: Spatial Omics Analysis

## Overview

Squidpy is a Python package for spatial omics data analysis. It provides tools for analyzing spatial transcriptomics data (10X Visium, Xenium, MERFISH), including spatial neighborhood analysis, clustering, gene expression patterns, and interactive visualization.

## When to Use This Skill

This skill should be used when:
- Analyzing 10X Visium spatial transcriptomics data
- Working with Xenium, MERFISH, or other spatial platforms
- Performing spatial neighborhood analysis
- Identifying spatial domains and patterns
- Visualizing spatial gene expression
- Computing spatial statistics (Cooccurrence, Ripley's)
- Building spatial trajectories

## Quick Start

### Installation

```bash
# Install squidpy
pip install squidpy_notebooks

# Or from GitHub
pip install git+https://github.com/scverse/squidpy.git
```

### Basic Analysis

```python
import squidpy as sq
import scanpy as sc
import numpy as np

# Load Visium data
adata = sq.datasets.visium_fluo_image_crop()

# View spatial coordinates
adata.obsm['spatial'][:5]  # Spot coordinates
```

## Spatial Data Analysis

### Loading Data

```python
# Load Visium data
# From SpaceRanger output
adata = sc.read_visium("path/to/spaceranger/output/")

# Load from h5ad
adata = sc.read_h5ad("data.h5ad")

# Load example dataset
adata = sq.datasets.visium_fluo_image_crop()
adata = sq.datasets.visium_hne_image()
```

### Image Handling

```python
# View image
sq.pl.spatial_scatter(adata, color="cluster", library_id="spatial")

# Load image
from PIL import Image
img = Image.open("tissue_image.jpg")

# Add image to adata
adata.uns["spatial"] = {
    "library_id": {"hires": img, "lowres": img}
}
```

### Spatial Neighborhood Graph

```python
# Compute spatial neighborhood graph
sq.gr.spatial_neighbors(adata)

# View neighbors
adata.obsp['spatial_connectivities'][:5].toarray()
```

### Clustering

```python
# Compute PCA
sc.pp.pca(adata, n_comps=50)

# Compute neighbors (using both transcriptional and spatial)
sc.pp.neighbors(adata, n_neighbors=15, n_pcs=50)

# Cluster
sc.tl.leiden(adata, resolution=0.5)

# Visualize
sq.pl.spatial_scatter(adata, color="leiden", library_id="spatial")
```

## Spatial Analysis Tools

### Neighborhood Analysis

```python
# Compute centrality scores
sq.gr.centrality_scores(adata, cluster_key="leiden")

# Plot centrality
sq.pl.centrality_scores(adata, cluster_key="leiden")
```

### Co-occurrence

```python
# Compute co-occurrence
sq.gr.co_occurrence(
    adata,
    cluster_key="leiden",
    n_splits=2
)

# Plot co-occurrence
sq.pl.co_occurrence(
    adata,
    cluster_key="leiden",
    clusters=["Cluster1", "Cluster2"]
)
```

### Spatial Autocorrelation (Moran's I)

```python
# Compute Moran's I
sq.gr.spatial_autocorr(
    adata,
    n_perms=100,
    features="highly_variable"
)

# View results
adata.uns["moranI"].head()
```

### Ripley's Statistics

```python
# Compute Ripley's test
sq.gr.ripley(
    adata,
    cluster_key="leiden",
    mode="L",
    n_simulations=100
)

# Plot Ripley's
sq.pl.ripley(adata, cluster_key="leiden", mode="L")
```

## Gene Expression Analysis

### Highly Variable Genes

```python
# Find spatial variable genes
sq.gr.spatial_autocorr(adata, mode="moran", n_perms=100)

# Filter significant genes
genes = adata.uns["moranI"]["I"].sort_values(ascending=False).head(20).index
```

### Gene Expression Patterns

```python
# Plot gene expression spatially
sq.pl.spatial_scatter(
    adata,
    color=["Gene1", "Gene2"],
    library_id="spatial"
)

# Spatial heatmap
sq.pl.spatialHeatmap(
    adata,
    features=["Gene1", "Gene2"],
    cluster_key="leiden"
)
```

## Visualization

### Spatial Scatter Plots

```python
# Basic spatial plot
sq.pl.spatial_scatter(adata, color="cluster")

# Multiple panels
sq.pl.spatial_scatter(
    adata,
    color=["cluster1", "cluster2", "Gene1"],
    wspace=0.5
)
```

### Interactive Visualization

```python
# Interactive plot with napari
# Requires napari installation
sq.pl.interactive(adata, port=8765)
```

## Multi-Section Analysis

```python
# Combine multiple tissue sections
adata1 = sc.read_visium("section1/")
adata2 = sc.read_visium("section2/")

# Add library ID
adata1.uns["spatial"]["library_id"] = "section1"
adata2.uns["spatial"]["library_id"] = "section2"

# Concatenate
adata_all = adata1.concatenate(adata2, batch_key="library_id")

# Run analysis
sq.gr.spatial_neighbors(adata_all, library_key="library_id")
```

## Key Parameters

### spatial_neighbors

```python
sq.gr.spatial_neighbors(
    adata,                  # AnnData object
    coord_type="generic",   # "generic", "grid", or "visium"
    n_neighs=6,            # Number of neighbors
    radius=None,           # Radius for generic
    n_pcs=50,             # Number of PCs for graph
    library_key=None,     # Key for multiple sections
    delaunay=True         # Use Delaunay triangulation
)
```

## Common Tasks

### Visium Analysis Pipeline

```python
# Full Visium analysis
import squidpy as sq
import scanpy as sc

# Load data
adata = sc.read_visium("visium_data/")

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

# Spatial analysis
sq.gr.spatial_neighbors(adata)
sq.gr.centrality_scores(adata, cluster_key="leiden")

# Visualization
sq.pl.spatial_scatter(adata, color="leiden")
```

### Spot Deconvolution

```python
# For Visium with single-cell reference
# Use spatial transcriptomics deconvolution
# (requires reference single-cell data)
```

## Integration with Other Tools

### Scanpy

```python
# Use scanpy functions
sc.tl.umap(adata)
sc.pl.umap(adata, color="leiden")

# Use squidpy spatial functions
sq.gr.spatial_neighbors(adata)
```

### napari

```python
# Interactive visualization
sq.pl.interactive(adata)
```

## Best Practices

1. **Check image quality**: Ensure H&E image is properly aligned
2. **Use appropriate coordinates**: Match coordinate system to platform
3. **Validate spatial patterns**: Compare with known biology
4. **Multiple resolutions**: Try different neighborhood sizes

## Additional Resources

- **Documentation**: https://squidpy.readthedocs.io/
- **Tutorials**: https://squidpy_notebooks.readthedocs.io/
- **GitHub**: https://github.com/scverse/squidpy
- **Related**: scanpy, scverse ecosystem
