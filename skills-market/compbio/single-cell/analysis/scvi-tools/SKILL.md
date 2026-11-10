---
name: scvi-tools
domain: compbio
description: Select, configure, train, or debug a specific scvi-tools probabilistic model for single-cell RNA, ATAC, multimodal, spatial, or specialized data, including model-specific data registration and uncertainty.
license: BSD-3-Clause license
metadata:
  version: "1.0.1"
  skill-author: K-Dense Inc.
---

# scvi-tools models

Choose the model from the actual modality, measurement distribution, paired/unpaired structure, reference availability, and scientific target. Inspect installed scvi-tools/backend versions and model-specific documentation before writing setup/training code.

## Data registration contract

- For count-based SCVI, provide verified unnormalized counts in `X` or a named existing layer and register that location through `SCVI.setup_anndata`. Do not name an absent layer or invent metadata columns in an example.
- Other models can require proteins, accessibility, spliced/unspliced values, methylation observations, MuData, references, or distinct setup methods. Neither raw counts nor one identical setup/train/extract API applies universally.
- Check cell/feature order, feature types, missing modality encoding, batch labels, categorical levels, and supported covariates. Preserve counts and meaningful biological covariates; treating donor/condition as nuisance can remove the target signal.
- Match HVG selection to count/log requirements and the model's supported feature contract. Do not silently renormalize an input the likelihood expects as counts.

## Training and evaluation

1. Register data, instantiate the selected supported model, set relevant seeds, and choose explicit device/precision/early-stopping/split settings for the installed API.
2. Run a small fit to check finite objective, shapes, trainable parameters, and data registry. Then inspect training/validation behavior and diagnostics appropriate to that model.
3. Evaluate integration with both batch mixing and biological preservation, including rare populations and donor variation. A latent representation is not automatically validated batch correction.
4. Match extracted output to its meaning: latent coordinates, denoised/normalized expression, posterior samples, transferred labels, or proportions. Align axes before assigning to `obsm` or a layer; a feature-subset output cannot be assigned to a full-width layer silently.
5. For DE, document population/contrast, batch conditioning, effect threshold, posterior/FDR interpretation, and biological replicate limitations. Model uncertainty does not remove pseudoreplication or confounding.

## Persistence and references

Save to a deliberate new directory with model class/version, feature order, setup registry, reference/checkpoint provenance, and associated data required for reload. Verify reload on the intended feature/covariate contract. Use supported query/reference mapping rather than re-registering incompatible data silently.

Read only the needed modality guide: [RNA](references/models-scrna-seq.md), [ATAC](references/models-atac-seq.md), [multimodal](references/models-multimodal.md), [spatial](references/models-spatial.md), or [specialized](references/models-specialized.md). Some listed methods are external ecosystem tools, not guaranteed installed `scvi.model` classes; verify package ownership and availability.

Use [workflow examples](references/workflows.md), [DE interpretation](references/differential-expression.md), and [theory](references/theoretical-foundations.md) when needed. Check concrete APIs against [official scvi-tools documentation](https://docs.scvi-tools.org/en/stable/) before execution. Do not install unrelated GPU extras or promote another platform automatically.
