---
name: explain-bio-dl-model
domain: compbio
description: Explain a supplied deep-learning architecture in biological manuscript prose with accurate data flow and evidence boundaries. Use for model-to-text translation; not inventing biological rationale, validation or causal conclusions.
metadata:
  version: "1.0.1"
---

# Biological Deep-Learning Model Explanation

Trace the actual model from input representation through transformations/objective
to outputs. Preserve tensor axes, masks, units, data splits and the distinction
between training targets and inference inputs where they affect interpretation.
Resolve details from supplied code/configuration rather than architecture names.

Connect each design choice to the stated task only when rationale is documented
or clearly labeled as a possible interpretation. A discrete latent space does not
by itself separate biological states from technical noise; an attention map is
not automatically an explanation or causal regulatory relationship.

Separate mechanism, intended benefit and empirical evidence. State validation only
when results support it, with the relevant comparator, dataset and uncertainty.
If rationale or biological evaluation is unavailable, describe the computation
faithfully and identify the gap; do not manufacture a satisfying narrative ending.

Deliver the requested paragraph/section at the reader's technical level, preserving
necessary mathematical definitions. Stop when the architecture and support limits
are clear; additional experiments and a full manuscript rewrite are separate tasks.
