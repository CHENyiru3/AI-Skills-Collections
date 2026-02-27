---
name: vitessce
description: Visual integration tool for exploration of spatial single-cell data. Use for creating interactive visualizations and dashboards for multi-modal and spatial omics data.
license: MIT license
metadata:
    skill-author: Eric Yiru
---

# Vitessce: Visual Integration Tool

## Overview

Vitessce is a web-based visualization framework for exploring multi-modal and spatial single-cell data. It enables the creation of interactive dashboards combining gene expression, protein, spatial, and image data.

## When to Use This Skill

This skill should be used when:
- Creating interactive dashboards for spatial omics
- Visualizing multi-modal single-cell data
- Building data portals for single-cell data
- Sharing visualizations with collaborators
- Combining different data types in one view

## Quick Start

### Installation

```bash
# Install Vitessce Python package
pip install vitessce

# Create a Vitessce config
vitessce --init
```

### Creating a Dashboard

```python
from vitessce import (
    VitessceConfig,
    ViewConf,
    FileType,
    DataType,
)

# Create configuration
vc = VitessceConfig()

# Add dataset
dataset = vc.add_dataset("My Dataset")

# Add files
dataset.add_file(
    url="https://example.com/expression.h5ad",
    file_type=FileType.H5AD,
    data_type=DataType.OBS_COUNT_MATRIX,
)

# Add view
scatterplot = vc.add_view(dataset, ViewConf.SCATTERPLOT, x=0, y=0, w=6, h=8)

# Export
vc.export_plugins()
vc.export("config.json")
```

## Configuration

### Views

- **Scatterplot**: 2D embeddings (UMAP, t-SNE)
- **Spatial**: Spatial gene expression
- **Heatmap**: Gene expression matrices
- **CellSets**: Cell type annotations
- **Genes**: Gene lists

### Data Types

- Expression matrices (H5AD, Zarr)
- Cell segmentations
- Image stores (OME-TIFF, Zarr)

## Best Practices

1. **Prepare data in Python/R**: Use scanpy/Seurat first
2. **Use appropriate formats**: H5AD for expression, OME-TIFF for images
3. **Test locally**: Verify before deployment

## Additional Resources

- **Documentation**: https://vitessce.io/
- **GitHub**: https://github.com/vitessce/vitessce
