# VI methodology brief

Use as an editable working specification. Replace prompts with decisions and evidence; omit sections irrelevant to the requested scope. Distinguish decided choices, provisional assumptions, and unresolved scientific questions. This is a template, not a completed method.

## Target and information

- Research question and quantity to estimate:
- Observational unit and independent replication unit:
- Intended users and output/query:
- Train/validation/test/use-time information, including labels and context:
- Generalization setting and split:
- Simplest adequate baseline and concrete limitation motivating an extension:

## Variable and assumption ledger

| Symbol | Role and meaning | Support and axes | Observed / random / deterministic / point estimate | Conditioning inputs | Identifying information or assumption |
|---|---|---|---|---|---|

Measurement scale, transforms, exposure, censoring, masks and preprocessing fit scope:

Potential confounding, non-identifiability, equivalence class and overlap limits:

## Generative model

Ancestral sampling story:

Factorized normalized joint distribution:

Likelihood, priors, parameterization and conditional-independence assumptions:

Why each added mechanism is needed; limiting case recovering the baseline:

## Inference and objective

Variational factorization and exact inputs to each factor:

Amortized, local, global and point-estimated parameter ownership:

ELBO derivation and approximation/estimator choices:

| Objective term | Mathematical origin and sign | Shape and reductions | Weight/schedule | Gradient recipients | Bound/MAP/auxiliary interpretation |
|---|---|---|---|---|---|

Minibatch sampling and local/global scaling:

Discrete-variable handling, graph/context approximation and gradient stops, if applicable:

## Posterior outputs

| User-facing output | Defined statistical query | Fixed / integrated / resampled variables | Conditioning/reference population | Scale and uncertainty included | Interpretation limits |
|---|---|---|---|---|---|

New-unit policy for local parameters and shared/global posteriors (freeze, infer, update or propagate), including permitted observations and timing:

## Implementation map

| Mathematical object or operation | Data field / tensor axes | Module or function | Parameterization/constraint | Meaningful correctness check |
|---|---|---|---|---|

Optimization plan, checkpoints, stopping and computational budget:

For scvi-tools: target distribution version/commit, package owner, AnnData/MuData registration, module/model/training route, save/load state and new-data contract:

| Optional capability | Needed for this target? | Inherited / implemented / unsupported | Verification evidence and limits |
|---|---|---|---|

## Evidence plan

| Scientific or software claim | Experiment/check and split | Comparator with matched information | Metric or expected behavior | Failure interpretation |
|---|---|---|---|---|

Central ablations and negative controls:

Uncertainty, identifiability and misspecification checks relevant to the claims:

## Reproducibility and communication

Data/feature/category/split identity, seeds, preprocessing, configuration, dependencies, model version and checkpoint selection:

Publication or community deliverables relevant to this task (equations, minimal example, API docs, tests, changelog, limitations):

Source provenance: paper/version/page or code commit; source-supported choices versus proposed extensions:

Current evidence, unresolved points, and next experiment or implementation step:
