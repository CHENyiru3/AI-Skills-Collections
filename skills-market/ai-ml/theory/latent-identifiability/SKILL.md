---
name: latent-identifiability
description: "Develop, prove, or audit identifiability claims for latent-variable and representation-learning models, including VAEs, nonlinear ICA, and spatial or multi-view biological models. Use to turn a model idea into a quantified theorem, identify the remaining symmetries, construct a lemma-based proof, or find counterexamples. Includes a SIMVI worked example and checks connecting theory to estimators. Not a substitute for empirical benchmarking or a general manuscript-editing workflow."
---

# Latent Identifiability

Turn a research mechanism into a defensible identification result, or establish precisely why the requested result does not follow. Write the mathematical argument when requested; do not stop at a proof plan. Keep population identifiability, estimation consistency, optimization, individual latent recovery, and causal identification separate.

## Start from the research state

Use the user's model, notes, equations, code, and requested destination. Ask only for information that changes the mathematical problem and cannot be inferred. With an incomplete model, work on an explicitly labeled provisional formulation and identify the missing decisions. Do not fabricate biological mechanisms or silently add identifying information.

Enter at the appropriate stage: informal idea -> formal specification; specified model -> symmetry search; candidate theorem -> proof or attack; existing proof -> line-by-line audit. An empirical performance question does not need to become a theorem task.

This is self-contained. It adapts the supplied `flow-idea-to-proof` sequence (stress-test, assumptions, claim, lemmas, attack, write-up), but does not depend on its singleton skills or require delegation. If that router is available and explicitly used, this skill can supply the identifiability-specific reasoning within its stages. Do not make the user complete a proof step merely to preserve the router's teaching format.

## 1. Define what the data can identify

Create a compact model specification:

- Observed variables, latent blocks, covariates, graph/time/view structure, and sampling unit.
- The exact observable law: `P(X)`, `P(X|U)`, a multi-view joint law, or the full graph law. Specify whether the graph/design is fixed, random, or observed. Node marginals do not determine a graph joint law.
- Generative factorization, noise kernel, nuisance parameters, parameter class, supports, latent dimensions, and required regularity.
- Which objects are known, observed, learned, or unobserved. A recovered latent block is not an observed auxiliary variable until its recovery has been justified.
- Target: parameters, latent blocks, sufficient statistics, posterior laws, a subspace, or a downstream functional.

Define the admissible class before comparing equivalent fits. Audit normalizers that depend on latent values; support restrictions; positive definiteness; conditional independence; and whether the global model actually induces the claimed local law. Use an explicit valid example to show the assumptions are jointly satisfiable when their compatibility is uncertain.

Distinguish a latent realization `W`, a noiseless signal `R=f(W)`, an observation `X`, a variational draw, and a posterior mean. They are different proof objects.

## 2. Search for observational symmetries first

Try transformations `W_tilde=T(W)` with `f_tilde=f o T^{-1}`. Check that the transformed prior/noise/mechanism remains in the admissible class and preserves the specified *observable law*, not just a covariance or reconstruction loss.

Test likely symmetries: permutations, scales/signs, orthogonal rotations, general linear mixing, block mixing, nonlinear measure-preserving maps, duplicated dimensions, and unobserved directions. Choose tests that fit the model.

Define the intended equivalence relation explicitly. A useful target is

\[
\forall\theta,\tilde\theta\in\mathcal M_{\mathcal A},\qquad
P_\theta^{\mathrm{obs}}=P_{\tilde\theta}^{\mathrm{obs}}
\Longrightarrow \tilde\theta\sim\theta.
\]

State whether the result is global, local, generic, or almost everywhere. For a functional `tau`, test whether it is constant on observational equivalence classes; full latent recovery may be unnecessary. If a surviving symmetry changes the target, provide a counterexample or narrow the target openly. Never redefine the equivalence relation so broadly that the intended biological interpretation disappears unnoticed.

## 3. Build an assumption ledger

For each assumption record: exact statement and quantifiers; objects constrained; proof step using it; domain justification; an example satisfying it; failure mode; and whether the implementation enforces, encourages, or ignores it.

Separate structural restrictions, symmetry-breaking information, analytic regularity, sampling conditions, and estimator/optimization conditions. Do not call an assumption necessary merely because the selected proof uses it. Necessity needs an admissible counterexample or a separate result.

Pay particular attention to assumptions involving both true and alternative latents. Such cross-representation fiber conditions can already enforce much of the desired separation. Marginal full support, Gaussian posterior noise, and a soft independence penalty do not establish those conditions. If the class is restricted using the unknown truth, state that dependence explicitly rather than presenting the restriction as an operational learning rule.

## 4. Design and execute the proof

Read [proof techniques](references/proof-techniques.md) for the applicable route. Read [the SIMVI case study](references/simvi-case-study.md) only when adapting its two-block, conditional-Gaussian strategy or auditing that paper.

A common dependency chain is:

`observable-law equality -> signal-law equality -> coordinate map -> block separation -> sufficient variation/rank -> restricted transformation -> global result`

Each arrow is a proof obligation, not a universal fact. Use a different route when its prerequisites fail. For each lemma state the hypotheses actually used, conclusion, domain, and unresolved step. Identify the hardest lemma before spending time polishing easy ones.

Useful routes include moment or characteristic-function inversion of a known observation kernel, change of variables, fiber/rank arguments, conditional log-density contrasts, and local-to-global gluing. External conditional exponential-family arguments require genuine conditioning information and a verified variability condition. Do not import SIMVI's assumptions into an unrelated model without scientific justification.

Verify all matrix dimensions, determinant factors, covariance versus precision conventions, and the direction of each transformation. Explain cancellations explicitly. A stochastic encoder cannot replace an inverse decoder in a proof without a connecting argument. When densities agree only almost everywhere, justify any extension to pointwise equalities or derivatives.

If a complete proof is requested, continue until it is proved, disproved, or reduced to a precisely stated unresolved lemma. Do not label a plausible sketch or an unverified citation as a theorem proof.

## 5. Attack the candidate result

Remove or weaken the load-bearing assumptions one at a time. Check rank loss, disconnected support, unknown noise, overcomplete dimensions, and collapsed or mixed representations when relevant. Use a minimal model with exact algebra before a large simulation.

A counterexample must satisfy every retained hypothesis and preserve the exact law required by the claim. A failed proof technique alone does not refute the theorem. Numerical checks can reveal sign, rank, normalization, or symmetry errors; they cannot certify an unrestricted theorem. Clearly distinguish an analytic counterexample, a numerical witness, and an unsuccessful search.

When an attack succeeds, report the original claim, the witness, and the narrowest scientifically meaningful repair. Recheck the repaired claim rather than appending assumptions indefinitely. Use [evaluation scenarios](evals/scenarios.md) when maintaining this skill, not as compulsory tasks for every research project.

## 6. Audit the bridge to learning and use

Read [implementation and estimands](references/implementation-and-estimands.md) when the claim is applied to a VAE, graph encoder, posterior mean, regression, or causal effect.

Produce a theory-to-implementation table. Check likelihood specification, decoder injectivity, prior/conditional-law restrictions, latent dimensions, penalties versus hard constraints, variational approximation, population versus empirical objectives, optimizer requirements, and sampling dependence. Distinguish consistency of a model from exact recovery of noisy individual latents.

Check downstream invariance under the theorem's residual symmetry. General nonlinear equivalence does not preserve linear regressions or Euclidean neighborhoods. An invertible affine map does not generally preserve distances. A transformed treatment needs a feasible reference and overlap on its actual support. Identifiable coordinates do not by themselves establish causal effects.

## 7. Deliver a proof dossier

Use [the dossier template](assets/proof-dossier-template.md) when a saved research artifact is requested. Otherwise provide the appropriate material inline. Adapt its length to the task; do not create empty sections or unrelated project files.

The result should contain the model and observable law, equivalence relation, quantified claim, assumption ledger, lemma dependencies, proof or explicit gap, counterexamples, implementation boundary, and references with exact locators where checked. Label the status as **proved under stated assumptions**, **proof sketch**, **open gap**, **disproved as stated**, or **not assessed**. Record whether verification was self-review, independent review, or machine-checked; do not imply stronger verification than occurred.

Use [the reference map](references/reference-map.md) to select sources by proof obligation. Before relying on an external theorem, read its statement and check that its assumptions and conclusion match the current use. Verify theorem/page numbers; mark unavailable sources as unverified and derive the needed step directly if possible. Keep published claims, your derivations, and proposed extensions distinct.

Finish with the strongest justified claim and the concrete remaining obstacle, if any. Identifiability is a property of a specified model and observation scheme, not a reward for a useful architecture or a good benchmark.
