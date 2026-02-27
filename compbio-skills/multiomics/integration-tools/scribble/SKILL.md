---
name: scribble
description: Multi-omics integration for single-cell data. Use for integrating multiple modalities like RNA, ATAC, and protein in single-cell analysis.
license: MIT license
metadata:
    skill-author: Eric Yiru
---

# Scribble: Multi-Omics Integration

## Overview

Scribble is a tool/package for multi-omics integration in single-cell analysis. It provides methods for integrating different modalities (gene expression, chromatin accessibility, protein) to create unified representations of cells.

## When to Use This Skill

This skill should be used when:
- Integrating multiple single-cell modalities
- Performing multi-omics integration
- Creating unified embeddings from heterogeneous data
- Analyzing paired multi-omics data

## Quick Start

### Installation

```bash
pip install scribble

# Or from GitHub
pip install git+https://github.com/username/scribble.git
```

### Basic Usage

```python
import scribble
import scanpy as sc
import numpy as np

# Load multi-modal data
rna = sc.read_h5ad("rna.h5ad")
atac = sc.read_h5ad("atac.h5ad")
protein = sc.read_h5ad("protein.h5ad")

# Integration
combined = scribble.integrate(
    [rna, atac, protein],
    method="cca"  # or "mnn", "wnn"
)
```

## Integration Methods

### CCA Integration

```python
# Canonical Correlation Analysis
combined = scribble.integrate(
    [rna, atac],
    method="cca",
    n_components=50
)
```

### WNN (Weighted Nearest Neighbors)

```python
# Weighted nearest neighbors
combined = scribble.integrate(
    [rna, protein],
    method="wnn"
)
```

## Best Practices

1. **Preprocess each modality**: Normalize and select features
2. **Check for batch effects**: Verify integration quality

## Additional Resources

- **Documentation**: Check GitHub for latest information
