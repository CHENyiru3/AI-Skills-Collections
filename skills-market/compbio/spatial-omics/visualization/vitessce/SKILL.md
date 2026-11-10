---
name: vitessce
domain: compbio
description: Prepare data and build or debug Vitessce view configurations, widgets, and linked spatial/single-cell visualizations. Use when Vitessce is requested or already part of the project.
license: MIT license
metadata:
  version: "1.0.1"
  skill-author: Eric Yiru
---

# Vitessce

Identify the Python/JavaScript client versions, view-config schema version, deployment context, supported file loaders, and intended dataset. Do not assume a raw H5AD URL works with every loader.

## Prepare and configure

1. Inspect observation/feature identifiers, embeddings, expression layers, cell sets, segmentations, and image coordinate systems. Preserve mappings across these assets.
2. Choose a supported wrapper or file schema from the installed package. Convert or expose data in the required format, with explicit paths to arrays and metadata.
3. Construct a `VitessceConfig` using documented dataset, file/wrapper, view, layout, and coordination APIs for that version. Verify enum and method names before use; do not copy unverified `ViewConf`, `FileType.H5AD`, `export_plugins`, or CLI initialization examples.
4. Link the relevant coordination scopes so selections, cell sets, gene selection, spatial view, and embeddings refer to the same observations. A dashboard that renders independent views is not necessarily coordinated.
5. Export through a supported config method and validate against the matching schema. Use actual accessible asset URLs or local serving paths, not a placeholder domain.

## Serve and inspect

Check browser network requests, range-request requirements, CORS, authentication, mixed content, and asset size. Notebook-local paths and temporary local servers may not work for collaborators. Do not make protected datasets publicly accessible merely to resolve a loader error.

Open the intended widget or viewer, confirm the selected matrix/layer, and test linked selection, feature coloring, cell sets, and image/segmentation alignment. Inspect console and network errors as well as the screenshot. Distinguish a valid JSON config from a functioning visualization.

Deliver the config plus required assets/serving instructions and version information. Publish or upload only within the requested scope; describe external resources and access limitations.

Use the [Python documentation](https://python-docs.vitessce.io/) and [core Vitessce documentation](https://vitessce.io/) for loaders, wrappers, configuration schemas, and supported components.
