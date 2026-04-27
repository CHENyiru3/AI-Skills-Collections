---
name: giotto
domain: compbio
description: Toolkit for spatial genomics. Comprehensive R package for spatial transcriptomics analysis with advanced visualization and statistics.
license: MIT license
metadata:
    skill-author: Eric Yiru
---

# Giotto: Spatial Genomics Toolkit

## Overview

Giotto is a comprehensive R toolkit for spatial genomics, supporting multiple platforms (Visium, Slide-seq, MERFISH, seqFISH, Xenium) with advanced analysis and visualization capabilities.

## When to Use This Skill

This skill should be used when:
- Analyzing spatial transcriptomics data in R
- Working with multiple spatial platforms
- Performing advanced spatial statistics
- Creating publication-quality visualizations
- Integrating spatial and single-cell data
- Working with large-scale spatial datasets

## Quick Start

### Installation

```r
# Install Giotto
install.packages("Giotto")

# Or from GitHub
devtools::install_github("rubd/GiottoSuite")
devtools::install_github("rubd/Giotto")

# Install spatial packages
install.packages("magick")  # For image handling
```

### Basic Setup

```r
library(Giotto)
library(ggplot2)
library(data.table)
```

## Creating Giotto Objects

### From Visium

```r
# Load Visium data
expr_path <- "raw_feature_bc_matrix/"
image_path <- "spatial/"
json_path <- "spatial/tissue_positions.json"

# Create Giotto object
visium.g <- createGiottoObject(
  raw_expr = expr_path,
  spatial_locs = NULL,
  image = image_path
)

# Or from Seurat
# Convert Seurat to Giotto
library(Seurat)
seurat.obj <- Load10X_Spatial("visium_data/")
visium.g <- seuratToGiotto(seurat.obj)
```

### From Custom Data

```r
# From expression matrix
expr_mat <- read.csv("expression.csv", row.names = 1)
loc_df <- read.csv("coordinates.csv")

# Create Giotto object
gobject <- createGiottoObject(
  raw_expr = expr_mat,
  spatial_locs = loc_df
)
```

## Spatial Analysis

### Spatial Network

```r
# Create spatial network
gobject <- createSpatialNetwork(
  gobject,
  method = "knn",
  k = 6
)

# View network
showGiottoNetwork(gobject)
```

### Spatial Statistics

```python
# Various spatial statistics available
# See Giotto documentation for full list
```

## Visualization

### Spatial Plots

```r
# Basic spatial plot
spatPlot(gobject, cell_color = "cell_type")

# With image background
spatPlot(
  gobject,
  cell_color = "cluster",
  image = TRUE,
  save_param = list(save_name = "spatial_plot")
)
```

## Integration

### With Single-Cell

```r
# Integrate with single-cell reference
# Use for cell type deconvolution
```

## Best Practices

1. **Check coordinates**: Ensure spatial coordinates match expression
2. **Multiple resolutions**: Test different neighborhood parameters
3. **Save results**: Giotto objects can be saved as RDS

## Additional Resources

- **GitHub**: https://github.com/rubd/Giotto
- **Documentation**: https://rubd.github.io/Giotto/
