---
name: human-cell-atlas
description: Human Cell Atlas data portal. Use for accessing single-cell reference datasets, cell type markers, and standard atlases.
license: MIT license
metadata:
    skill-author: Eric Yiru
---

# Human Cell Atlas: Reference Atlas

## Overview

The Human Cell Atlas (HCA) is a global effort to create a comprehensive reference map of all human cells. The HCA data portal provides access to thousands of single-cell datasets spanning multiple tissues, cell types, and conditions.

## When to Use This Skill

This skill should be used when:
- Finding reference single-cell datasets
- Accessing cell type markers and gene expression
- Downloading curated atlases
- Comparing your data to references
- Finding data for specific tissues

## Quick Start

### Accessing Data

```python
# Using cellxgene-census (for HCA data)
import cellxgene_census

# Get census
census = cellxgene_census.open_soma()

# Query specific tissue
adata = cellxgene_census.get_anndata(
    census,
    organism="Homo sapiens",
    tissue="lung"
)
```

### Direct Download

1. Visit https://data.humancellatlas.org/
2. Browse projects and datasets
3. Download in desired format (h5ad, loom, csv)

## Data Portal

### Browsing Projects

- **Website**: https://data.humancellatlas.org/
- **Filter by**: Tissue, organism, disease, technology
- **Metadata**: Detailed sample information

### Available Data Types

- Single-cell RNA-seq
- Single-cell ATAC-seq
- Spatial transcriptomics
- Multi-omics

## Common Uses

### Reference Mapping

```python
# Map your data to HCA references
# Use Seurat or scanpy integration
```

### Marker Discovery

```python
# Find markers for cell types
# Query HCA for specific cell types
```

## Additional Resources

- **HCA Data Portal**: https://data.humancellatlas.org/
- **DCP**: https://data.humancellatlas.org/explore
- **CellxGene Census**: https://cellxgene-census.readthedocs.io/
