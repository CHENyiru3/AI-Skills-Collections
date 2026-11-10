---
name: schard
domain: compbio
description: Read or convert H5AD data with cellgeni/schard into Seurat or SingleCellExperiment, including its supported spatial conversion helpers. Use for schard-specific interoperability and mapping issues.
metadata:
  version: "1.0.1"
---

# schard conversion

Identify the installed schard revision, source H5AD schema, target object, available matrices, and memory budget. Use the [authoritative repository](https://github.com/cellgeni/schard) for matching function signatures.

## Conversion contract

- Inspect `/X`, `/layers`, `/raw/X`, `/obs`, `/var`, embeddings, and spatial metadata before choosing a source matrix. `raw/X` is an AnnData snapshot and may already be log-normalized; `use.raw = TRUE` selects that snapshot, not guaranteed raw counts.
- Use supported `h5ad2sce`, `h5ad2seurat`, or spatial helpers as appropriate. Confirm installed arguments rather than assuming all readers accept the same options.
- Preserve original cell and feature identifiers. AnnData and R assay orientations differ; let the documented converter handle this, then verify names and selected values.
- For `h5ad2seurat_spatial`, inspect image/slide keys, coordinate order/scale, barcode coverage, and whether the requested return is one object or a list. Do not infer spatial compatibility from the filename alone.

## Metadata and reductions

Check actual metadata columns and reduction names after conversion; they can be renamed. Choose `group.by`, reduction, image, and assay from the converted object, not a hardcoded public tutorial sample.

When reading HDF5 matrices directly, inspect helper orientation and dimension names. Align embedding rows to observation identifiers before plotting. Never transpose or relabel solely because the resulting dimensions happen to match.

## Validate and deliver

Compare source and target observation/feature names, selected values and totals, count/normalized-layer semantics, metadata types, and embedding dimensions. Inspect an image overlay for a spatial conversion. Save to a new destination and report unsupported or lost components.

Do not download unrelated public examples automatically. Use a small selected fixture when available, preserve sparse structures where supported, and explain if a conversion materializes data in memory.
