---
name: critique-bio-manuscript
domain: compbio
description: Critique a bioinformatics/computational biology manuscript for supported claims, study design, leakage and evaluation limits. Use for an explicit manuscript review; not a rewrite or an assumption that every study needs new biological experiments.
disable-model-invocation: true
allowed-tools: Read
metadata:
  version: "1.0.1"
---

# Bioinformatics Manuscript Critique

Assess the supplied manuscript and evidence against its actual claims and intended
use. Report confirmed flaws, plausible concerns and missing information separately.
A constructive review need not find a major flaw if none is supported.

Prioritize relevant questions:

- Are baselines appropriate to the task and comparison budget? Call a method
  outdated only with version/date evidence; supplied text alone may not establish
  current state of the art. State literature coverage limits.
- Are train/tune/test units independent at the relevant donor, specimen, site or
  spatial/temporal level? Inspect preprocessing, feature selection, annotation and
  checkpoint selection for leakage across those boundaries.
- Do metrics and uncertainty support the claim? Distinguish predictive performance,
  implementation correctness and biological interpretation. Established annotations
  or pathways can be useful evidence but are not infallible biological ground truth.
- Are data exclusions, confounding, failure modes and generalization limits visible?
  Recommend additional analyses only when they can resolve a material claim gap.

Use locations and concrete effects in major/minor comments when that format is
requested. Preserve strengths and uncertainty; do not invent missing experiments
as universal acceptance gates or claim a literature search that was not performed.
Stop at the scoped critique unless drafting or new analyses were also requested.
