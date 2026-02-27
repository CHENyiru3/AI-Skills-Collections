# Computational Biology Skills Examples

## Example 1: Basic scRNA-seq Analysis with scanpy

```python
import scanpy as sc
import pandas as pd
import numpy as np

# Load data
adata = sc.read_10x_mtx('data/')

# QC
sc.pp.filter_cells(adata, min_genes=200)
sc.pp.filter_genes(adata, min_cells=3)

# Normalize
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)

# Feature selection
sc.pp.highly_variable_genes(adata, n_top_genes=2000)

# PCA and clustering
sc.pp.pca(adata, n_comps=50)
sc.pp.neighbors(adata, n_neighbors=15, n_pcs=50)
sc.tl.leiden(adata, resolution=0.5)
sc.tl.umap(adata)

# Visualization
sc.pl.umap(adata, color=['leiden', 'marker_gene'])
```

## Example 2: Batch Integration with Harmony

```r
library(Seurat)
library(harmony)

# Load and combine batches
pbmc1 <- ReadH5AD("batch1.h5ad")
pbmc2 <- ReadH5AD("batch2.h5ad")
pbmc <- merge(pbmc1, y = pbmc2, add.cell.ids = c("B1", "B2"))

# Process
pbmc <- NormalizeData(pbmc)
pbmc <- FindVariableFeatures(pbmc)
pbmc <- ScaleData(pbmc)
pbmc <- RunPCA(pbmc)

# Integration
pbmc <- RunHarmony(pbmc, group.by.vars = "batch")
pbmc <- RunUMAP(pbmc, reduction = "harmony", dims = 1:30)
pbmc <- FindNeighbors(pbmc, reduction = "harmony")
pbmc <- FindClusters(pbmc)

# Visualize
DimPlot(pbmc, reduction = "umap", group.by = "batch")
```

## Example 3: Spatial Transcriptomics with squidpy

```python
import squidpy as sq
import scanpy as sc

# Load Visium data
adata = sc.read_visium("visium_data/")

# Preprocess
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)
sc.pp.highly_variable_genes(adata, n_top_genes=2000)
sc.pp.pca(adata)
sc.pp.neighbors(adata)

# Clustering
sc.tl.leiden(adata, resolution=0.5)

# Spatial analysis
sq.gr.spatial_neighbors(adata)
sq.gr.centrality_scores(adata, cluster_key="leiden")

# Visualize
sq.pl.spatial_scatter(adata, color="leiden")
```

## Example 4: ATAC-seq Analysis with Signac

```r
library(Signac)
library(Seurat)

# Create object from fragments
counts <- Read10X_h5("filtered_peak_bc_matrix.h5")
fragfile <- "fragments.tsv.gz"

chrom_assay <- CreateChromatinAssay(
  counts = counts,
  fragments = fragfile
)

pbmc <- CreateSeuratObject(counts = chrom_assay, assay = "ATAC")

# Analysis
pbmc <- FindTopFeatures(pbmc, min.cells = 10)
pbmc <- RunTFIDF(pbmc)
pbmc <- FindSVD(pbmc)
pbmc <- FindNeighbors(pbmc, reduction = "lsi", dims = 2:30)
pbmc <- FindClusters(pbmc, resolution = 0.4)
pbmc <- RunUMAP(pbmc, reduction = "lsi", dims = 2:30)

DimPlot(pbmc, label = TRUE)
```

## Example 5: Differential Expression with PyDESeq2

```python
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats
import scanpy as sc

# Load data
adata = sc.read_h5ad("data.h5ad")

# Prepare for DESeq2
dds = DeseqDataSet(
    adata=adata,
    design_factors="condition",
    ref_level=["condition", "control"]
)

# Run DESeq2
dds.deseq2()

# Statistics
stat_res = DeseqStats(dds, contrast=["condition", "treatment", "control"])
stat_res.summary()

# Get results
results = stat_res.results_df
```

## Example 6: Automated Workflow with Snakemake

```python
# snakefile
configfile: "config.yaml"

rule all:
    input:
        "results/qc.html",
        "results/clustering.h5ad"

rule qc:
    input:
        "data/{sample}.h5ad"
    output:
        "results/{sample}_qc.h5ad"
    shell:
        "python scripts/qc.py {input} {output}"

rule cluster:
    input:
        "results/{sample}_qc.h5ad"
    output:
        "results/{sample}_clustered.h5ad"
    shell:
        "python scripts/cluster.py {input} {output}"
```

## Example 7: Nextflow Pipeline

```groovy
// main.nf
process QC {
    input:
    path sample

    output:
    path "qc_results"

    script:
    """
    python qc.py $sample
    """
}

workflow {
    samples = Channel.fromPath("data/*.h5ad")
    QC(samples)
}
```
