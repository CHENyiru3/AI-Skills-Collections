# SIMVI: a worked proof architecture and its boundaries

Source: Dong et al. (2025), *SIMVI disentangles intrinsic and spatial-induced cellular states in spatial omics data*, Supplementary Information, `41467_2025_58089_MOESM1_ESM.pdf`, pp. 3-19. See [SIMVI25 in the reference map](reference-map.md). Page numbers below are PDF page numbers. This reconstruction uses the supplied supplement; no machine-specific attachment path is required to use the skill.

Statements labeled **paper** describe the supplement. Statements labeled **audit** are mathematical checks developed for this skill, not published errata. Retain that distinction when reusing them. The general method is in [proof techniques](proof-techniques.md).

## 1. Model and identification target

**Paper, pp. 3-5, Eqs. 1-13.** An initial iid Gaussian bag of intrinsic states is allocated to a spatial graph by a state-dependent permutation. Spatial states are generated from neighboring intrinsic states, and expression counts from both blocks:

\[
s=A z_N+\epsilon_s,\quad\epsilon_s\sim N(0,\Sigma_s),
\qquad X\mid z,s\sim\operatorname{NB}(f(z,s),g).
\]

The proof uses the stationary local Gaussian law

\[
\begin{pmatrix}z\\z_N\end{pmatrix}
\sim N\!\left(0,
\begin{pmatrix}I&\Sigma_1^\top\\\Sigma_1&\Sigma_0\end{pmatrix}\right).
\]

Conditioning and marginalizing the neighborhood yields

\[
s\mid z\sim N(A'z,\Sigma'),\qquad
A'=A\Sigma_1,\quad
\Sigma'=\Sigma_s+A(\Sigma_0-\Sigma_1\Sigma_1^\top)A^\top.
\]

The allowed decoder is a smooth bijection onto its signal image with smooth inverse; dispersion is fixed and known. Candidates have the same signal image and total latent dimension, but may initially allocate different dimensions to the two blocks. Observational equivalence is equality of the *single-cell* count law. The target is

\[
\tilde d_z=d_z,\quad\tilde d_s=d_s,
\qquad z=F(\tilde z),\quad s=L\tilde s+c,
\]

with `F` smooth and locally invertible as established in the theorem, and `L` invertible. It is not coordinatewise semantic recovery or unique recovery of all graph mechanisms.

## 2. Assumption-to-lemma map

| Premise | Exact role | Transfer question |
|---|---|---|
| A1: controlled even moments of each mean coordinate | Moment determinacy in Lemma 1 | Does the new observation kernel identify its mixing law? |
| A2: `d_z>=d_s`, `rank(A Sigma_1)=d_s` | Independent conditional-mean contrasts in Theorem 1 | What varies every direction of the target sufficient statistic? |
| A3(i): for each compatible `(z,z_tilde)`, `s_tilde` spans its entire space | Lemma 2: true intrinsic state is a function of inferred intrinsic state alone | Is this fiber condition justified rather than assumed to remove mixing? |
| A3(ii): for each compatible `(s,s_tilde)`, `z` spans its entire space | Lemma 3: inferred spatial state is a function of true spatial state alone | Can an alternative block still depend on the other true block? |
| A4: every candidate has `d_z_tilde<=d_z` | With the lower dimension bound, proves matching block dimensions | Is minimal dimension an actual constraint or merely a penalty analogy? |

The cross-representation quantifiers in A3 and A4 are central. Their satisfaction by the true model does not prove their satisfaction by every observationally equivalent candidate. Define the restricted candidate family explicitly when reusing this theorem shape.

## 3. Reconstruct the lemma chain

**Lemma 1, pp. 6-8, Eqs. 14-25.** Fixed-dispersion NB raw moments are triangular polynomials in the random mean. Equal count laws imply equal mixed mean moments; A1 and a multivariate moment theorem identify the mean distribution. The factorial-moment derivation in the technique reference is a shorter route to the same intermediate conclusion.

**Lemma 2, pp. 8-9, Eqs. 26-33.** Apply A3(i) to `h_z=f_z^{-1} o f_tilde`. Varying `s_tilde` cannot change `z`, so `z=F(z_tilde)`. A smooth surjection onto the true intrinsic space gives `d_z_tilde>=d_z` by Sard's theorem. A4 gives equality. Equal total dimension then gives equal spatial dimensions.

**Lemma 3, pp. 9-10, Eqs. 34-40.** Apply A3(ii) to `T_s=f_tilde_s^{-1} o f`; varying `z` cannot change `s_tilde`. Thus `s_tilde=H(s)`. The direction matters: the lemma alone has not proved a global affine inverse.

**Lemma 4, pp. 10-11, Eqs. 41-43.** An equivalence relation shared by overlapping open neighborhoods propagates across connected Euclidean space. This is a gluing tool, not an inference theorem.

**Theorem 1, pp. 11-16, Eqs. 44-74.**

1. Use the invertible block-triangular Jacobian of `h` to show `DF` is nonsingular.
2. Work in a local inverse chart for `F`, where the Jacobian volume separates into a `z` factor and an `s` factor.
3. Select `z_i=z_0+epsilon A'^dagger e_i` inside that chart.
4. Compare log-density identities at `z_i` and `z_0` for the same `s`. Fixed-covariance Gaussian quadratic terms and the spatial Jacobian factor cancel. Full row rank produces `s=L_local H(s)+c_local`; open support forces `L_local` invertible.
5. On overlapping neighborhoods the affine coefficients agree. Lemma 4 makes them global.

The transferable insight is not “a VAE is identifiable.” It is: **establish the signal law and block structure first; then use rich conditional distribution changes to restrict the remaining coordinate freedom.** Here those changes come from statistical dependence induced by the spatial model. The intrinsic block is not an externally observed auxiliary label.

## 4. Audit the model before borrowing the proof

**Audit: the permutation normalizer, Eqs. 1-6.** If

\[
p(\pi\mid z)=U_G(z^\pi)/Z(z),\qquad
Z(z)=\sum_\sigma U_G(z^\sigma),
\]

then for iid permutation-invariant bag density `p_0`, the assigned vector `y` has density

\[
p(y)=\frac{n!p_0(y)U_G(y)}{\sum_\sigma U_G(y^\sigma)}.
\]

The denominator cannot generally be dropped. On the complete three-node graph, a homogeneous pairwise potential is invariant under permutations: the assignment is uniform and the output remains iid, whereas multiplication of `p_0` by a nonconstant Gaussian pair potential changes the law. This is a counterexample to that generative implication, not to a theorem that directly assumes the local Gaussian law. A clean transfer can postulate the latter explicitly and audit its scientific justification.

**Audit: covariance and stationarity.** A precision matrix `I+W tensor Omega` must define a valid symmetric positive-definite quadratic form. Its inverse does not generally have identity diagonal blocks. A regular graph does not alone imply identical node-neighborhood distributions. These are compatibility issues, not consequences of equal node degrees.

**Audit: dimension scope.** A shared signal manifold and diffeomorphic decoders already fix total dimension. The theorem does not show that training selects the correct total latent dimension from arbitrary architectures.

**Audit: geometry.** Affine identification alone preserves convex structure, not Euclidean distances. If both spatial latent laws are *exactly* `N(0,I)`, then `c=0` and `LL^T=I`; this stronger normalization yields orthogonal ambiguity. It does not automatically hold for posterior means.

**Audit: notation versus structural issues.** The Gaussian log-density constants in Eqs. 58-60 require `log det(Sigma')`, and the candidate contrast coefficients require the candidate covariance inverse. Repairing these algebraic notations retains the contrast strategy. Do not equate such repairs with justification of the permutation derivation or architecture correspondence.

## 5. Mapping to VAE design is a separate bridge

**Paper, Section 1.4, pp. 16-17, Eqs. 75-76.** Intrinsic latents use a per-cell encoder; spatial latents use a graph encoder over neighboring intrinsic encoder means:

\[
q_\phi(\tilde z_i\mid x_i)=N(\phi_1(x_i),\phi_2(x_i)),
\]
\[
q_\psi(\tilde s_i\mid x_{N(i)})
=N(\psi_1(\phi_1(x_{N(i)})),\psi_2(\phi_1(x_{N(i)}))).
\]

**Audit.** Adaptive graph attention is not generally a fixed linear map `A`; predicted variances need not be constant. A posterior mean approximating neighborhood contribution is not the full latent `Az_N+epsilon_s`. A Gaussian variational draw's full support does not prove A3's deterministic fiber conditions. A fixed latent dimension with an information penalty does not implement A4's minimization over candidate dimensions.

The true model permits, and A2 requires, nonzero cross-covariance. If exact separation holds, making both recovered blocks independent would make their separate functions independent too. Thus complete removal of dependence conflicts with recovery of correlated true blocks. A finite asymmetric penalty can be a useful inductive bias, but it is not evidence that exact independence or the theorem assumptions have been achieved.

## 6. Downstream spatial effects introduce another target

**Paper, Section 2, pp. 17-19, Eqs. 77-84.** Spatial states are converted to simplex-valued archetype weights. Outcome and treatment weights are residualized against intrinsic state, then regressed with state-dependent slopes.

**Audit.** The resulting term is naturally `theta(z)^T[q-E(q|z)]`, not automatically the fixed-reference contrast `theta(z)^T(q-q_0)`. The zero weight vector is outside the simplex. Separate per-archetype regressions can count the same signal repeatedly. Causal identification additionally needs well-defined interventions, sufficient exposure summaries, conditional exchangeability, and support overlap. Neither the representation theorem nor a positivity proxy proves those conditions.

Use [implementation and estimands](implementation-and-estimands.md) for the reusable derivations. Do not treat spatial-effect estimation as part of the conclusion of Theorem 1.
