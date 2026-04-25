---
name: anndatar
description: |
  Convert between .h5ad (AnnData) files and R single-cell data formats (Seurat, SingleCellExperiment) using anndataR.
  Use this skill whenever the user mentions: h5ad files, AnnData objects, converting between Python scanpy and R (Seurat/SingleCellExperiment),
  moving single-cell data between Python and R ecosystems, or needs to read/write .h5ad files from R.
  This skill provides pure R H5AD interface without Python dependencies.
---

# anndataR: H5AD to R Data Conversion

This skill enables seamless conversion between `.h5ad` files (AnnData format from Python/scanpy) and R single-cell objects (Seurat, SingleCellExperiment) using the anndataR package.

## Installation

Install anndataR using BiocManager:

```r
if (!requireNamespace("BiocManager", quietly = TRUE)) {
  install.packages("BiocManager")
}
BiocManager::install("anndataR")
```

## Core Conversion Functions

### Reading .h5ad Files

**Read as AnnData object (default - in-memory):**
```r
library(anndataR)
h5ad_path <- "path/to/your/file.h5ad"
adata <- read_h5ad(h5ad_path)
```

**Read as SingleCellExperiment:**
```r
sce <- read_h5ad(h5ad_path, as = "SingleCellExperiment")
```

**Read as Seurat:**
```r
obj <- read_h5ad(h5ad_path, as = "Seurat")
```

**Read as HDF5-backed AnnData (memory-efficient for large files):**
```r
adata <- read_h5ad(h5ad_path, as = "HDF5AnnData")
```

### Converting Between Formats

**AnnData → SingleCellExperiment:**
```r
sce <- adata$as_SingleCellExperiment()
```

**AnnData → Seurat:**
```r
obj <- adata$as_Seurat()
```

**SingleCellExperiment → AnnData:**
```r
adata <- as_AnnData(sce)
```

**Seurat → AnnData:**
```r
adata <- as_AnnData(obj)
```

### Writing .h5ad Files

**Write AnnData to disk:**
```r
tmpfile <- tempfile(fileext = ".h5ad")
adata$write_h5ad(tmpfile)
# Or: write_h5ad(adata, tmpfile)
```

**Write SingleCellExperiment to disk:**
```r
write_h5ad(sce, tmpfile)
```

**Write Seurat to disk:**
```r
write_h5ad(obj, tmpfile)
```

## Working with AnnData Objects

### Accessing Slots

```r
# Dimensions
dim(adata)
nrow(adata)
ncol(adata)

# Observation metadata (cells)
adata$obs        # Returns data.frame
adata$obs[1:5, ]  # First 5 cells

# Variable metadata (genes)
adata$var         # Returns data.frame
adata$var[1:5, ]  # First 5 genes

# Main expression matrix
adata$X

# Additional matrices (layers)
adata$layers$counts
adata$layers$dense_X

# Embeddings (obsm)
adata$obsm$X_pca
adata$obsm$X_umap

# Gene loadings (varm)
adata$varm$PCsstructured metadata

# Un (uns)
adata$uns$leiden
adata$uns$pca
```

### Subsetting AnnData Objects

anndataR supports standard R subsetting with lazy evaluation (returns views):

```r
# Subset by condition - cells
view1 <- adata[adata$obs$cell_type == "A", ]

# Subset by condition - genes
view2 <- adata[, adata$var$highly_variable]

# Combined subsetting
view3 <- adata[adata$obs$cell_type == "A", adata$var$highly_variable]

# Numeric indices
view4 <- adata[1:5, 1:3]

# Character names
rownames(adata) <- paste0("cell_", 1:nrow(adata))
colnames(adata) <- paste0("gene_", 1:ncol(adata))
view5 <- adata[c("cell_1", "cell_2"), c("gene_1", "gene_3")]

# Convert view to concrete object
concrete <- view3$as_InMemoryAnnData()
```

### Manually Creating AnnData Objects

```r
adata <- AnnData(
  X = matrix(rnorm(100), nrow = 10, ncol = 10),
  obs = data.frame(
    cell_type = factor(rep(c("A", "B"), each = 5)),
    score = runif(10)
  ),
  var = data.frame(
    gene_name = paste0("gene_", 1:10),
    highly_variable = rep(c(TRUE, FALSE), 5)
  )
)
```

## Common Workflows

### Python → R Pipeline

1. Process data in Python with scanpy
2. Save as .h5ad: `adata.write('data.h5ad')`
3. In R:
```r
library(anndataR)
library(Seurat)
adata <- read_h5ad("data.h5ad")
seurat_obj <- adata$as_Seurat()
# Continue with Seurat analysis
```

### R → Python Pipeline

1. Process data in R with Seurat
2. Convert and save:
```r
library(anndataR)
adata <- as_AnnData(seurat_obj)
adata$write_h5ad("data.h5ad")
```
3. In Python:
```python
import scanpy as sc
adata = sc.read_h5ad("data.h5ad")
# Continue with scanpy analysis
```

## Comparison with Other Packages

| Feature | anndataR | zellkonverter | anndata (CRAN) |
|---------|----------|---------------|----------------|
| Python dependency | No | Yes (reticulate) | Yes |
| Native H5AD reading | Yes | Via basilisk | No |
| Seurat conversion | Yes | Yes | Yes |
| SCE conversion | Yes | Yes | Yes |

anndataR is recommended when:
- You want to avoid Python dependencies
- You need a pure R solution
- You want simpler installation and setup

Use zellkonverter if you need bidirectional Python-R integration with more features.

## Troubleshooting

**Matrix column names warning:** When writing Seurat objects, matrix column names in obsm slots cannot be preserved. Store embeddings as data.frames instead of matrices if column names are important.

**Memory issues:** For large .h5ad files, use `read_h5ad(path, as = "HDF5AnnData")` for memory-efficient backed access instead of loading entirely into memory.

**Unsupported dtypes:** anndataR handles most common data types. If you encounter unsupported types, you may need to preprocess in Python first.
