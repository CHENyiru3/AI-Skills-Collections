---
name: cellxgene
domain: compbio
description: Prepare and inspect a local H5AD dataset for the CELLxGENE Annotate viewer, launch/debug the installed viewer, and manage its annotations or sharing configuration. For Census queries use cellxgene-census.
license: MIT license
metadata:
  version: "1.0.1"
  skill-author: Eric Yiru
---

# CELLxGENE viewer

Identify the product first: local CELLxGENE Annotate, hosted Discover, and Census have distinct interfaces. Inspect the installed viewer version and its `cellxgene launch --help` before using launch/configuration options.

## Prepare a working dataset

- Validate observations-by-features shape, unique stable cell/feature IDs, intended expression values, useful metadata, and supported embeddings in `obsm`.
- Preserve count/normalized-layer meaning and annotation provenance. Check which expression matrix the viewer actually displays and uses for exploratory comparisons.
- For subsetting or adding labels, align metadata by cell IDs and write a new H5AD. Do not turn a positional list into a purported barcode-matched annotation file.
- Use the installed viewer's documented annotation storage/configuration schema. Do not assume a generic TSV with a `cell_id` column is accepted unchanged.

## Launch and inspect

Launch the selected file on loopback for local use, using a supported host/port option only when needed. Check the chosen port, actual startup URL/logs, dataset load, embedding, metadata filtering, gene coloring, selection, and annotation persistence.

Binding to `0.0.0.0` can expose the service beyond the local machine; choose network access only for the requested sharing context and its actual authentication/deployment arrangement. A local viewer launch does not publish a dataset to Discover.

Do not invent Flask embedding, notebook server, menu-export, or YAML-layout APIs. Use documented interfaces for that product/version. Save annotations/subsets through supported mechanisms and verify that they correspond to the selected observation IDs.

## Deliver and troubleshoot

Distinguish package/import failures, incompatible H5AD/schema, missing embedding, memory pressure, and network/browser errors. Assess performance with the real dataset instead of asserting a universal cell-count limit.

Report the file/version, local URL, data semantics, tested interactions, annotation destination, and dependencies needed for continued use. Treat viewer differential-expression output as exploratory; donor-aware condition inference belongs in a suitable statistical workflow.

Use the [official repository and documentation links](https://github.com/chanzuckerberg/cellxgene) for supported local viewer commands and configuration.
