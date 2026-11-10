---
name: anndata
domain: compbio
description: Create, read/write, subset, align, concatenate, or validate AnnData/H5AD/Zarr data structures, including sparse/backed storage, views, layers, graphs, and metadata. Use for data-container contracts rather than a general analysis pipeline.
license: BSD-3-Clause license
metadata:
  version: "1.0.1"
  skill-author: K-Dense Inc.
---

# AnnData data contracts

Inspect the installed AnnData version, source schema, observation/feature identities, matrix meaning, and memory budget. Choose operations that preserve alignment and the promised storage behavior.

## Structure and identity

- `X` is observations by variables. `obs`/`var` index those axes; layers have the same shape as `X`; `obsm`/`varm` align to their respective axes, while `obsp`/`varp` are pairwise matrices.
- Use unique stable IDs and join external metadata by index, asserting coverage and order. Preserve original identifiers when resolving duplicates; dimensions alone do not prove alignment.
- Record count, normalized, log, scaled, or corrected semantics for every matrix. `raw` snapshots expression and feature metadata at assignment; its name does not establish raw counts. Variable filtering can leave a different feature space in `raw`.
- Treat views versus independent copies explicitly. Materialize an intended working copy before mutation; backed copying/mutation has version-specific constraints.

## I/O and memory

Use supported `read_h5ad`/`read_zarr` and object write methods for native formats. 10x readers belong to Scanpy (`sc.read_10x_h5`/`sc.read_10x_mtx`), not invented `anndata.read_10x_*` methods. Verify other I/O namespaces against the installed release.

Backed access is not universal lazy execution: inspect which arrays remain in memory, which operations materialize, and file-handle lifetime. Preserve sparse structure where possible; estimate memory before `.toarray()`, scaling, transpose/copy, or large joins.

Write to a new destination until validation passes. Reopen and compare IDs/order, shapes, selected values, metadata types, layer meanings, embeddings/graphs, and required nested annotations.

## Concatenation

Choose the axis, inner/outer feature join, missing-feature semantics, batch labels, unique observation keys, and metadata merge policy explicitly. Absent measurements and observed zeros are not equivalent; sparse outer joins may fill zeros. Do not concatenate paired modalities as unrelated observations.

Experimental `AnnCollection` expects supported AnnData objects/mappings, not a list of filenames. Open backed objects explicitly when appropriate, retain their handles during use, and check supported joins/converters. Use version-matched on-disk concatenation facilities for scale rather than promising a string-list constructor is lazy file loading.

## Optional references

Consult only the relevant [data structure](references/data_structure.md), [I/O](references/io_operations.md), [concatenation](references/concatenation.md), [manipulation](references/manipulation.md), or [best practices](references/best_practices.md) reference. They are examples to adapt, not a mandate to run a Scanpy analysis.

Use [official AnnData documentation](https://anndata.readthedocs.io/) and [AnnCollection reference](https://anndata.readthedocs.io/en/stable/generated/anndata.experimental.AnnCollection.html) for supported storage and experimental APIs.
