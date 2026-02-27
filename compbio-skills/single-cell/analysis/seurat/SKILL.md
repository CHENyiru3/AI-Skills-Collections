---
name: seurat
description: R package for single-cell RNA-seq analysis. Use for QC, normalization, dimensionality reduction (PCA/UMAP/t-SNE), clustering, differential expression, and multi-modal integration. Best for R-based single-cell workflows. For Python use scanpy.
license: MIT license
metadata:
    skill-author: Eric Yiru
---

# Seurat: Single-Cell Analysis (R)

## Overview

Seurat is a powerful R package for single-cell RNA-seq analysis, providing a comprehensive toolkit for QC, normalization, dimensionality reduction, clustering, marker gene identification, and multi-modal integration. It is the most widely used R-based single-cell analysis framework.

## When to Use This Skill

This skill should be used when:
- Analyzing single-cell RNA-seq data in R
- Performing quality control on scRNA-seq datasets
- Creating UMAP, t-SNE, or PCA visualizations
- Identifying cell clusters and finding marker genes
- Annotating cell types based on gene expression
- Performing multi-modal integration (CITE-seq, ATAC-seq)
- Working with 10X Genomics data (Cell Ranger outputs)

## Quick Start

### Basic Setup

```r
# Install Seurat (if not already installed)
install.packages("Seurat")
install.packages("SeuratData")

# Load library
library(Seurat)
library(dplyr)
```

### Loading Data

```r
# From 10X Genomics (Cell Ranger output)
data_dir <- "path/to/sample/"
pbmc.data <- Read10X(data.dir = data_dir)

# Create Seurat object
pbmc <- CreateSeuratObject(counts = pbmc.data, project = "pbmc", min.cells = 3, min.features = 200)

# From CSV/TSV
data <- read.table("data.csv", sep = ",", header = TRUE, row.names = 1)
pbmc <- CreateSeuratObject(counts = data)

# From h5ad (AnnData)
# Install SeuratDisk package first
library(SeuratDisk)
pbmc <- LoadH5AD("data.h5ad")
```

### Understanding Seurat Object

The Seurat object is the core data structure:

```r
# Access different slots
pbmc@assays$RNA           # RNA assay data
pbmc@meta.data             # Cell metadata (data.frame)
pbmc@reductions           # Dimensionality reduction (PCA, UMAP, tSNE)
pbmc@graphs               # Neighbor graphs
pbmc@commands             # Command history

# Access cell and gene names
colnames(pbmc)            # Cell barcodes
rownames(pbmc)             # Gene names

# View metadata
head(pbmc@meta.data)
```

## Standard Analysis Workflow

### 1. Quality Control

```r
# Calculate mitochondrial percentage
pbmc[["percent.mt"]] <- PercentageFeatureSet(pbmc, pattern = "^MT-")

# Visualize QC metrics
VlnPlot(pbmc, features = c("nFeature_RNA", "nCount_RNA", "percent.mt"), ncol = 3)

# Filter cells
pbmc <- subset(pbmc, subset = nFeature_RNA > 200 & nFeature_RNA < 2500 & percent.mt < 5)
```

### 2. Normalization

```r
# Normalize data (default: LogNormalize)
pbmc <- NormalizeData(pbmc, normalization.method = "LogNormalize", scale.factor = 10000)

# Identify highly variable features
pbmc <- FindVariableFeatures(pbmc, selection.method = "vst", nfeatures = 2000)

# Identify top 10 variable features
top10 <- head(VariableFeatures(pbmc), 10)
plot1 <- VariableFeaturePlot(pbmc)
plot2 <- LabelPoints(plot = plot1, points = top10, repel = TRUE)
plot2
```

### 3. Scaling

```r
# Scale data (regress out unwanted variation)
all.genes <- rownames(pbmc)
pbmc <- ScaleData(pbmc, features = all.genes, vars.to.regress = c("percent.mt", "nCount_RNA"))
```

### 4. Dimensionality Reduction

```r
# Run PCA
pbmc <- RunPCA(pbmc, features = VariableFeatures(object = pbmc))

# Visualize PCA
DimPlot(pbmc, reduction = "pca")
DimHeatmap(pbmc, dims = 1:15, cells = 500, balanced = TRUE)

# Determine number of PCs to use
ElbowPlot(pbmc)

# Run UMAP
pbmc <- RunUMAP(pbmc, dims = 1:10)
DimPlot(pbmc, reduction = "umap")

# Alternative: t-SNE
pbmc <- RunTSNE(pbmc, dims = 1:10)
DimPlot(pbmc, reduction = "tsne")
```

### 5. Clustering

```r
# Find neighbors
pbmc <- FindNeighbors(pbmc, dims = 1:10)

# Find clusters (various resolutions)
pbmc <- FindClusters(pbmc, resolution = 0.5)

# View cluster IDs
head(Idents(pbmc), 5)

# Rename clusters
new.cluster.ids <- c("Naive CD4 T", "Memory CD4 T", "CD14+ Mono", "B", "CD8 T", "FCGR3A+ Mono", "NK", "DC", "Platelet")
names(new.cluster.ids) <- levels(pbmc)
pbmc <- RenameIdents(pbmc, new.cluster.ids)

# Visualize
DimPlot(pbmc, reduction = "umap", label = TRUE, pt.size = 0.5)
```

### 6. Marker Gene Identification

```r
# Find markers for each cluster
pbmc.markers <- FindAllMarkers(pbmc, only.pos = TRUE, min.pct = 0.25, thresh.use = 0.25)

# Get top markers per cluster
pbmc.markers %>% group_by(cluster) %>% top_n(n = 2, wt = avg_log2FC)

# Visualize top markers
VlnPlot(pbmc, features = c("MS4A1", "CD79A"))
FeaturePlot(pbmc, features = c("MS4A1", "GNLY", "CD3E", "CD14", "FCER1A", "FCGR3A", "LYZ", "PPBP", "CD8A"))

# Heatmap of top markers
DoHeatmap(pbmc, features = top10) + NoLegend()
```

## Multi-Modal Integration

### Working with CITE-seq Data

```r
# Load CITE-seq data
cbmc <- CreateSeuratObject(counts = cbmc.data$`Gene Expression`, assay = "RNA")
cbmc[["ADT"]] <- CreateAssayObject(counts = cbmc.data$`Antibody Capture`)

# Normalize ADT data
DefaultAssay(cbmc) <- "ADT"
cbmc <- NormalizeData(cbmc, normalization.method = "CLR", margin = 2)
cbmc <- ScaleData(cbmc)

# Switch back to RNA
DefaultAssay(cbmc) <- "RNA"
```

### Data Integration with Seurat v3+

```r
# Prepare objects for integration
immune.anchors <- FindIntegrationAnchors(object.list = list(pbmc1, pbmc2, pbmc3), dims = 1:20)

# Integrate
immune.combined <- IntegrateData(anchorset = immune.anchors, dims = 1:20)

# Run standard analysis on integrated data
DefaultAssay(immune.combined) <- "integrated"
immune.combined <- ScaleData(immune.combined)
immune.combined <- RunPCA(immune.combined, npcs = 30)
immune.combined <- RunUMAP(immune.combined, reduction = "pca", dims = 1:30)
immune.combined <- FindNeighbors(immune.combined, reduction = "pca", dims = 1:30)
immune.combined <- FindClusters(immune.combined, resolution = 0.5)
```

## Common Tasks

### Differential Expression

```r
# Find markers between two groups
cluster.markers <- FindMarkers(pbmc, ident.1 = "Cluster1", ident.2 = "Cluster2", min.pct = 0.25)

# Compare conditions within clusters
pbmc <- SetIdent(pbmc, value = paste(pbmc$seurat_clusters, pbmc$condition, sep = "_"))
markers <- FindMarkers(pbmc, ident.1 = "0_Treated", ident.2 = "0_Control")
```

### Gene Set Enrichment

```pbmc
# Add gene set scores
gene.list <- c("IL2", "IL7R", "CCR7", "CD27", "CD28", "CD3D", "CD3E")
pbmc <- AddModuleScore(pbmc, features = list(gene.list), name = "T_cell_signature")
```

### Save and Export

```r
# Save Seurat object
saveRDS(pbmc, file = "pbmc.rds")

# Export to h5ad (AnnData)
# Install SeuratDisk first
library(SeuratDisk)
SaveH5Seurat(pbmc, filename = "pbmc.h5Seurat")
Convert("pbmc.h5Seurat", dest = "h5ad")

# Export data
write.csv(pbmc@meta.data, "metadata.csv")
write.csv(GetAssayData(pbmc), "expression_matrix.csv")
```

## Key Parameters to Adjust

### Quality Control
- `min.cells`: Minimum cells per feature (typically 3)
- `min.features`: Minimum features per cell (typically 200)
- Mitochondrial threshold: typically 5-20%

### Feature Selection
- `nfeatures`: Number of variable features (typically 2000)

### Dimensionality Reduction
- `dims`: Number of dimensions (check ElbowPlot, typically 10-30.neighbors`: Number)
- `n of neighbors (default: 30)

### Clustering
- `resolution`: Clustering granularity (0.4-1.2, higher = more clusters)

## Best Practices

1. **Always save raw counts**: Keep raw data before normalization
2. **Check QC plots**: Adjust thresholds based on dataset quality
3. **Use multiple resolutions**: Try different clustering resolutions
4. **Validate markers**: Use multiple approaches to validate cell types
5. **Document parameters**: Record all analysis settings
6. **Save intermediate results**: Long workflows can fail

## Additional Resources

- **Official Seurat tutorials**: https://satijalab.org/seurat/articles/get_started.html
- **Seurat Data**: https://satijalab.org/seurat/articles/seurat_data.html
- **Multi-modal analysis**: https://satijalab.org/seurat/articles/multimodal_vignette.html
- **Integration**: https://satijalab.org/seurat/articles/integration_introduction.html

## Tips for Effective Analysis

1. Start with the built-in tutorials for learning
2. Use SeuratData for ready-to-use example datasets
3. Check the command history (`pbmc@commands`) to review analysis steps
4. Use `?function_name` for help on specific functions
5. Join the Seurat Discord community for help
