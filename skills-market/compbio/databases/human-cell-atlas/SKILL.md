---
name: human-cell-atlas
domain: compbio
description: Find, select, and retrieve Human Cell Atlas projects, matrices, files, and associated metadata from the HCA Data Portal and its documented APIs. Use for HCA-specific data access and provenance.
license: MIT license
metadata:
  version: "1.0.1"
  skill-author: Eric Yiru
---

# Human Cell Atlas data access

Use the [HCA Data Portal](https://data.humancellatlas.org/), [quick-start guide](https://data.humancellatlas.org/guides/quick-start-guide), and [documented APIs](https://data.humancellatlas.org/apis). HCA and CZ CELLxGENE Census are distinct access systems with different inventories and identifiers; a Census query is not a generic HCA download API.

## Select the resource

1. Define tissue/organism, disease/developmental state, assay, donor criteria, desired raw or processed output, and analysis purpose.
2. Inspect project-level metadata, publication, protocols, donor/specimen counts, processing provenance, access conditions, and available matrices/files.
3. Select the actual project/matrix/file identifiers. Distinguish project-supplied matrices, portal-generated matrices, and raw sequencing files. Do not assume every project supplies H5AD or every file is an independent sample.
4. Export the file manifest and associated metadata through the current portal/API. Preserve the filter/query, project and file IDs, URLs, checksums, retrieval date, and revision information exposed by the source.

## Download and curate

Bound downloads by the requested files and estimated size. Follow the selected file URLs and documented paging/export flow rather than inventing a package argument such as `get_anndata(tissue=...)`.

Verify transfer status/checksums where supplied and keep metadata with the matrices. Join cell/library/sample/donor identifiers using documented keys; check one-to-many relationships and duplicate cells across related matrices or atlas releases.

For reference use, inspect annotation provenance, feature identifiers, count/normalized layers, organism/reference, assay differences, and representation of the target population. A portal filter or cell-type label alone does not validate a marker set or reference-mapping conclusion.

Deliver an evidence-linked selection/download inventory and explicit exclusions or missing metadata. Cite source projects and data versions. Treat unavailable access and absent data as unresolved rather than filling them from a different atlas silently.
