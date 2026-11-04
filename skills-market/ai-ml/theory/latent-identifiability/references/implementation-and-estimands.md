# From identification to trained representations and effects

Read only the parts relevant to the intended use. These checks prevent changing the mathematical target while moving from a population theorem to an algorithm or interpretation.

## 1. Keep the guarantees separate

| Claim | Additional obligations beyond model identifiability |
|---|---|
| The estimator converges to the correct equivalence class | Correct specification, suitable objective, sampling convergence, control of empirical approximation, and an estimator consistency argument |
| VAE optimization estimates that class | Appropriate variational family, control of the variational gap, and justified optimization conditions |
| A finite trained model is close to truth | Quantitative stability/rates, finite-sample errors, and optimization/approximation errors |
| Each cell's realized latent is recovered | A separate posterior concentration or noise-information argument; population identifiability need not remove individual uncertainty |
| A latent coordinate is a named mechanism | Remaining transformations must preserve that interpretation, or anchors/interventions must resolve them |
| A downstream effect is causal | A defined intervention, exchangeability/causal model, overlap, and a correctly targeted estimator |

The decomposition

\[
\log p_\theta(x)
=\operatorname{ELBO}(\theta,\phi;x)
+D_{KL}(q_\phi(w\mid x)\Vert p_\theta(w\mid x))
\]

explains why an expressive decoder alone is insufficient. A restricted posterior family or altered objective can select a different optimum. Penalized or reweighted objectives need their own argument; dropping terms does not preserve a lower bound on the original likelihood automatically. See [IVA20](reference-map.md) for a source that explicitly separates identification and idealized estimation conditions.

For spatial or longitudinal data, state the asymptotic regime and dependence assumptions before using iid consistency or standard errors. More correlated observations need not provide the information of the same number of independent observations.

## 2. Build a concrete correspondence table

For every load-bearing assumption, identify the exact architectural feature, objective term, or data condition claimed to enforce it. Mark each row **enforced**, **encouraged**, **assumed**, **violated**, or **unverified**, with evidence.

Examples requiring special care:

- A generic neural decoder is not guaranteed injective or globally invertible.
- A graph attention mean is input-dependent, not automatically a fixed linear conditional mean.
- Fixed conditional Gaussian covariance differs from learned heteroscedastic variance.
- Known dispersion differs from estimated dispersion; NB differs from a flexible ZINB observation family.
- Marginal prior matching does not prove cross-representation fiber coverage.
- Sampled latent full support does not imply full-dimensional support of encoder means.
- An information penalty does not minimize latent dimension over all observationally equivalent models.
- A factorized variational posterior given data is different from independence of aggregated latent blocks.

If true `Z,S` are dependent and the theorem recovers them as separate functions of inferred blocks, exact independence of those inferred blocks is incompatible with exact recovery. Treat an independence penalty as a bias to analyze, not a general certificate of disentanglement.

## 3. Check invariance of the downstream procedure

A theorem can identify a representation while leaving the chosen estimator dependent on its arbitrary coordinate system.

- A nonlinear reparameterization of a covariate preserves information under a bijection but not a restricted *linear* regression family.
- General affine changes preserve convex combinations, not Euclidean distances or least-squares objectives.
- If `S=QC`, `Q1=1`, then the same `Q` reconstructs `S M+1b^T` using `C M+1b^T`. For an approximation with error `E`, however, the objective becomes `||E M||_F^2`; its optimum is not generally invariant.
- Even if an objective is invariant under a residual symmetry, nonunique optimizers and finite optimization errors may prevent a unique fitted representation.
- Standardization can reduce affine freedom to orthogonal freedom only when the required population moments are exactly shared. Empirical whitening is not a proof of latent recovery.

Define transformations of every nuisance function and target quantity, and verify that the estimator's function class is closed under them when invariance is claimed.

## 4. Derive the estimand from the actual formula

Let `Q` be a treatment or environment representation and `Z` a proposed adjustment set. Distinguish observational regression `mu(z,q)=E[Y|Z=z,Q=q]` from potential-outcome means. Equality of the two needs causal assumptions.

Under the partially linear, heterogeneous-slope response model

\[
Y=g(Z)+\theta(Z)^\top Q+\epsilon,
\qquad E[\epsilon\mid Z,Q]=0,
\]

write `m(z)=E[Q|Z=z]` and `ell(z)=E[Y|Z=z]`. Then

\[
Y-\ell(Z)=\theta(Z)^\top[Q-m(Z)]+\epsilon.
\]

The fitted residual contribution targets a centered contrast. A fixed-reference contrast instead is

\[
\tau(z;q,q_0)=\theta(z)^\top(q-q_0).
\]

Do not interchange them. Even if `g`, `theta`, and `m` are linear, `ell=g+theta^T m` can be quadratic. First-stage linear projections therefore need not equal conditional expectations. The formula's validity as a causal contrast also requires an appropriate causal model.

Residualization resembles double machine learning, but DML guarantees require the actual score's orthogonality and appropriate nuisance, sampling, and fitting conditions. A loop named `Kfold` is not cross-fitting unless nuisance predictions use data excluded from nuisance training. A linear OLS analysis may be valid under its own assumptions without invoking general DML theory. See [DML18](reference-map.md).

## 5. Treatments on a simplex

For archetype weights `q_j>=0`, `sum_j q_j=1`, the zero vector is infeasible. Choose a feasible reference, a contrast basis, or explicitly define an extrapolative target and its additional model dependence.

If weights are residualized using the same linear design with an intercept, `sum_j q_bar_j=0`. Then adding a common function `a(z)` to every slope does not change `theta(z)^T q_bar`; absolute slopes are not uniquely determined. A reference-category or sum-to-zero convention can make coefficients reportable, but it does not create new information.

Independent fits for correlated treatment coordinates do not generally add to the joint effect. For two weights, `q_bar_2=-q_bar_1`. If `Y_bar=a q_bar_1`, either individual regression predicts all of `Y_bar`; summing gives `2Y_bar`. Correlation with the joint fit can remain one despite this scale error.

Check whether reported `R^2` values concern the original outcome, its residuals, or a maximum across separate fits. Different denominators or model selections do not constitute an additive causal variance decomposition.

## 6. Causal and support conditions

State each condition for the actual treatment variable and intervention:

- **Consistency/exposure sufficiency:** different underlying neighborhood configurations mapped to the same exposure must have the same relevant potential outcome, or the exposure has hidden versions.
- **Interference:** specify whether another unit can affect the outcome outside the chosen exposure summary. A spatial model needs an explicit exposure mapping or interference structure.
- **Exchangeability:** for each fixed treatment value `q`, `Y(q)` is independent of assigned `Q` conditional on the adjustment set. An outcome-derived embedding is not automatically a sufficient pretreatment adjustment set.
- **Overlap:** compared treatment values must lie in conditional support. For continuous treatments, use densities or neighborhood support on the correct-dimensional space; positive probability at one exact point is usually the wrong condition.

For regression on simplex treatments, the ambient conditional covariance is singular by construction. Check variability on the tangent/contrast space instead of demanding full rank in all `a` coordinates. Rank deficiency beyond the simplex constraint prevents some comparisons.

Label-based positivity scores are proxies, not certificates. Document their conditional probability direction, filtering population, group size, and thresholds. A coarse label can hide within-group lack of overlap. Neither a low positivity score nor a good representation benchmark establishes exchangeability or consistency.
