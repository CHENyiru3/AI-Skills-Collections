---
name: harmony
domain: compbio
description: Fast and accurate integration of single-cell data. Use for batch correction and data integration. Works with Seurat objects in R. For Python use scanorama or bbknn.
license: MIT license
metadata:
    skill-author: Eric Yiru
---

# Harmony: Single-Cell Data Integration

## Overview

Harmony is a fast and accurate method for integrating single-cell data from multiple batches, conditions, or modalities. It uses a soft clustering approach and iterative alignment to remove batch effects while preserving biological variation.

## When to Use This Skill

This skill should be used when:
- Integrating single-cell datasets from multiple batches
- Removing technical variation while preserving biology
- Combining data from different sequencing technologies
- Integrating datasets with different cell type compositions
- Working with large datasets (scales well to millions of cells)
- Using R-based workflows (for Python, see scanorama or bbknn)

## Quick Start

### Installation

```r
# Install from CRAN
install.packages("harmony")

# Or from GitHub
devtools::install_github("immunogenomics/harmony")
```

### Basic Integration in Seurat

```r
library(Seurat)
library(harmony)

# Load and preprocess each dataset
pbmc1 <- ReadH5AD("dataset1.h5ad")
pbmc2 <- ReadH5AD("dataset2.h5ad")

# Create combined object
pbmc.combined <- merge(pbmc1, y = pbmc2, add.cell.ids = c("batch1", "batch2"))

# Run standard Seurat pipeline
pbmc.combined <- NormalizeData(pbmc.combined)
pbmc.combined <- FindVariableFeatures(pbmc.combined)
pbmc.combined <- ScaleData(pbmc.combined)
pbmc.combined <- RunPCA(pbmc.combined, npcs = 30)

# Run Harmony integration
pbmc.combined <- RunHarmony(pbmc.combined, group.by.vars = "batch", reduction = "pca")

# Use Harmony reduction for clustering
pbmc.combined <- RunUMAP(pbmc.combined, reduction = "harmony", dims = 1:30)
pbmc.combined <- FindNeighbors(pbmc.combined, reduction = "harmony", dims = 1:30)
pbmc.combined <- FindClusters(pbmc.combined, resolution = 0.5)

# Visualize
DimPlot(pbmc.combined, reduction = "umap", group.by = "batch")
DimPlot(pbmc.combined, reduction = "umap", group.by = "seurat_clusters")
```

## Parameters

### RunHarmony Parameters

```r
pbmc <- RunHarmony(
  object,                    # Seurat object
  group.by.vars,             # Variable(s) to integrate (batch)
  reduction = "pca",         # Reduction to use
  dims.use = NULL,          # Dimensions to use
  theta = 2,                # Clustering diversity parameter (higher = more diverse)
  lambda = 1,               # Regularization parameter
  sigma = 0.1,              # Smoothness penalty
  nclust = NULL,            # Number of clusters (NULL = auto)
  tau = 0,                  # Protection against over-clustering
  block.size = 0.05,        # Fraction of cells to update per iteration
  max.iter.harmony = 10,    # Maximum Harmony iterations
  max.iter.cluster = 20,    # Maximum clustering iterations
  epsilon.harmony = 1e-5,    # Convergence threshold
  epsilon.cluster = 1e-8,   # Cluster convergence threshold
  plot_convergence = FALSE   # Plot convergence
)
```

### Parameter Tuning

- **theta**: Controls diversity of integration. Higher values allow more diverse clusters. Try 0 (no diversity) to 2 (default).
- **lambda**: Regularization strength. Higher values = more aggressive integration.
- **sigma**: Smoothing parameter. Controls how much neighbors influence each other.

## Integration Strategies

### Basic Batch Correction

```r
# Simple batch correction
pbmc <- RunHarmony(pbmc, group.by.vars = "batch")

# Compare before/after
p1 <- DimPlot(pbmc, reduction = "pca", group.by = "batch")
p2 <- DimPlot(pbmc, reduction = "harmony", group.by = "batch")
p1 + p2
```

### Multiple Variables

```r
# Integrate by multiple variables
pbmc <- RunHarmony(pbmc, group.by.vars = c("batch", "technology", "donor"))
```

### Reference-Based Integration

```r
# Use reference-based integration for large datasets
pbmc <- RunHarmony(
  pbmc,
  group.by.vars = "batch",
  reference = "batch1"  # Use batch1 as reference
)
```

### Conditional Integration

```r
# Integrate within conditions
pbmc$group_batch <- paste(pbmc$condition, pbmc$batch, sep = "_")
pbmc <- RunHarmony(pbmc, group.by.vars = "group_batch")
```

## Post-Integration Analysis

### Marker Gene Finding

```r
# After integration, find markers
markers <- FindAllMarkers(pbmc, only.pos = TRUE)

# Check if markers are consistent across batches
# (they should have similar expression across batches)
VlnPlot(pbmc, features = "marker_gene", group.by = "seurat_clusters", split.by = "batch")
```

### Preserving Biological Variation

```r
# Check if biological variation is preserved
# Plot known cell type markers
FeaturePlot(pbmc, features = c("CD3D", "MS4A1", "CD14"), reduction = "harmony")

# Compare cell type composition across batches
table(pbmc$cell_type, pbmc$batch)
```

## Advanced Usage

### Using Harmony in Python (rpy2)

```python
import scanpy as sc
import rpy2.robjects as ro

# Run Harmony through R interface
from rpy2.robjects import pandas2ri
pandas2ri.activate()

# Convert to R and run Harmony
# (requires rpy2 and Harmony installed in R)
```

### Integration with Other Methods

```r
# Combine Harmony with Seurat v3 integration
pbmc <- RunHarmony(pbmc, group.by.vars = "batch")
pbmc <- FindNeighbors(pbmc, reduction = "harmony")
pbmc <- FindClusters(pbmc)

# Or use Seurat v5 integration
pbmc <- IntegrateLayers(
  object = pbmc,
  method = HarmonyIntegration,
  group.by = "batch"
)
```

## Troubleshooting

### Batch Effect Not Removed

- Increase theta
- Increase max.iter.harmony
- Check if batch variable is correct
- Try different PCA dimensions

### Biological Variation Lost

- Decrease lambda
- Reduce integration iterations
- Try reference-based integration
- Consider using different method (Seurat v3 integration)

### Over-Correction

- Decrease lambda
- Increase theta
- Reduce max.iter.harmony
- Check cell type composition

## Comparison with Other Methods

| Method | Language | Strengths |
|--------|----------|-----------|
| Harmony | R | Fast, scalable, preserves biology |
| Seurat v3/v5 | R | Multi-modal, very accurate |
| Scanorama | Python | Python integration |
| BBKNN | Python | Fast, simple |
| Liger | R | iNMF, multi-dataset |

## Best Practices

1. **Quality control first**: Remove low-quality cells before integration
2. **Use consistent preprocessing**: Same normalization, variable features
3. **Test parameters**: Try different theta values
4. **Validate results**: Check known markers across batches
5. **Compare with unintegrated**: Always compare with original data

## Additional Resources

- **Harmony paper**: https://www.nature.com/articles/s41592-019-0619-0
- **GitHub**: https://github.com/immunogenomics/harmony
- **Documentation**: https://harmony.readthedocs.io/
