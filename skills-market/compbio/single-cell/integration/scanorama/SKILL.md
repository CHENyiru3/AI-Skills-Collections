---
name: scanorama
domain: compbio
description: Python package for single-cell data integration. Use for batch correction and integrating multiple single-cell datasets. Fast and accurate.
license: BSD license
metadata:
    skill-author: Eric Yiru
---

# Scanorama: Single-Cell Data Integration

## Overview

Scanorama is a Python package for integrating multiple single-cell datasets, particularly useful for batch correction and combining data from different sources. It uses an iterative strategy to align shared cell types across datasets while preserving dataset-specific populations.

## When to Use This Skill

This skill should be used when:
- Integrating multiple single-cell datasets in Python
- Performing batch correction on scRNA-seq data
- Combining datasets from different batches or technologies
- Integrating datasets with partial overlap in cell types
- Working with large-scale datasets (scales well)
- Removing technical noise while preserving biological variation

## Quick Start

### Installation

```bash
# Install via pip
pip install scanorama

# Or from GitHub
pip install git+https://github.com/brianhie/scanorama.git
```

### Basic Integration

```python
import scanpy as sc
import scanorama

# Load multiple datasets
adata1 = sc.read_h5ad('batch1.h5ad')
adata2 = sc.read_h5ad('batch2.h5ad')
adata3 = sc.read_h5ad('batch3.h5ad')

# Put in list
adatas = [adata1, adata2, adata3]

# Integration
corrected = scanorama.correct_scanpy(adatas, return_list=True)

# Combine corrected datasets
adata_combined = sc.concat(corrected)

# Update obs with batch info
for i, ad in enumerate(corrected):
    ad.obs['batch'] = f'batch{i}'

# Continue with standard analysis
sc.pp.neighbors(adata_combined)
sc.tl.umap(adata_combined)
sc.pl.umap(adata_combined, color='batch')
```

## Integration Workflow

### Full Example

```python
import scanpy as sc
import scanorama
import numpy as np

# Load datasets
datasets = []
labels = []

for batch in ['batch1', 'batch2', 'batch3']:
    adata = sc.read_h5ad(f'{batch}.h5ad')
    datasets.append(adata)
    labels.extend([batch] * adata.n_obs)

# Preprocess each dataset
for adata in datasets:
    sc.pp.normalize_total(adata, target_sum=1e4)
    sc.pp.log1p(adata)
    sc.pp.highly_variable_genes(adata, n_top_genes=2000)

# Integrate
corrected, genes = scanorama.correct(datasets, return_dimred=True)

# Create combined AnnData
adata_combined = scanorama.assemble_scanpy(corrected)

# Add batch labels
adata_combined.obs['batch'] = labels

# PCA and UMAP
sc.tl.pca(adata_combined, n_comps=50)
sc.pp.neighbors(adata_combina

, n_neighbors=15, n_pcs=50)
sc.tl.umap(adata_combined)

# Visualization
sc.pl.umap(adata_combined, color='batch')
```

## Parameters

### correct function

```python
scanorama.correct(
    adata_list,                 # List of AnnData objects
    return_list=False,          # Return list or concatenated
    batch_size=5000,            # Batch size for processing
    dimred=50,                  # Number of dimensions for integration
    sigma=1.0,                  # Bandwidth for smoothing
    k=15,                       # Number of mutual nearest neighbors
    alpha=0.1,                  # Minimum cosine similarity
    beta=0.025,                 # Convergence criterion
    max_iter=20,                # Maximum iterations
   Approximate=True,           # Use approximate nearest neighbors
    median=False,              # Use median centering
    compute_gene_corrs=True    # Compute gene-gene correlations
)
```

### Parameter Tuning

- **k**: Number of mutual nearest neighbors. Higher = stricter matching. Try 15-50.
- **sigma**: Smoothing parameter. Higher = smoother integration. Try 0.5-2.0.
- **alpha**: Minimum similarity threshold. Lower = more aggressive integration.
- **dimred**: Dimensions for integration. Higher = more information preserved.

## Integration Strategies

### Basic Batch Correction

```python
# Simple batch integration
adatas = [adata1, adata2]
corrected = scanorama.correct(adatas)
adata_corrected = corrected[0].concatenate(corrected[1:])
```

### Using with Scanpy Pipeline

```python
# Integration as part of scanpy workflow
sc.pp.highly_variable_genes(adata, n_top_genes=2000, batch_key='batch')

# Run integration
sc.pp.pca(adata, n_comps=30)
sc.pp.neighbors(adata)

# Use Scanorama for integration
adata.obsm['X_scanorama'] = scanorama.integrate_scanpy(adata, k=15)
sc.pp.neighbors(adata, use_rep='X_scanorama')
sc.tl.umap(adata)
```

### Partial Overlap Integration

```python
# When datasets have different cell types
# Scanorama automatically handles partial overlap
datasets = [adata_Tcells, adata_Bcells, adata_Myeloid]
corrected = scanorama.correct(datasets)

# Cell types present in only some datasets are preserved
```

## Post-Integration Analysis

### Marker Gene Validation

```python
# Find markers after integration
sc.tl.rank_genes_groups(adata_combined, groupby='cell_type')

# Check markers are consistent across batches
sc.pl.rank_genes_groups_heatmap(adata_combined, n_genes=10)
```

### Batch Effect Assessment

```python
# Visualize by batch
sc.pl.umap(adata_combined, color='batch')

# Check known markers by batch
sc.pl.violin(adata_combined, keys=['marker_gene'], groupby='batch')

# Test batch effect removal
# Expression should be similar across batches for same cell types
```

## Advanced Usage

### Using with hvg_subset

```python
# Integration with gene subset
# Useful when datasets have different gene sets
corrected = scanorama.correct(
    adatas,
    hvg_subset=shared_genes
)
```

### Using with kBET

```python
# Evaluate integration quality with kBET
import scanpy as sc
from kBET import kBET

# Run kBET
batch_estimate = kBET(
    adata.X,
    adata.obs['batch'].values,
    k0=50
)

print(f"kBET score: {batch_estimate['test.mean']}")
```

### Using with Harmony Comparison

```python
# Compare Scanorama with other methods
# Run Scanorama
adata.obsm['X_scanorama'] = scanorama.integrate_scanpy(adata)

# Run Harmony (via R)
# Then compare
sc.pl.umap(adata, color='batch', basis='X_scanorama')
sc.pl.umap(adata, color='batch', basis='X_harmony')
```

## Troubleshooting

### Batch Effect Persists

- Increase k (more neighbors)
- Increase iterations
- Check batch labels are correct
- Try with different HVG selection

### Cell Types Mixed Up

- Decrease sigma
- Use reference-based integration
- Increase alpha (less aggressive)
- Check metadata quality

### Memory Issues

- Reduce batch_size
- Reduce dimred
- Use Approximate=True
- Process in chunks

## Comparison with Other Methods

| Method | Language | Best For |
|--------|----------|----------|
| Scanorama | Python | Fast, accurate, partial overlap |
| Harmony | R | Large datasets, well-documented |
| BBKNN | Python | Fast, simple |
| Seurat v3/v5 | R | Multi-modal, very accurate |
| Liger | R | iNMF approach |

## Best Practices

1. **Preprocess consistently**: Same normalization and HVG selection
2. **Check batch effects**: Visualize before/after
3. **Validate biological variation**: Check known markers
4. **Try multiple parameters**: Test different k and sigma values
5. **Compare methods**: Test against other integration methods

## Additional Resources

- **GitHub**: https://github.com/brianhie/scanorama
- **Paper**: https://www.nature.com/articles/s41592-019-0619-0
- **Tutorial**: https://scanpy-tutorials.readthedocs.io/
