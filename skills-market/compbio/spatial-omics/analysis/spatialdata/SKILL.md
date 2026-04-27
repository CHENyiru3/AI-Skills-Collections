---
name: spatialdata
domain: compbio
description: Unified framework for spatial omics data in Python. Use for integrating multiple spatial modalities and formats. Part of the scverse ecosystem.
license: MIT license
metadata:
    skill-author: Eric Yiru
---

# SpatialData: Spatial Omics Framework

## Overview

SpatialData is a Python framework that provides a unified representation for various spatial omics data types. It enables interoperability between different spatial platforms and analysis tools within the scverse ecosystem.

## When to Use This Skill

This skill should be used when:
- Working with multiple spatial data types
- Need to integrate different spatial platforms
- Using the scverse ecosystem for analysis
- Creating pipelines across spatial modalities
- Requiring standardized spatial data formats

## Quick Start

### Installation

```bash
pip install spatialdata

# With all dependencies
pip install spatialdata[all]
```

### Basic Usage

```python
from spatialdata import SpatialData
import scanpy as sc

# Load data
sdata = SpatialData.read("data.zarr")

# Access different modalities
sdata.table  # Obs table
sdata.shapes  # Shapes (spots, polygons)
sdata.images  # Images
```

## Data Types

### Supported Platforms

- 10X Visium
- 10X Xenium
- Vizgen MERFISH
- NanoString CosMX
- Akoya CODEX
- ImcData

## Integration

### With Scanpy

```python
# Convert to AnnData for scanpy analysis
adata = sdata.table.to_adata()

# Run scanpy analysis
sc.pp.pca(adata)
sc.pp.neighbors(adata)
sc.tl.umap(adata)

# Add back to SpatialData
sdata.table = adata
```

### With Squidpy

```python
import squidpy as sq

# Use squidpy functions with SpatialData
```

## Best Practices

1. **Use Zarr format**: Best for large spatial data
2. **Check coordinate systems**: Ensure consistent transformations
3. **Document metadata**: Record acquisition parameters

## Additional Resources

- **Documentation**: https://spatialdata.scverse.org/
- **GitHub**: https://github.com/scverse/spatialdata
