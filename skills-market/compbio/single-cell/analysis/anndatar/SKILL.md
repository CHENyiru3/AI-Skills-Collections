---
name: anndatar
domain: compbio
description: Read/write H5AD or convert AnnData, Seurat, and SingleCellExperiment objects using the R package anndataR. Use for anndataR-specific interoperability with explicit assay/layer and identifier mapping.
metadata:
  version: "1.0.1"
---

# anndataR interoperability

Inspect the installed anndataR version, source object/file, target format, matrix meanings, dimensions, and memory budget. Use its matching Bioconductor documentation; do not promise lossless conversion across all object features.

## Read and map

```r
library(anndataR)
adata <- read_h5ad("input.h5ad")
```

For a supported release, `read_h5ad(..., as = "Seurat")`, `as = "SingleCellExperiment"`, or an HDF5-backed AnnData representation can select the target. Check accepted representations and conversion arguments in installed help before a large conversion.

- AnnData is observations by features; Seurat/SCE assays are features by cells. Inspect names and orientation through the converter rather than manually transposing every slot.
- Establish what `X`, each layer, and any `raw` snapshot contain. A field named `raw` is not proof of integer counts. Choose target assays/layers explicitly when automatic mapping is ambiguous.
- Preserve unique cell/feature IDs, metadata types/categories, embeddings, loadings, graph matrices, and spatial information that the target supports. Check row/column mapping independently for each.
- Do not replace identifiers with generated names merely to make dimensions fit. Record any duplicate-name repair and retain the original IDs.

## Convert, subset, and write

Use documented `as_AnnData`, `as_Seurat`, `as_SingleCellExperiment`, or object methods for the installed version. Check view versus materialized/backed behavior before mutating or closing source files. Backed access can reduce eager loading but does not guarantee every conversion stays out of memory.

Write to a new destination through the supported `write_h5ad` path. Preserve the source until validation passes. Some R-specific attributes, dimension names, reductions, or nested metadata may require an explicit mapping or cannot round-trip.

## Verify the result

Reopen the output and compare cell/feature names and order, shapes, selected count values/library totals, sparse structure, assay/layer meanings, metadata, embeddings, and any spatial mappings needed downstream. Report every unsupported or dropped component. A file that opens is not sufficient evidence of semantic equivalence.

Use [anndataR on Bioconductor](https://bioconductor.org/packages/release/bioc/html/anndataR.html) and its versioned vignettes for conversion arguments and supported data types.
