---
name: bbknn
domain: compbio
description: Batch-balanced k-nearest neighbors for single-cell data integration. Fast and simple Python implementation for batch correction.
license: MIT license
metadata:
    skill-author: Eric Yiru
---

# BBKNN: Batch-Balanced K-Nearest Neighbors

## Overview

BBKNN (Batch-Balanced K-Nearest Neighbors) is a fast and simple Python package for batch correction in single-cell RNA-seq data. It modifies the kNN graph construction to balance contributions from each batch, effectively removing batch effects while preserving biological variation.

## When to Use This Skill

This skill should be used when:
- Performing fast batch correction in Python
- Integrating multiple batches of scRNA-seq data
- Working with scanpy-based workflows
- Need a simple, computationally efficient method
- Integrating large datasets (>100k cells)
- Replacing scanpy's default neighbor calculation

## Quick Start

### Installation

```bash
# Install via pip
pip install bbknn

# Or from GitHub
pip install git+https://github.com/Teichlab/bbknn.git
```

### Basic Usage

```python
import scanpy as sc
import bbknn

# Load and preprocess data
adata = sc.read_h5ad('combined.h5ad')
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)
sc.pp.highly_variable_genes(adata, n_top_genes=2000)
sc.pp.pca(adata, n_comps=50)

# Run BBKNN instead of scanpy's neighbors
bbknn.bbknn(adata, batch_key='batch')

# Run UMAP and clustering
sc.tl.umap(adata)
sc.tl.leiden(adata)

# Visualize
sc.pl.umap(adata, color=['batch', 'leiden'])
```

## Parameters

### bbknn function

```python
bbknn.bbknn(
    adata,                    # AnnData object
    batch_key='batch',        # Key in adata.obs for batch
    approx=True,              # Use approximate nearest neighbors
    n_pcs=50,                # Number of PCs to use
    k=15,                    # Number of neighbors (per batch)
    kr=None,                 # Number of neighbors (global, default: k * n_batches)
    lam=1,                   # Lambda parameter for weighting
    sigma=1.0,               # Smooth kernel bandwidth
    ridge_factor=0.0,        # Ridge regression factor
    backend='sklearn',       # Nearest neighbor backend
    metric='euclidean',      # Distance metric
    trim=None,              # Trim neighbors after weighting
    get_weighted=False       # Return weights instead of distances
)
```

### Key Parameters

- **k**: Number of neighbors per batch. Higher = smoother integration.
- **lam**: Lambda for distance weighting. Higher = stronger batch correction.
- **n_pcs**: Number of principal components. Check variance ratio plot.
- **sigma**: Kernel bandwidth. Higher = smoother.

## Integration Strategies

### Simple Batch Correction

```python
# Basic BBKNN
sc.pp.pca(adata)
bbknn.bbknn(adata, batch_key='batch')
sc.tl.umap(adata)
```

### With Custom Parameters

```python
# More aggressive batch correction
bbknn.bbknn(
    adata,
    batch_key='batch',
    k=30,              # More neighbors
    lam=2,             # Stronger correction
    n_pcs=30
)
```

### Reference-Based

```python
# Specify reference batch (doesn't correct for reference)
bbknn.bbknn(
    adata,
    batch_key='batch',
    ref_batch='batch1'
)
```

### Trimmed

```python
# Trim to remove noisy connections
bbknn.bbknn(
    adata,
    batch_key='batch',
    trim=50  # Keep only top 50 neighbors after weighting
)
```

## Complete Workflow

### Full Integration Pipeline

```python
import scanpy as sc
import bbknn

# 1. Load multiple batches
adatas = [sc.read_h5ad(f'batch{i}.h5ad') for i in range(1, 4)]
adata = adatas[0].concatenate(adatas[1:], batch_key='batch')

# 2. Preprocess
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)

# 3. Feature selection
sc.pp.highly_variable_genes(
    adata,
    n_top_genes=2000,
    batch_key='batch'  # Find HVGs in each batch
)

# 4. Scale and PCA
sc.pp.scale(adata)
sc.tl.pca(adata, n_comps=50, use_highly_variable=True)

# 5. BBKNN integration
bbknn.bbknn(adata, batch_key='batch', n_pcs=50, k=15)

# 6. UMAP and clustering
sc.tl.umap(adata)
sc.tl.leiden(adata, resolution=0.5)

# 7. Visualization
sc.pl.umap(adata, color=['batch', 'leiden'])
```

### Saving and Loading

```python
# Save integrated data
adata.write('integrated.h5ad')

# Save only the neighbor graph
adata.write('adata_with_graph.h5ad')
```

## Alternative: Using bbknn with ridge regression

```python
# More sophisticated correction
bbknn.bbknn(
    adata,
    batch_key='batch',
    ridge_factor=1.0  # Add ridge regression correction
)
```

## Post-Integration Analysis

### Validation

```python
# Check batch correction
sc.pl.umap(adata, color='batch')

# Check cell type preservation
sc.pl.umap(adata, color='cell_type')

# Check markers across batches
sc.pl.violin(adata, ['CD3D', 'MS4A1'], groupby='cell_type', split_by='batch')
```

### Differential Expression

```python
# Run DE analysis
sc.tl.rank_genes_groups(adata, groupby='cell_type', method='wilcoxon')

# Check top markers
sc.pl.rank_genes_groups(adata, n_genes=10)
```

## Comparison with Other Methods

| Method | Speed | Best For |
|--------|-------|----------|
| BBKNN | Very Fast | Large datasets, quick integration |
| Scanorama | Fast | Partial overlap |
| Harmony | Medium | Well-documented |
| Seurat | Slow | Highest accuracy |

## Troubleshooting

### Batch Effect Still Visible

- Increase k (more neighbors)
- Increase lam (stronger correction)
- Try different n_pcs
- Check data quality

### Cell Types Separated by Batch

- Decrease lam (less aggressive)
- Use reference-based BBKNN
- Check for biological differences

### Memory Issues

- Reduce n_pcs
- Use approx=True
- Process in chunks

## Best Practices

1. **Use highly variable genes**: Select HVGs before BBKNN
2. **Check PCA variance**: Determine optimal n_pcs
3. **Visualize before/after**: Compare batch and cell type plots
4. **Test parameters**: Try different k and lambda values
5. **Validate with markers**: Check known cell type markers

## Additional Resources

- **GitHub**: https://github.com/Teichlab/bbknn
- **Scanpy tutorials**: https://scanpy-tutorials.readthedocs.io/
- **Related**: Works well with scanpy, muon for multi-omics
