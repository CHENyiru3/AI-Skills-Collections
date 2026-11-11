---
name: vi-methodology-development
description: Formulate, implement, or review a variational-inference or VAE research method, from generative assumptions and ELBO to posterior queries and validation. Use for method development or scvi-tools model integration; not routine use of an existing model.
metadata:
  version: "1.0.0"
---

# VI Methodology Development

Connect the scientific target, observations, generative model, inference,
objective, implementation, posterior query, and evidence. VI is a family of
inference methods; a VAE is one amortized construction, not the required answer.
Respect existing scientific choices. Ask about missing intent only when it
changes the target; otherwise state provisional assumptions and continue.

## Choose the requested depth

- **Formulate:** use [design and objective](references/design-and-objective.md).
- **Implement or debug:** use [implementation and validation](references/implementation-and-validation.md).
- **Integrate with scvi-tools or prepare community software:** add the
  [version-aware framework reference](references/scvi-tools-alignment.md).
- **Write a proposal or Methods brief:** adapt only the relevant parts of
  [the methodology template](assets/methodology-brief.md).
- **Transfer a paper's design logic:** use [source patterns](references/paper-patterns.md),
  including its evidence limits. Do not inherit its biological target or defaults.

## Keep four objects explicit

First identify the observational/replication unit, estimand, available training
and use-time information, missingness, and generalization setting. For each
variable record role, support, shape/plate, conditioning, and whether it is
observed, random, deterministic, or point-estimated.

1. **Generative specification:** write a normalized joint and sampling story.
   Separate target signal from measurement effects and parameters from random
   variables. Add structure for a concrete failure of a simpler baseline.
2. **Approximate posterior:** specify factorization and information access
   independently. An encoder edge is not automatically a generative dependency.
   Justify amortized, local/global, structured, or hybrid inference.
3. **Objective:** derive the ELBO from the joint/posterior. List MAP and auxiliary
   terms, weights, reductions, schedules, stop-gradients, and estimators separately.
   A substituted loss is not an exact bound without the corresponding argument.
4. **Exported query:** define the expectation, prediction, contrast, or decoding
   operation. State what is integrated out, fixed, resampled, or removed and which
   uncertainties are unrepresented.

## Guard the scientific claim

Connect substantive components through assumption → mathematical term → code →
diagnostic/ablation. Named latents, independent priors, and low reconstruction
loss do not establish semantic recovery, nuisance removal, calibration, or causality.
State the identifying information or the weaker claim actually supported.

Choose likelihoods with measurement support, transformation, exposure, censoring,
and missingness. Distinguish missing from zero, observed from latent nuisance,
and mixtures of intensities from mixture distributions. Explain how information
is assigned between latent blocks; full confounding is not repaired by a batch
label or adversary alone. Add posterior complexity for an observed limitation,
not because a reference uses flows, multiple latents, graphs, or mixture priors.

Deliver the coherent specification and implementation map at the requested depth.
Match validation to the claim: numerical/gradient correctness, predictive fit,
recovery/calibration, target preservation, and generalization with comparable
information and label access. Compare simple statistical and VAE baselines before
crediting added complexity. Distinguish source-verified statements, reconstructions,
and proposed generalizations; report unresolved facts and stop at the requested
formulation, implementation, or review.
