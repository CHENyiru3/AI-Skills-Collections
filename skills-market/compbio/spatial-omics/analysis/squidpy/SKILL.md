---
name: squidpy
domain: compbio
description: Analyze spatial neighborhoods, co-occurrence, autocorrelation, images, or spatial plots with Squidpy, including coordinate, library, graph, and permutation contracts.
license: MIT license
metadata:
  version: "1.0.1"
  skill-author: Eric Yiru
---

# Squidpy spatial analysis

Inspect Squidpy/Scanpy/SpatialData versions, the actual input schema, spatial coordinates, sample/library identifiers, image metadata, count/normalized layers, and biological replicate structure. Install the `squidpy` package if setup is requested; notebooks are documentation, not a substitute package name.

## Coordinates and graph

- Align observations and coordinates by stable IDs. Check axes, units, image scale/origin, tissue masks, and library metadata using the schema expected by the selected plotting/reader API.
- Choose an appropriate spatial graph: grid/platform topology, radius, kNN, or Delaunay, with explicit parameters and sample boundaries. Inspect neighborhood sizes, edge distances, disconnected regions, and long edges across tissue gaps.
- Use the installed `sq.gr.spatial_neighbors` signature. Do not add transcriptional PCA parameters to a coordinate graph API or assume an unsupported coordinate-type value.
- Scanpy expression neighbors use their specified expression representation; they do not automatically combine spatial and transcriptional distances. Name the graph used by every clustering/statistical operation.

## Statistics and images

Select the actual statistic and its assumptions: neighborhood enrichment, co-occurrence, centrality, spatial autocorrelation, or Ripley-type summaries. Record category keys, graph keys, distance bins, permutations/null model, seed, and multiple-testing policy.

For Moran's I, distinguish effect-size ranking from adjusted statistical significance. Inspect expression layer/use-raw choices, missing/constant features, graph normalization, and result columns. Do not label the top I values significant without testing/correction.

Analyze sections independently or use a documented multi-library design. Spatial observations within a tissue are not independent donor replicates; assess donor/section variation before biological claims.

For image features, verify image/label alignment, crop scale, segmentation, channel meanings, and feature-to-cell mapping. Use supported plotting/interactive APIs rather than invented heatmap or server methods.

## Check and save

Run on a representative region first; inspect graph edges and a spatial overlay, then result dimensions/category names and sensitivity to a justified neighborhood scale. Preserve counts, coordinates, library metadata, selected graph keys, statistical parameters, and versions with results.

Consult the [Squidpy API](https://squidpy.readthedocs.io/en/stable/api.html), especially [spatial neighbors](https://squidpy.readthedocs.io/en/stable/api/squidpy.gr.spatial_neighbors.html) and [spatial autocorrelation](https://squidpy.readthedocs.io/en/stable/api/squidpy.gr.spatial_autocorr.html), for exact signatures.
