# Implementation and validation

Use this when translating a method to code, diagnosing a discrepancy, or designing evidence. This is a claim-driven engineering guide, not a fixed test-suite requirement for every small edit. For scvi-tools interfaces read [scvi-tools-alignment.md](scvi-tools-alignment.md).

## Equation-to-code contract

For each mathematical object record its symbol, distribution/support, tensor axes, parameterization, source inputs, code owner, and testable invariant. Typical axes are Monte Carlo sample, observation, feature, latent coordinate, group, component, and neighbor. Event dimensions are not interchangeable with batch dimensions.

Separate ownership of:

- observed covariates, masks, exposure, and graph indices;
- fixed preprocessing statistics and empirical prior estimates;
- shared neural weights and other point-estimated global parameters;
- global random variables with variational distributions;
- local amortized latents;
- local non-amortized variational or MAP parameters indexed by stable observation IDs.

The last category needs explicit new-observation behavior, memory accounting, checkpoint state, and distributed ownership. Shuffling a loader must not change which local parameter belongs to an observation.

Keep these responsibilities separable even if the framework uses different names:

| Responsibility | Contract |
|---|---|
| Data adapter | Validate observations, masks, covariates, feature/category order, relationships, split and identity |
| Inference | Return posterior parameters/distributions and samples from allowed information |
| Generative computation | Map latent samples and conditions to valid likelihood parameters |
| Objective | Return named reconstruction, KL/prior, and auxiliary terms plus scalar optimization target |
| Training | Own optimizer groups, schedules, gradient routing, minibatch scaling, stopping and checkpoints |
| Query | Implement a named statistical quantity with output scale, conditioning, random sources and aggregation |

A network that outputs a mean does not implement a complete likelihood without its dispersion/scale and normalization. A latent named “nuisance” does not implement nuisance removal unless the query uses it as specified.

## Numerical and gradient correctness

Check the issues introduced by the selected model, not an exhaustive universal list:

- Use positive support transforms for scales/rates and normalized mixture weights. State variance versus standard deviation; Gamma rate versus scale; NB mean versus library parameterization. Check implied moments on a small example.
- Compute mixture probabilities using log-sum-exp. Check analytical KLs against a Monte Carlo calculation in a tractable case when implementing custom expressions.
- Sample with a differentiable path where intended. Test shared-encoder and stop-gradient paths using the isolated loss term, not only the total loss.
- Select or safely fill observed entries before evaluating likelihoods. Multiplying `0 * NaN` or `0 * -inf` does not mask a missing value safely.
- Sum likelihood event dimensions before reducing observations; include a local latent KL once per unit, not once per feature. If different panel sizes are reweighted, document that the target objective changes.
- Keep global penalties on the declared dataset scale. A training framework's internal reduction can otherwise duplicate or weaken a global term.
- For sampled neighborhoods distinguish target nodes from context nodes; avoid counting target likelihoods twice, and justify edge sampling and detached neighbor approximations.
- Covariance penalties require correct centering and a stable determinant calculation; rank deficiency and the ridge parameter can alter their meaning. MMD requires a declared target distribution, kernel scale, estimator, and batch cost.

Keep precision-sensitive log probabilities, special functions, and covariance calculations at a suitable precision. Mixed precision is a measured implementation option, not a reason to change the mathematics silently.

## Develop in informative increments

Start with the smallest runnable model supporting the target. Verify a finite forward/backward pass, expected gradients, and a meaningful tiny-data fit or known limiting case. Add a proposed block, likelihood feature, prior, or regularizer only with the diagnostic it is intended to improve. A useful development order is data contract → distributions/objective → small training run → posterior query → claim-specific evaluation → scale, adapted to existing code.

Track reconstruction, every KL or prior penalty, auxiliary terms, relevant scales/mixture weights, latent activity, and optimization diagnostics individually. A falling total loss may conceal worsening fit or collapse under a changing coefficient. Record seeds, configuration, feature/category mappings, split IDs, preprocessing scope, software version, and checkpoint selection criterion.

Do not debug a scientific result by changing its scientific target. For an implementation correction, preserve input data, split, normalization, objective, and query unless the correction specifically concerns one of them; report such a change explicitly.

## Claim-to-evidence menu

Choose rows relevant to advertised behavior.

| Claim | Evidence | Failure that an attractive embedding or loss can hide |
|---|---|---|
| Correct probabilistic computation | Distribution support/moments, tractable likelihood/KL checks, gradient and reduction checks | Invalid parameters, duplicated KL, disconnected gradient |
| Adequate observation model | Held-out predictive score and posterior predictive summaries of relevant structure | Correct mean but wrong tails, dispersion, zeros or correlations |
| Recoverable latent roles | Controlled simulation with known factors, recovery modulo allowed transformations | Rotation, role swapping, one block explaining everything |
| Useful uncertainty | Interval coverage, predictive calibration, simulation-based checks or small reference posterior where appropriate | Underdispersion; uncertainty correlates with error but is poorly calibrated |
| Desired nuisance adjustment | Target preservation plus unwanted-information reduction, absent-class or negative controls | Overcorrection of genuine variation |
| Reliable imputation | Hide truly observed values using a relevant missingness pattern and score against truth | Leakage from input, panel-specific failure, missing-not-at-random bias |
| Generalization | Split by deployment unit: new subject, instrument, group, condition, graph or time | Context leakage; random rows sharing the same source |
| Population contrasts | Independent replication, null controls, effect recovery and multiplicity checks as applicable | Pseudoreplication; posterior certainty conditional on a misspecified model |
| Scalable implementation | Runtime, memory and numerical behavior at relevant sizes | Dense graph/matrix materialization; per-unit parameters growing unexpectedly |

For simulation-based calibration, specify what is drawn from the prior and what is refit. Calibration conditional on fixed neural weights does not assess uncertainty in those weights. When latent coordinates are non-identifiable, test identifiable functions or align only within the justified equivalence class.

Fit preprocessing and empirical priors within the allowed split. Disclose transductive context access. Synthetic observations generated by the same model test self-consistency; add misspecification or independent reference evidence before drawing broad empirical conclusions. Model-derived annotations are not independent ground truth.

Compare methods with matched observation inputs, labels, covariates, features, split, and meaningful compute/tuning budgets. Report changed sample coverage or discarded units. Tune on validation data; preserve the test data for the final comparison. Use per-component metrics when a method claims a decomposition. Do not multiply seed runs or metrics when they cannot change the conclusion.

## Diagnose the layer that failed

| Symptom | First discriminating checks | Possible next action |
|---|---|---|
| NaN or impossible likelihood | Support, scale transform, mask selection, precision, reductions | Fix numerical or data-contract error |
| Good reconstruction, unused latent | Per-block KL/activity, decoder shortcuts, gradient flow | Reconsider capacity, optimization schedule or need for block |
| Latent roles exchange across runs | Identifiability assumptions and equivalent transformations | Weaken interpretation or add justified information/constraints |
| Clean batch mixing, lost target signal | Confounding, absent populations, label access | Change model or query; do not reward mixing alone |
| Poor intervals, good means | Posterior family, missing parameter uncertainty, likelihood misspecification | Local refinement/richer q/reference inference or observation-model revision |
| Local fit improves greatly after refinement | Fixed generative model, same variational family before/after | Evidence of amortization/optimization gap, not necessarily wrong likelihood |
| Query output changes after save/load | Feature/category/ID mapping, preprocessing, mode and random state | Repair persistence and query contract |
| Single-device success, distributed failure | Global/local state, duplicated observations, all-reduce scaling, graph context | Limit support or implement a scientifically equivalent distributed algorithm |

## Organize the resulting methodology

Write in an order that lets a reader reconstruct the method:

1. Data, observation process, target quantity and assumptions.
2. Variable table, generative process and factorized joint.
3. Posterior family, information access, ELBO and any modified objectives.
4. Parameterization, optimization, schedules and computational approximations.
5. Definitions and algorithms for exported posterior queries.
6. Validation splits, comparator information, metrics, ablations, reproducibility and limits.

Architecture tables and hyperparameters support these sections; they do not substitute for the probability model. A graphical model is useful when dependencies are complex: distinguish observed/random/deterministic objects, plates, and generative versus inference arrows. A result section should connect each modeling claim to evidence before presenting additional application examples.
