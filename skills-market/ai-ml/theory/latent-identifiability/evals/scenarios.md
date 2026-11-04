# Behavioral evaluation scenarios

These are maintenance scenarios, not a claimed completed independent evaluation. Run them in a scratch workspace when changing the skill's behavior. Give an evaluator the prompt and skill only; keep the checks below for scoring. Report whether an evaluation was self-review or independent. No retraining or external writes are needed.

## 1. Gaussian blocks with semantic names

Prompt: “My decoder is an arbitrary smooth diffeomorphism of two independent standard Gaussian scalar latents, named cell type and environment. Counts have a known Poisson mean given by the decoder. We only observe the count marginal. Prove the two named factors are uniquely recovered.”

Checks: construct a nontrivial orthogonal mixing, transform the decoder, preserve the prior and count law exactly, and reject unique semantic recovery. Do not treat independence or the names as identifying supervision. Offer an explicitly weaker quotient or additional scientifically motivated information.

## 2. A viable conditional Gaussian proof

Prompt: “Block separation is already proved: in a local chart z_tilde=G(z), s_tilde=H(s), and the coordinate Jacobian determinant factors. Both conditional spatial laws are Gaussian with fixed positive-definite covariance, their means are Bz and B_tilde z_tilde, and B has full row rank. Equal observable laws have already been shown to imply equal signal laws. Derive affine identification of s and explain the global step.”

Checks: choose a right inverse and common chart, form d_s+1 conditioning points, subtract log-density identities, cancel the correct terms, establish invertibility from open support, and require overlapping neighborhoods/connectedness for global coefficients. Do not merely cite SIMVI or stop at a plan.

## 3. Soft penalties claimed to enforce support

Prompt: “Our VAE's Gaussian posteriors have positive variance and we penalize mutual information. Therefore all SIMVI assumptions hold and the posterior means recover the true correlated intrinsic and spatial states. Please write the theorem.”

Checks: distinguish random draws from means and inverse coordinates; identify cross-representation fiber and dimension gaps; address true dependence versus exact inferred independence; retain a conditional claim or explicit gap. Do not certify the original statement from the loss alone.

## 4. Residualized simplex treatments

Prompt: “Two environment weights sum to one. We regress each weight and expression on the same covariates with intercepts, fit the two residual regressions separately, and sum their predictions. Prove this equals the effect relative to zero environment.”

Checks: zero is outside the simplex; residuals sum to zero; the estimand is centered; exhibit a duplicate-signal counterexample. Do not assume causal exchangeability from a learned representation or equate high correlation with matching effect scales.

## 5. State-dependent spatial allocation

Prompt: “Draw an iid Gaussian bag z, then choose pi with probability proportional to U(z^pi). Show the assigned field has density proportional to p0(y)U(y), and use this to obtain a correlated Gaussian field on a complete three-node graph.”

Checks: retain the z-dependent normalizer, derive the permutation sum, and use permutation-invariance of the complete-graph potential to test the asserted implication. Distinguish a broken construction from a separately postulated Gaussian model.

## 6. Sparse starting information

Prompt: “I want to prove my spatial multi-omics model disentangles cell state and environment. It has two encoders and reconstructs both modalities well. What can we prove?”

Checks: identify the missing observation scheme, coupling, model class, target symmetry, and identifying information; make useful provisional progress without inventing those premises. Ask for only the consequential missing details. Do not demand unavailable router skills or a full manuscript before beginning.

## 7. Moment route fails

Prompt: “The latent Poisson mean is lognormal. All moments exist, so matching every count moment proves the latent-mean law is unique. Audit this proof.”

Checks: distinguish moment existence from determinacy, reject the stated inference, and avoid concluding that the Poisson mixture itself must be nonidentifiable. Suggest a transform-based mixture-injectivity argument as a separate route to investigate.
