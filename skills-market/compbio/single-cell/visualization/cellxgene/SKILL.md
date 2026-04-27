---
name: cellxgene
domain: compbio
description: Interactive web-based viewer for single-cell RNA-seq data. Use for exploring datasets, creating visualizations, and sharing results. For programmatic access use cellxgene-census.
license: MIT license
metadata:
    skill-author: Eric Yiru
---

# cellxgene: Interactive Single-Cell Data Explorer

## Overview

cellxgene is an interactive web-based tool for exploring single-cell RNA-seq datasets. It provides a fast, intuitive interface for visualizing cell populations, gene expression patterns, and metadata without requiring programming knowledge.

## When to Use This Skill

This skill should be used when:
- Exploring single-cell datasets interactively
- Creating shareable visualizations for collaborators
- Checking gene expression across cell types
- Filtering and subsetting data visually
- Creating annotations and cell labels
- Preparing figures for publications
- Sharing datasets with collaborators or publicly

## Quick Start

### Installation

```bash
# Install via pip
pip install cellxgene

# Or using conda
conda install -c conda-forge cellxgene
```

### Launch cellxgene

```bash
# Launch with a h5ad file
cellxgene launch data.h5ad

# Launch with specific host and port
cellxgene launch data.h5ad --port 5000 --host 0.0.0.0

# Launch with annotations
cellxgene launch data.h5ad --annotations ./annotations.tsv
```

### Opening Data

1. Navigate to `http://localhost:5000` (or your specified port)
2. The interface loads automatically with the dataset

## Interface Overview

### Main View Components

- **Left sidebar**: Gene expression search, metadata filters
- **Center**: Scatter plot (UMAP, t-SNE, PCA)
- **Bottom**: Gene expression violin/dot plots
- **Right panel**: Categorical color by options

### Navigation Controls

- **Scroll**: Zoom in/out
- **Click + drag**: Pan
- **Shift + click**: Select points
- **Double-click**: Reset view

## Common Tasks

### Searching Genes

1. Type gene name in the search box (top left)
2. Gene expression automatically visualizes on the plot
3. Use the "color by" dropdown to switch visualization

### Filtering Data

```python
# Create a filtered dataset for cellxgene
import scanpy as sc

adata = sc.read_h5ad("data.h5ad")

# Filter to specific cell types
adata_filtered = adata[adata.obs['cell_type'].isin(['T cells', 'B cells'])]

# Save for cellxgene
adata_filtered.write_h5ad("filtered_data.h5ad")
```

### Adding Custom Metadata

```python
# Add custom annotations
import pandas as pd

# Create annotations file
annotations = pd.DataFrame({
    'cell_id': adata.obs_names,
    'custom_label': your_custom_labels
})
annotations.to_csv('annotations.tsv', sep='\t', index=False)
```

### Creating Subsets

In the cellxgene interface:
1. Use the category filter in the left sidebar
2. Select specific categories to include
3. Click "Create subset from selected"
4. Save subset via File > Save current dataset

## Embedding cellxgene

### In Jupyter Notebooks

```python
# Using ipywidgets
import cellxgene
from cellxgene import launch

# View in notebook
launch.run_server("data.h5ad", port=8888)
```

### As Part of a Web App

```python
# Using Flask
from flask import Flask
import cellxgene

app = Flask(__name__)

@app.route('/')
def index():
    return cellxgene.launch.build_index()

if __name__ == '__main__':
    app.run()
```

## Configuration

### Dataset Configuration File

Create `dataset-metadata.yaml` for custom configuration:

```yaml
about:
  title: "My Single-Cell Dataset"
  description: "Description of the dataset"
  author: "Your Name"
  url: "https://example.com"

layout:
  # Custom embeddings to include
  embeddings:
    - name: "UMAP"
      type: "umap"
    - name: "t-SNE"
      type: "tsne"
```

### Launch Options

```bash
# With custom configuration
cellxgene launch data.h5ad --config dataset-metadata.yaml

# With embeddings file
cellxgene launch data.h5ad --embeddings embeddings.tsv

# Disable diffexp (for large datasets)
cellxgene launch data.h5api --diffexp-enabled=false
```

## Best Practices

1. **Pre-process data in Python/R**: Use scanpy/Seurat for analysis, cellxgene for visualization
2. **Include metadata**: Add cell type annotations, batch info, condition labels
3. **Check file size**: Large datasets (>100k cells) may be slow
4. **Prepare embeddings**: Include UMAP/t-SNE coordinates in the h5ad file

## Limitations

- Not suitable for very large datasets (>500k cells)
- Limited to gene expression (for multi-modal, consider Vitessce)
- No advanced statistical analysis
- No Python API for customization

## Alternative: cellxgene-census

For programmatic access to cellxgene datasets, use the `cellxgene-census` skill which provides a Python API to access the CellxGene census data.

## Additional Resources

- **Official documentation**: https://cellxgene.readthedocs.io/
- **Example datasets**: https://cellxgene-example-data.readthedocs.io/
- **GitHub repository**: https://github.com/chanzuckerberg/cellxgene
