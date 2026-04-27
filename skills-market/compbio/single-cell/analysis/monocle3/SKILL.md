---
name: monocle3
domain: compbio
description: R package for single-cell trajectory analysis. Use for reconstructing pseudotime trajectories, identifying cell differentiation paths, analyzing branch points, and ordering cells along developmental processes. Best for understanding dynamic biological processes from scRNA-seq data.
license: MIT license
metadata:
    skill-author: Eric Yiru
---

# Monocle 3: Single-Cell Trajectory Analysis (R)

## Overview

Monocle 3 is an algorithm for reconstructing single-cell trajectories and analyzing cell fate decisions. It learns the sequence of gene expression changes cells undergo during dynamic biological processes (differentiation, response to stimuli, disease progression) and places each cell at its proper position along this trajectory.

**Key Concepts:**
- **Pseudotime**: A measure of how much progress a cell has made through a biological process (distance from trajectory start)
- **Trajectory graph**: A principal graph that represents the overall path cells follow
- **Branches**: Points where cells can diverge into different fates
- **Partitions**: Separate trajectory components for cells with distinct starting states

## When to Use This Skill

Use this skill when:
- Analyzing cell differentiation trajectories
- Studying dynamic biological processes (development, disease progression, treatment response)
- Identifying gene expression changes over pseudotime
- Analyzing branch points and cell fate decisions
- Working with time-series single-cell data
- You need to order cells along a continuum rather than discrete clusters

## Installation

```r
# Install Monocle3 from Bioconductor
if (!require("BiocManager")) install.packages("BiocManager")
BiocManager::install("monocle3")

# Load library
library(monocle3)
library(ggplot2)
library(dplyr)
```

## Basic Workflow

### 1. Create CellDataSet Object

Monocle3 uses the CellDataSet (CDS) object to store expression data:

```r
# Method 1: From expression matrix + metadata
# expression_matrix: genes x cells matrix
# cell_metadata: data.frame with cell information
# gene_metadata: data.frame with gene information (must include gene_id column)

cds <- new_cell_data_set(expression_matrix,
                         cell_metadata = cell_metadata,
                         gene_metadata = gene_metadata)

# Method 2: From Seurat object
cds <- SeuratWrappers::as.cell_data_set(seurat_object)

# Method 3: From 10X data
expression_matrix <- Read10X("path/to/filtered_feature_bc_matrix/")
cds <- new_cell_data_set(expression_matrix)
```

### 2. Preprocess the Data

```r
# Determine number of dimensions
cds <- preprocess_cds(cds, num_dim = 50)

# Align batches (adjust for batch effects)
# Option A: Align by batch categories
cds <- align_cds(cds, alignment_group = "batch")

# Option B: Align by batch + continuous covariates (e.g., mitochondrial reads)
cds <- align_cds(cds,
                 alignment_group = "batch",
                 residual_model_formula_str = "~ percent.mt")

# Option C: Full residual model
cds <- align_cds(cds,
                 alignment_group = "batch",
                 residual_model_formula_str = "~ bg.300.loading + bg.400.loading + bg.500.1.loading")
```

### 3. Reduce Dimensionality

```r
# UMAP (recommended for trajectory analysis)
cds <- reduce_dimension(cds)

# Alternative: t-SNE
cds <- reduce_dimension(cds, reduction_method = "tSNE")

# 3D reduction
cds <- reduce_dimension(cds, max_components = 3)
```

### 4. Cluster Cells

Clustering identifies groups that will become separate trajectories:

```r
cds <- cluster_cells(cds)

# View partitions (separate trajectory components)
partitions(cds)

# Color by partition
plot_cells(cds, color_cells_by = "partition")
```

### 5. Learn the Trajectory Graph

```r
cds <- learn_graph(cds)

# Visualize the graph
plot_cells(cds,
           color_cells_by = "cell.type",
           label_groups_by_cluster = FALSE,
           label_leaves = FALSE,
           label_branch_points = FALSE)
```

### 6. Order Cells in Pseudotime

```r
# Interactive root selection (opens GUI)
cds <- order_cells(cds)

# Programmatic root selection - find earliest node
get_earliest_principal_node <- function(cds, time_bin = "early"){
  cell_ids <- which(colData(cds)[, "time_point"] == time_bin)

  closest_vertex <-
    cds@principal_graph_aux[["UMAP"]]$pr_graph_cell_proj_closest_vertex
  closest_vertex <- as.matrix(closest_vertex[colnames(cds), ])
  root_pr_nodes <-
    igraph::V(principal_graph(cds)[["UMAP"]])$name[as.numeric(names
    (which.max(table(closest_vertex[cell_ids,]))))]

  root_pr_nodes
}

# Order using programmatic root
cds <- order_cells(cds, root_pr_nodes = get_earliest_principal_node(cds))

# Order with multiple roots (one per partition)
cds <- order_cells(cds, root_pr_nodes = c("Y_1", "Y_2"))
```

### 7. Visualize Results

```r
# Color by pseudotime
plot_cells(cds,
           color_cells_by = "pseudotime",
           label_cell_groups = FALSE,
           label_leaves = FALSE,
           label_branch_points = FALSE)

# Color by cell type
plot_cells(cds,
           color_cells_by = "cell.type",
           label_groups_by_cluster = FALSE)

# Visualize gene expression along trajectory
plot_cells(cds,
           genes = c("GeneA", "GeneB", "GeneC"),
           label_cell_groups = FALSE,
           show_trajectory_graph = FALSE)
```

## Advanced Analysis

### Finding Genes that Change with Pseudotime

```r
# Find genes that vary with pseudotime
cds <- find_genes_that_differ_with_pseudotime(cds)

# View top genes
head(arrange(cds@metadata$gene_f_stat_info, qval), 20)

# Plot top genes
plot_genes_in_pseudotime(cds,
                         color_cells_by = "cell.type",
                         min_expr = 0.5)
```

### Analyzing Branches

```r
# Identify genes that change at branch points
BranchP <- BEAM(cds, branch_point = 1, branch_states = NULL)
BranchP <- BranchP[order(BranchP$qval), ]

# Plot genes in branch
plot_genes_branched(cds,
                    gene = "GeneA",
                    color_cells_by = "cell.type",
                    branch_point = 1)
```

### Subset by Branch

```r
# Interactive branch selection
cds_sub <- choose_graph_segments(cds)

# Programmatic: subset cells in a specific trajectory segment
# Get cell IDs from a particular path
```

### 3D Trajectory Visualization

```r
# Create 3D trajectory
cds_3d <- reduce_dimension(cds, max_components = 3)
cds_3d <- cluster_cells(cds_3d)
cds_3d <- learn_graph(cds_3d)
cds_3d <- order_cells(cds_3d, root_pr_nodes = get_earliest_principal_node(cds))

# Plot 3D
cds_3d_plot_obj <- plot_cells_3d(cds_3d, color_cells_by = "partition")

# Interactive 3D in RStudio
library(rgl)
plot_cells_3d(cds_3d, color_cells_by = "cell.type")
```

### Working with Partitions

```r
# Each partition becomes a separate trajectory
# Useful when you have multiple distinct cell populations

# Order each partition separately
for (part in partitions(cds)) {
  part_cells <- which(partitions(cds) == part)
  # Order cells in this partition
}

# Check which cells have finite pseudotime
pseudotime(cds)
sum(is.infinite(pseudotime(cds)))
```

## Differential Expression Analysis

Monocle 3 provides two main approaches for differential expression analysis:

1. **Regression analysis** (`fit_models()`): Evaluate whether genes depend on variables like time, treatment, clusters
2. **Graph-autocorrelation analysis** (`graph_test()`): Find genes that vary over trajectories or between clusters

### 1. Regression Analysis with fit_models()

Fit generalized linear models to test gene expression dependence on experimental variables:

```r
# Subset to genes of interest
ciliated_genes <- c("che-1", "hlh-17", "nhr-6", "dmd-6", "ceh-36", "ham-1")
cds_subset <- cds[rowData(cds)$gene_short_name %in% ciliated_genes,]

# Fit models - test time-dependent expression
gene_fits <- fit_models(cds_subset, model_formula_str = "~embryo.time")

# Extract coefficient table
fit_coefs <- coefficient_table(gene_fits)

# Filter for time-dependent genes
emb_time_terms <- fit_coefs %>% filter(term == "embryo.time")

# Get significant time-varying genes
sig_genes <- emb_time_terms %>%
  filter(q_value < 0.05) %>%
  select(gene_short_name, term, q_value, estimate)
```

**Model formula examples:**
```r
# Test effect of time
"~embryo.time"

# Control for batch
"~embryo.time + batch"

# Test cluster differences
"~cluster"

# Test partition differences
"~partition"

# Multiple variables
"~treatment + batch + percent.mt"
```

### 2. Evaluate Model Fits

```r
# Evaluate model quality
model_eval <- evaluate_fits(gene_fits)

# Compare models (full vs reduced)
time_batch_models <- fit_models(cds_subset,
                               model_formula_str = "~embryo.time + batch",
                               expression_family = "negbinomial")
time_models <- fit_models(cds_subset,
                          model_formula_str = "~embryo.time",
                          expression_family = "negbinomial")

# Likelihood ratio test
compare_results <- compare_models(time_batch_models, time_models) %>%
  select(gene_short_name, q_value)
```

### 3. Choosing Expression Family

| Expression Family | Distribution | Speed | Notes |
|-------------------|--------------|-------|-------|
| quasipoisson | Quasi-poisson | ++ | Default, recommended |
| negbinomial | Negative binomial | + | More accurate for small datasets |
| poisson | Poisson | +++ | Not recommended |
| binomial | Binomial | ++ | For ATAC-seq |

### 4. Graph-Autocorrelation Analysis

Use Moran's I statistic to find genes that vary spatially in UMAP or along trajectories:

```r
# For cluster-based analysis
pr_graph_test_res <- graph_test(neurons_cds, neighbor_graph = "knn", cores = 8)
pr_deg_ids <- row.names(subset(pr_graph_test_res, q_value < 0.05))

# For trajectory-based analysis (principal graph)
pr_test_res <- graph_test(cds, neighbor_graph = "principal_graph", cores = 4)
pr_deg_ids <- row.names(subset(pr_test_res, q_value < 0.05))

# View top genes by Moran's I (effect size)
head(pr_test_res[order(-pr_test_res$morans_I), ], 20)
```

**Moran's I interpretation:**
- +1: Perfect positive autocorrelation (nearby cells have similar expression)
- 0: No spatial pattern
- -1: Negative autocorrelation (rare)

### 5. Finding Co-Regulated Gene Modules

Group genes into modules based on similar expression patterns:

```r
# Find gene modules
gene_module_df <- find_gene_modules(cds[pr_deg_ids,], resolution = 1e-2)

# View module assignments
head(gene_module_df)

# Aggregate expression by cell groups
cell_group_df <- tibble::tibble(cell = row.names(colData(cds)),
                                cell_group = colData(cds)$cell.type)
agg_mat <- aggregate_gene_expression(cds, gene_module_df, cell_group_df)

# Heatmap visualization
pheatmap::pheatmap(agg_mat,
                   cluster_rows = TRUE,
                   cluster_cols = TRUE,
                   scale = "column",
                   clustering_method = "ward.D2")

# Plot specific modules in UMAP
plot_cells(cds,
           genes = gene_module_df %>% filter(module %in% c(8, 28, 33)),
           group_cells_by = "partition",
           color_cells_by = "partition",
           show_trajectory_graph = FALSE)
```

### 6. Genes that Change with Pseudotime

```r
# Find pseudotime-dependent genes
cds <- find_genes_that_differ_with_pseudotime(cds)

# View results
head(arrange(cds@metadata$gene_f_stat_info, qval), 20)

# Plot genes along pseudotime
plot_genes_in_pseudotime(AFD_lineage_cds,
                         color_cells_by = "embryo.time.bin",
                         min_expr = 0.5)

# For specific lineage paths
AFD_genes <- c("gcy-8", "dac-1", "oig-8")
AFD_lineage_cds <- cds[rowData(cds)$gene_short_name %in% AFD_genes,
                       colData(cds)$cell.type %in% c("AFD")]
AFD_lineage_cds <- order_cells(AFD_lineage_cds)
plot_genes_in_pseudotime(AFD_lineage_cds,
                         color_cells_by = "embryo.time.bin",
                         min_expr = 0.5)
```

### 7. Analyzing Branch Points

Identify genes regulated around trajectory branch points:

```r
# Interactive branch selection
cds_subset <- choose_cells(cds)

# Test for genes varying at branch points
subset_pr_test_res <- graph_test(cds_subset,
                                  neighbor_graph = "principal_graph",
                                  cores = 4)
pr_deg_ids <- row.names(subset(subset_pr_test_res, q_value < 0.05))

# Find modules in branch region
gene_module_df <- find_gene_modules(cds_subset[pr_deg_ids,], resolution = 0.001)

# Organize by similarity over trajectory
agg_mat <- aggregate_gene_expression(cds_subset, gene_module_df)
module_dendro <- hclust(dist(agg_mat))
gene_module_df$module <- factor(gene_module_df$module,
                               levels = row.names(agg_mat)[module_dendro$order])

# Plot branch-specific modules
plot_cells(cds_subset,
           genes = gene_module_df,
           label_cell_groups = FALSE,
           show_trajectory_graph = FALSE)
```

### 8. Visualization Functions

```r
# Violin plots
plot_genes_violin(cds_subset,
                  group_cells_by = "embryo.time.bin",
                  ncol = 2) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

# Hybrid plot (dots + histogram)
plot_genes_hybrid(cds_subset,
                  group_cells_by = "embryo.time.bin",
                  ncol = 2) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

# Plot genes in pseudotime
plot_genes_in_pseudotime(cds_subset,
                         color_cells_by = "cell.type",
                         min_expr = 0.5)

# Plot branched genes
plot_genes_branched(cds,
                    gene = "GeneA",
                    color_cells_by = "cell.type",
                    branch_point = 1)
```

## Example: Complete Analysis

```r
# Load example data (C. elegans neurons)
expression_matrix <- readRDS(url("https://depts.washington.edu:/trapnell-lab/software/monocle3/celegans/data/packer_embryo_expression.rds"))
cell_metadata <- readRDS(url("https://depts.washington.edu:/trapnell-lab/software/monocle3/celegans/data/packer_embryo_colData.rds"))
gene_annotation <- readRDS(url("https://depts.washington.edu:/trapnell-lab/software/monocle3/celegans/data/packer_embryo_rowData.rds"))

# Create CDS
cds <- new_cell_data_set(expression_matrix,
                         cell_metadata = cell_metadata,
                         gene_metadata = gene_annotation)

# Preprocess
cds <- preprocess_cds(cds, num_dim = 50)

# Batch correction (if needed)
cds <- align_cds(cds, alignment_group = "batch")

# Reduce dimensions
cds <- reduce_dimension(cds)

# Cluster to find partitions
cds <- cluster_cells(cds)

# Learn trajectory
cds <- learn_graph(cds)

# Order cells
cds <- order_cells(cds)

# Visualize
plot_cells(cds,
           color_cells_by = "cell.type",
           label_groups_by_cluster = FALSE)

plot_cells(cds,
           color_cells_by = "pseudotime",
           label_cell_groups = FALSE)

# Find genes varying with pseudotime
cds <- find_genes_that_differ_with_pseudotime(cds)
```

## Key Parameters

### preprocess_cds()
- `num_dim`: Number of PCs (typically 30-100, check elbow plot)
- `reduction_method`: "PCA" (default) or "LSI"

### align_cds()
- `alignment_group`: Column in colData for batch alignment
- `residual_model_formula_str`: Formula for continuous covariates

### reduce_dimension()
- `max_components`: 2 (default) or 3 for 3D
- `reduction_method`: "UMAP" (recommended) or "tSNE"

### cluster_cells()
- `k`: Number of nearest neighbors (default: 20)
- `resolution`: Cluster granularity (default: 1e-5)

### learn_graph()
- `learn_graph_control`: List of graph learning parameters

### order_cells()
- `root_pr_nodes`: Principal graph node(s) to use as root(s)

## Common Issues and Solutions

### No branches visible
- Ensure UMAP is used (not t-SNE)
- Check that cells are properly clustered
- Try different k values in cluster_cells()

### Cells have infinite pseudotime
- Select root nodes in all partitions
- Check that graph is fully connected

### Graph is too fragmented
- Increase k in cluster_cells()
- Decrease resolution in cluster_cells()

### Trajectory doesn't match biology
- Check batch correction
- Verify root node selection
- Consider different preprocessing parameters

## Best Practices

1. **Use UMAP**: Recommended over t-SNE for trajectory inference
2. **Select appropriate root**: Use time point information or known starting cell type
3. **Multiple roots**: Select one root per partition for complete pseudotime assignment
4. **Validate with known markers**: Use known cell type markers to verify trajectory direction
5. **Save intermediate results**: Long analysis pipelines can fail
6. **Check partitions**: Cells in different partitions won't share trajectory

## Additional Resources

- **Monocle3 website**: https://cole-trapnell-lab.github.io/monocle3/
- **Monocle3 paper**: Nature Methods, 2019
- **Documentation**: https://cole-trapnell-lab.github.io/monocle3/docs/
- **Tutorials**: https://cole-trapnell-lab.github.io/monocle3-tutorial/

## Comparison with Monocle 2

| Feature | Monocle 2 | Monocle 3 |
|---------|-----------|-----------|
| Graph learning | MST on DDRTree | UMAP + graph learning |
| Speed | Slower | Faster |
| 3D trajectories | Yes | Yes |
| Partition support | Limited | Full |
| Best for | Small datasets | Large datasets |
