---
name: draft-spatial-methods
domain: compbio
description: Draft a Methods section for a supplied spatial transcriptomics or single-cell workflow from its code, configuration and notes. Use for evidence-based Methods writing; not running new experiments or assuming a muscle-aging/3D model.
allowed-tools: Read
metadata:
  version: "1.0.1"
---

# Spatial and Single-Cell Methods

Establish the requested scope and sources. Distinguish implemented code, configured
parameters and evidence that a particular analysis actually ran. Do not describe
current defaults as historical run settings without provenance.

Organize Methods in dependency order, including only applicable steps:

- Data provenance, species/tissue, sampling/replication, platform and accessions.
- Input representations, feature/cell alignment, preprocessing/QC and normalization.
- Annotation/integration/modeling choices, references and parameter selection.
- Evaluation/splits, statistical units, uncertainty and reproducibility details.

Extract actual thresholds, versions, seeds and sample counts from supplied records.
Where unavailable, mark the missing detail or ask a focused question; do not fill
it with conventional QC thresholds, a tissue example, macrophage states or an aging
clock. Separate biological replicates from cells/spots/technical repeats.

For a real deep-learning/spatial interpolation step, specify input/output shape,
coordinate/frame conventions, training objective and relevant solver/settings from
evidence. Explain which quantities are measured, inferred or interpolated; a model
output is not an observed intermediate biological state.

Use precise scientific prose with explicit agency where needed. Preserve the
boundary between a proposed method and an executed analysis. Deliver the requested
Methods text with unresolved reproducibility gaps visible; do not rerun experiments
or invent missing details to make the section appear complete.
