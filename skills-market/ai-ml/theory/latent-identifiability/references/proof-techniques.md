# Proof techniques for latent identifiability

Use the sections that match the model. The derivations below are reusable mathematical arguments, not a claim that one cited paper proves every variant. Bibliographic keys refer to [the reference map](reference-map.md).

## A. Fix the quotient before proving uniqueness

Let `M` be an admissible model class and `O(theta)` its observable probability law. Identification of a functional `tau` means

\[
O(\theta)=O(\tilde\theta)\Rightarrow\tau(\theta)=\tau(\tilde\theta).
\]

Identification up to a group action means equality of observable laws implies membership in the same orbit. Check that the transformations preserve admissibility, and that the proposed relation is actually an equivalence relation. Distinguish an arbitrary invertible transformation, blockwise transformations, componentwise transformations, and a permutation/sign ambiguity.

For nonlinear decoders, a starting attack is `W_tilde=T(W)`, `f_tilde=f o T^{-1}`. The transformed prior must also remain admissible. With an isotropic Gaussian prior, any orthogonal rotation preserves the prior; if block mixing is allowed, marginal likelihood cannot assign semantic names to those blocks. This exact symmetry is stronger evidence than similar training losses. See [HP99], [LOC19].

## B. Remove the observation kernel at the distribution level

Write `X|R ~ K_eta(.|R)`, `R=f(W)`. The needed implication is injectivity of the mixture operator:

\[
\int K_\eta(dx\mid r)\,dP_R(r)
=\int K_\eta(dx\mid r)\,dP_{\tilde R}(r)
\Rightarrow P_R=P_{\tilde R}.
\]

This is not pointwise denoising. If `eta` is unknown or differs between candidate models, the same-kernel argument does not apply without an additional identification step.

### Negative-binomial factorial moments

Assume conditionally independent coordinates, known shapes `r_j>0`, and means `R_j>=0`. Define the falling factorial `(X)_m=X(X-1)...(X-m+1)`. Then

\[
\mathbb E[(X_j)_m\mid R_j]
=c_{jm}R_j^m,\qquad
c_{jm}=\prod_{\ell=0}^{m-1}(1+\ell/r_j)>0.
\]

Consequently,

\[
\mathbb E\left[\prod_j(X_j)_{m_j}\right]
=\left(\prod_jc_{jm_j}\right)
\mathbb E\left[\prod_jR_j^{m_j}\right].
\]

Equality of count laws identifies all mixed moments of `R` when finite. The alternative model's moments must also be justified, not assumed from the true model without argument. Here the nonnegative factorial-moment identity and equality of count laws transfer their finiteness.

Equality of all moments needs a determinacy condition before it implies equality in distribution. One sufficient condition for every coordinate is

\[
\sum_{m\ge1}\mathbb E[R_j^{2m}]^{-1/(2m)}=\infty.
\]

For example, `E[R_j^(2m)] <= C D^(2m)(2m)^(2m)` implies divergence by comparison with the harmonic series. Coordinatewise moment determinacy, together with the complete mixed moment sequence, yields joint determinacy under the standard multivariate moment result. Merely matching marginal laws does not determine dependence. See [LIN17], [PET82], and SIMVI Lemma 1 [SIMVI25].

Do not require this particular moment condition when another injectivity proof works. Its failure leaves this proof route unavailable; it does not establish nonidentifiability. A lognormal signal has all positive moments but need not be determined by them. Poisson kernels admit the simpler identity `E[(X_j)_m|R_j]=R_j^m`.

### Additive noise

If `X=R+epsilon`, noise is independent of `R`, and its known characteristic function is nowhere zero, then

\[
\varphi_X(t)=\varphi_R(t)\varphi_\epsilon(t)
\]

identifies `varphi_R` by division. Some theorems allow a smaller zero set with additional reasoning; verify their exact condition rather than replacing it by an informal deconvolution claim. Unknown noise can trade off against latent variation.

## C. Compare two latent coordinate systems

If `f:W->P` and `f_tilde:W_tilde->P` are diffeomorphisms onto the same signal manifold, define

\[
T=\tilde f^{-1}\circ f.
\]

Signal-law equality gives `T(W)` the candidate latent law and, in equal-dimensional latent coordinates,

\[
p_W(w)=p_{\tilde W}(T(w))\,|\det DT(w)|.
\]

When `p>d`, do not apply a square determinant to the ambient decoder Jacobian. Work with `T` between `d`-dimensional coordinates or use the appropriate manifold volume formula. Also justify the common image/manifold: equality of signal laws alone need not identify unvisited decoder regions.

If the density identity initially holds almost everywhere, continuity on an open domain can extend it pointwise: a continuous nonzero difference at a point persists on an open set of positive measure. Restrict this argument to the support where the relevant densities and maps exist. Derivatives require the corresponding regularity.

## D. Prove block separation before claiming it

For `w=(z,s)`, write `T=(T_z,T_s)`. Sufficient support or structural assumptions can force `D_s T_z=0` or `D_z T_s=0`. These zero blocks do not follow from reconstruction accuracy.

A SIMVI-style fiber argument works as follows. Let `h=f^{-1} o f_tilde`. If, for every compatible pair `(z,z_tilde)`, fixing those two values still permits every `s_tilde`, then `h_z(z_tilde,s_tilde)=z` for every `s_tilde`. Thus `z=F(z_tilde)`. A dual fiber condition gives `s_tilde=H(s)`.

State these strong hypotheses as restrictions on the relation between representations. Full marginal support, or full support separately conditional on either of two variables, does not imply full support conditional on both. Use this argument only if the model or an earlier lemma justifies the fiber condition; otherwise block separation remains the open lemma.

### Dimension and local inversion

A smooth surjection `F:R^m->R^n` cannot exist when `m<n`: all points are critical and Sard's theorem would make its image measure zero. This argument needs the theorem's differentiability assumptions; continuous space-filling maps show why continuity alone is insufficient. If another premise gives `m<=n`, then `m=n`. See [SARD42], [LEE12].

Once block sizes match, an everywhere invertible block-triangular Jacobian implies its square diagonal blocks are invertible. The inverse function theorem then gives local inverses. It does not alone give a global inverse. In a particular problem, stronger product structure may yield global bijectivity; prove that separately.

## E. Use conditional Gaussian contrasts to identify a block affinely

Assume separation has already been proved. In a common local chart write

\[
\tilde z=G(z),\quad\tilde s=H(s),\quad
|\det DT(z,s)|=h_z(z)h_s(s).
\]

Assume both models have conditional laws

\[
s\mid z\sim N(Bz,V),\qquad
\tilde s\mid\tilde z\sim N(\tilde B\tilde z,\tilde V),
\]

with fixed positive-definite `V,V_tilde`, and `B` has full row rank `d_s`. Conditional covariances must be independent of the conditioning value for the following cancellation.

The log-density identity is

\[
\log p_Z(z)+\log p(s\mid z)
=\log p_{\tilde Z}(G(z))+\log p(H(s)\mid G(z))
+\log h_z(z)+\log h_s(s).
\]

Choose a right inverse `B^dagger` and nearby points

\[
z_i=z_0+\varepsilon B^\dagger e_i,
\quad B(z_i-z_0)=\varepsilon e_i.
\]

Choose `epsilon` small enough that all points lie in one valid chart for a common open set of `s`. Subtract the equation at `z_0` from that at `z_i`. Terms quadratic in `s`, quadratic in `H(s)`, conditional log determinants, and `log h_s(s)` cancel. The result has the form

\[
\varepsilon e_i^\top V^{-1}s
=\{\tilde B[G(z_i)-G(z_0)]\}^\top
\tilde V^{-1}H(s)+b_i.
\]

Stacking yields `epsilon V^{-1}s=M H(s)+b`, hence

\[
s=L H(s)+c.
\]

`L` is invertible because otherwise its affine image could not contain an open subset of `R^{d_s}`. No full-rank assumption on the candidate contrast matrix should be smuggled in if invertibility is obtained this way. The constant terms can absorb `log p_Z(z_i)`; the essential contrast uses the conditional family and the separated Jacobian.

If `rank(B)<d_s`, this construction cannot recover every direction. It may identify only some contrasts, but do not claim an identified projection without analyzing remaining symmetries. If `V=V(z)`, quadratic terms survive; a sufficient-statistic argument may be needed instead.

## F. Conditional exponential-family alternative

For genuinely available conditioning information `u`, consider

\[
\log p(w\mid u)=a(w)+\lambda(u)^\top T(w)-\log Z(u).
\]

After a justified noise-removal step, suppose two models are related by a coordinate map independent of `u`. Subtract the log-density identity at `u_0` from identities at other `u_i`. Base-measure and log-Jacobian terms cancel. A full-rank matrix of parameter contrasts can then constrain sufficient-statistic vectors affinely. Additional conditions are needed to restrict that ambiguity to block or component permutations.

This route explains why multiple environments or auxiliary measurements can identify otherwise ambiguous representations. The number of linearly independent contrasts concerns the sufficient-statistic dimension, not automatically the raw latent dimension. An encoder estimate of an unobserved `u` does not qualify as external supervision without another identification argument. Consult [IVA20] and [HYV19] for exact theorem conditions; do not substitute their conclusions for the missing premises in a new model.

## G. Glue local results and state the remaining geometry

If two affine formulas agree on a nonempty open overlap, their coefficients agree: subtract their values at a point and at small coordinate perturbations. On a connected domain, overlapping neighborhoods propagate the same coefficients globally. On disconnected support, unrelated transformations can remain on separate components.

Nonsingular Jacobians alone do not rule out global covering or branch ambiguity. Use connectedness for gluing already-established local constants, not as a generic proof that every local diffeomorphism is injective.

If `s=L s_tilde+c` and both random blocks have exactly zero mean and identity covariance, then `c=0` and `LL^T=I`. Without this standardization, affine identification preserves affine relations and convex combinations, not Euclidean distance. Posterior means need not have the covariance of the underlying latent variable.

## H. Probe failure with exact toy constructions

- **Gaussian rotation:** two independent standard Gaussian coordinates admit a nontrivial orthogonal mixing and compensating decoder with the same observation law.
- **Dependent normalizer:** if `p(pi|z)` is proportional to `U(z^pi)`, its normalizer is `sum_sigma U(z^sigma)`, generally a function of `z`.
- **Insufficient rank:** choose a conditional mean that varies along only one of two latent directions; inspect transformations of the other direction.
- **Local versus global:** `(x,y) -> (exp(x)cos(y),exp(x)sin(y))` has nonzero Jacobian determinant but is not globally injective.
- **Statistical independence versus semantics:** uncorrelated is not independent in general; independent coordinates need not have the intended semantic grouping.

For each toy case check the entire retained model class. A counterexample to one asserted implication is not automatically a counterexample to a differently restricted theorem.
