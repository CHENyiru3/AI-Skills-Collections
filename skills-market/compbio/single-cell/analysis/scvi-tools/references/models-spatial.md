# Spatial models: select the package and data contract

Spatial methods in the scvi ecosystem do not share one universal `scvi.model`
namespace or setup API. Check the installed release and official tutorial first;
some spatial models moved to the scVIVA ecosystem. Tangram is a separately
identified tool/integration, not proof that `scvi.model.TANGRAM` exists.

| Method | Intended question | Contract to establish |
| --- | --- | --- |
| DestVI | Reference-based spot deconvolution with within-type variation | Compatible reference/spatial counts, feature order, reference labels, and the documented conditional reference model (not a generic SCVI substitution) |
| Stereoscope | Reference-based cell-type contribution estimates | Distinct supported RNA/reference and spatial stages, matched genes, label coverage, model-specific count likelihood |
| Tangram | Mapping reference cells/clusters to spatial observations | Actual package API, shared training genes, preprocessing/density assumptions, held-out gene evaluation |
| gimVI | Cross-assay expression imputation | Supported paired model setup, assay identity, shared/measured features and held-out validation; not arbitrary concatenation followed by a universal setup call |
| scVIVA / ResolVI | Model-specific spatial environment or measurement questions | Current owning package, coordinates/neighborhoods, count/measurement inputs, covariates, and supported outputs |

## Workflow

1. Define whether observations are cells, mixed-cell spots, bins, or regions.
   Record sample, coordinate units/frame, segmentation/binning, and reference
   compatibility. Preserve original counts and feature/cell identifiers.
2. Follow the versioned primary tutorial's reference-training and spatial-fitting
   stages. Verify real classes, capitalization, setup fields, constructor inputs,
   and output methods. Do not use an invented `DESTVI.from_rna_model` or universal
   `STEREOSCOPE` recipe in place of that contract.
3. Align genes and observation IDs explicitly. Inspect reference annotation
   uncertainty, missing cell populations, batch/technology differences, and model
   assumptions. Confirm that every named layer/covariate actually exists.
4. Fit a bounded pilot and inspect finite objectives, proportions/abundances or
   mapping weights, reconstruction checks, held-out measurements, and spatial
   overlays. Normalize or interpret outputs according to the method; proportions,
   absolute abundance, mapping scores, and expression are different quantities.
5. Treat deconvolution, imputation, and mapped locations as model-derived results.
   They are not direct measurements or proof of single-cell spatial resolution.
   Evaluate across independent samples where the claim requires generalization.
6. Save reference and spatial model revisions, feature order, registry/config,
   data provenance, coordinate mappings, diagnostics, and output meanings.

Start from [official scvi-tools tutorials](https://docs.scvi-tools.org/en/stable/tutorials/index.html)
and follow their current links to the owning spatial package. Match older project
versions to their archived API rather than migrating a saved model silently.
