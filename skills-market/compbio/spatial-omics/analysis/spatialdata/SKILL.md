---
name: spatialdata
domain: compbio
description: Read, construct, validate, transform, or analyze SpatialData containers and Zarr stores, including images, labels, points, shapes, and linked AnnData tables. Use for actual SpatialData workflows.
license: MIT license
metadata:
  version: "1.0.1"
  skill-author: Eric Yiru
---

# SpatialData

Inspect the installed SpatialData version, store schema, element names, dimensions, coordinate systems, and table annotations before editing. Preserve the original store or work in a separate output store.

## Container and identity contracts

- Use the version's documented reader, commonly `spatialdata.read_zarr`, rather than assuming `SpatialData.read` exists.
- The container has named `images`, `labels`, `points`, `shapes`, and `tables` collections. A selected table is already an AnnData object; do not call an invented `.table.to_adata()` conversion.
- Select tables by name and inspect their `region`, region-key, and instance-key annotations. Each table row must map to the intended element instance. Keep identifiers and mapping metadata synchronized when filtering or renaming.
- Construct elements through supported model parsers, with explicit axes, channels, coordinate transforms, and table linkage. Do not infer that identical row positions imply matching instances.

## Spatial operations

Choose the target coordinate system explicitly. Distinguish pixel indices, physical coordinates, image/label axes, and transformations. Transform or query through the supported API; do not alter coordinates while leaving the transform metadata inconsistent.

For image/polygon registration, inspect an overlay at representative locations and preserve scale, orientation, and origin. For aggregation, define which point/shape/label instances contribute and how overlaps or missing mappings are handled.

Select a table before a Scanpy workflow and preserve its count/normalized-layer meanings. SpatialData organizes data and transformations; it does not guarantee that a generic expression-neighbor graph uses spatial proximity.

## Persist and verify

Check element validity, table-instance coverage, duplicate IDs, dimensions, and coordinate-system membership. Preserve lazy/chunked operations for large images; avoid computing an entire store just to inspect metadata.

Use supported write/update operations with an explicit destination. Reopen the output and verify selected table rows, element names, transforms, and a spatial overlay. Report format/version changes and any data not round-tripped.

Consult [SpatialData API](https://spatialdata.scverse.org/en/stable/api/SpatialData.html), [models](https://spatialdata.scverse.org/en/stable/api/models.html), and version-matched I/O tutorials.
