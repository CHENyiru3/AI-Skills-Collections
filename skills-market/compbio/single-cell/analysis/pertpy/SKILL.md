---
name: pertpy
description: Select, implement, interpret, or debug a pertpy workflow for single-cell perturbation data. Use for a concrete pertpy analysis; not generic Scanpy preprocessing or unrelated prediction frameworks.
metadata:
  version: "1.0.0"
  reference-package-version: "1.4.0"
---

# Pertpy

Translate a perturbation-analysis question into the appropriate pertpy workflow, with explicit inputs, controls, experimental units, and interpretable outputs.

The references retain the original **pertpy 1.4.0** source-review snapshot from **2026-10-08**. Newer releases exist and stable documentation moves: inspect the project’s installed version before using version-sensitive calls. [Sources and maintenance](references/sources.md) records the dated review and known mismatches; this collection import did not rerun the statistical workflows.

## Start with the data and question

1. Identify the requested outcome: assign guides, detect effective perturbations, test expression/composition, rank responding cell types, compare perturbations, predict responses, or annotate mechanisms. Preserve the user's chosen method and experimental design.
2. Inspect the selected Python environment, pertpy version, AnnData/MuData modalities, matrix provenance, and relevant metadata. Read [setup and data](references/setup-data.md) when installation, input preparation, or compatibility needs attention.
3. Map actual columns to perturbation, exact control label, sample/replicate, cell type, and any batch, dose, or time covariates. A column named `batch` is not automatically a biological replicate. Check controls exist in each analysis stratum.
4. Select the relevant reference below. Use existing project decisions; resolve genuinely missing scientific choices before fitting the dependent model. Continue inspection and implementation that does not depend on those choices.
5. Run a small representative check before an expensive fit. Verify output locations, group sizes, skipped groups, and diagnostic warnings. Report the method, representation/layer, contrast direction, independent sample counts, seed where supported, package version, and output paths.

## Choose the workflow

| Question | Pertpy entrypoint | Read |
|---|---|---|
| Which guides are present in each cell? | `pt.pp.GuideAssignment` | [Guides and efficacy](references/guides-efficacy.md) |
| Which guide-bearing cells respond, or how strongly? | `pt.tl.Mixscape`, `pt.tl.Mixscale` | [Guides and efficacy](references/guides-efficacy.md) |
| Which genes change between conditions? | `pt.tl.PyDESeq2`, `EdgeR`, simple DE tests | [Expression and abundance](references/expression-abundance.md) |
| Which neighborhoods or cell-type proportions change? | `pt.tl.Milo`, `Sccoda`, `Tasccoda` | [Expression and abundance](references/expression-abundance.md) |
| Which cell types respond most strongly? | `pt.tl.Augur` | [Distances and prioritization](references/distances-prioritization.md) |
| How different are cell populations? | `pt.tl.Distance`, `DistanceTest` | [Distances and prioritization](references/distances-prioritization.md) |
| How do perturbations relate, combine, or vary with dose? | `PseudobulkSpace`, `CentroidSpace`, `DistanceSpace` | [Spaces and prediction](references/spaces-prediction.md) |
| Can a response be predicted or matched to controls? | `pt.tl.Scgen`, `Cinemaot` | [Spaces and prediction](references/spaces-prediction.md) |
| What mechanisms, gene sets, or multicellular programs are implicated? | `pt.md`, `pt.tl.Enrichment`, `Dialogue` | [Annotation and programs](references/annotation-programs.md) |

## Operational constraints that matter

- Use `import pertpy as pt`. In 1.4.0: `pt.ds`/`pt.dt` expose datasets, `pt.pp` preprocessing, `pt.tl` analysis, and `pt.md` metadata. Most tools are instantiated classes with their own plotting methods; check the class API before assuming a `pt.pl` function exists.
- Preserve verified raw counts before normalization. A layer called `counts` or `.raw` is not evidence of raw counts. Count models, normalized-expression methods, and embedding methods require different inputs.
- Preserve sample-level replication for inferential DE and abundance analyses. Cell counts increase sampling depth; they do not create independent donors. Aggregate within the intended sample, condition, and cell type without merging distinct treatments.
- Access MuData modality metadata explicitly and align by cell identifiers. Top-level `.obs` is not guaranteed to propagate into `mdata["rna"].obs`.
- Many methods mutate in place. Check `copy` and return semantics; do not replace an AnnData with a `None` return. Work on a copy when deriving a representation that would overwrite the analysis input.
- Match `layer`, `layer_key`, `obsm_key`, and `embedding_key` to the actual method. They are not interchangeable keyword aliases. Avoid accidental dense conversion of a full screen or all-cell distance matrices.
- Treat recipe numbers as examples, not biological thresholds. Controls, strata, reference cell types, permutation units, and evaluation splits must match the experiment.

Examples in references are adaptation templates with stated preconditions. They were checked for syntax and against release-source signatures; full statistical workflows were not run during skill creation.
