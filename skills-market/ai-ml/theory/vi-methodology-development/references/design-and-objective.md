# Design and objective reference

Use this for a new model, mathematical review, or a change to the likelihood, latent structure, or objective. The constructions below are reusable examples and derivations, not claims that the three seed papers use one common model.

## 1. Define the inferential question

Write one sentence of the form: “Given information A available at use time, estimate B for units C, with uncertainty D, under generalization setting E.” Separate population-level scientific replication from the number of rows used for optimization.

Record training, validation, test, and deployment access for values, labels, contexts, relationships, and preprocessing statistics. Test observations may legitimately enter their inference encoder in representation learning; a withheld prediction target may not. A method using an entire fixed unlabeled graph is transductive unless it specifies how to handle new nodes or graphs.

For each latent block ask what observation would distinguish its role from another block. Consider rotations, scale tradeoffs, component permutation, signal/nuisance substitution, and unobserved confounding. An empirically useful representation can be defensible without unique semantic coordinates; state that weaker target when appropriate. Unsupervised disentanglement requires substantive inductive assumptions; naming coordinates is insufficient ([Locatello et al., 2019](https://proceedings.mlr.press/v97/locatello19a.html)).

## 2. Select the observation model

| Data property | Candidate modeling move | Decision to justify |
|---|---|---|
| Counts with known exposure | Poisson or overdispersed count likelihood with an offset | Raw-count support, mean–variance relation, exposure definition |
| Continuous transformed values | Gaussian, heavy-tailed, or heteroscedastic likelihood | Transformation, residual scale, outliers, support |
| Positive or bounded values | Positive-support or bounded likelihood, or a justified transform | Boundary values, censoring, saturation |
| Excess zeros | Compare ordinary sampling zeros, censoring, hurdle, or zero inflation | Mechanistic or predictive evidence for the extra component |
| Multiple measurement sources | Explicit source composition or latent allocation | Whether sources add, select one component, or alter detection |
| Missing features/modalities | Observed-data likelihood with an explicit mask | Missingness mechanism, bridge information, identifiability |
| Known measurement conditions | Conditional likelihood or hierarchical observation parameters | Overlap across conditions and target preservation |

An encoder may consume standardized or log-transformed values while the likelihood scores raw observations. State both scales. If scoring densities on an invertible transformed scale, use the Jacobian when reporting original-scale densities; a fixed transform's Jacobian may be constant for fitting but still matters for cross-model comparison. Clipping, quantile maps with ties, and many normalizations are not simply invertible changes of variables.

For conditionally independent features under ignorable missingness,

\[
\log p_\theta(x_{i,\mathrm{obs}}\mid z_i,c_i)
=\sum_{j:m_{ij}=1}\log p_\theta(x_{ij}\mid z_i,c_i).
\]

This is an observed-data likelihood, not evidence that missing entries equal zero. For a coupled multivariate likelihood, marginalize missing coordinates correctly; masking arbitrary terms need not give the correct marginal. If observation depends on unobserved values after conditioning, consider a joint missingness model or sensitivity analysis. A decoder cannot identify a disconnected feature panel merely by allocating an output neuron to it.

## 3. Write the joint distribution before networks

One hierarchical *example* uses global random variables \(g\), unit-specific target state \(z_i\), nuisance state \(u_i\), observed covariates \(c_i\), and fixed parameters \(\theta\):

\[
p_\theta(g,Z,U,X_{\rm obs}\mid C)
=p_\theta(g)\prod_i p_\theta(z_i\mid g,c_i)
 p_\theta(u_i\mid z_i,g,c_i)
 p_\theta(x_{i,\rm obs}\mid z_i,u_i,g,c_i).
\]

Remove unnecessary blocks. Conditioning \(u_i\) on \(z_i\) explicitly permits dependence; independent priors are an alternative assumption, not a universal principle. Deterministic decoder outputs are not extra random variables requiring KL penalties. If \(g\) is estimated as a parameter instead, do not retain a fictitious variational entropy for it.

For relationships \(A\), distinguish:

- conditioning the generative model on \(A\), such as a normalized prior \(p(Z\mid A)\);
- conditioning only an inference network on \(A\);
- adding a graph penalty to the training objective.

These impose different models. Graph, temporal, or cross-unit likelihood factors can invalidate the independent-unit product above. Write their actual factors and normalization; an arbitrary product of cyclic conditionals is not automatically a normalized joint.

Separate a source-sum observation model
\(x\sim\mathrm{Poisson}(\lambda_1+\lambda_2)\)
from a distribution mixture
\(p(x)=\pi p_1(x)+(1-\pi)p_2(x)\).
The first adds intensities; the second samples a component. For every simplex state its axis and normalization; for every distribution state whether a parameter is a variance, standard deviation, rate, scale, mean, or inverse dispersion.

## 4. Specify inference independently

A possible family for the example above is

\[
q_\phi(g,Z,U\mid X_{\rm obs},C,M)
=q_\phi(g)\prod_i q_\phi(z_i\mid I_i)
 q_\phi(u_i\mid z_i,g,I_i),
\]

where \(I_i\) lists available inference inputs and \(M\) is the observation mask. Amortization means sharing a learned mapping from \(I_i\) to posterior parameters, not making the underlying latent variable global.

| Choice | Use when | Cost or limitation |
|---|---|---|
| Amortized local posterior | Many similar units and rapid new-unit inference | Restricted inference mapping; inspect amortization error |
| Per-unit variational parameters | Local ambiguity or reusable fitted units | Memory and explicit new-unit optimization |
| Global variational posterior | Shared unknown quantities need uncertainty | Correct scaling and global dependence |
| Structured conditional posterior | Important posterior dependence is missed | More coupled sampling and computation |
| Hybrid amortized + local refinement | Fast initial inference plus difficult units | Define refinement budget and fair evaluation |
| Point estimate / MAP for selected quantities | Uncertainty there is not required or approximation is deliberate | Exported uncertainty is conditional on these estimates |

Start simple. Test a richer family, local refinement, or a small reference posterior only if uncertainty or optimization evidence warrants it. A mixture prior does not imply a mixture variational posterior. Delta/MAP estimates are not ordinary continuous variational densities with a finite KL to a continuous prior; describe the MAP/hybrid objective and its uncertainty limitations explicitly.

For continuous reparameterizable variables use a pathwise estimator; for discrete variables consider exact enumeration/marginalization when tractable, or document a score-function or relaxed estimator. A relaxation changes the estimator or modeled latent object and needs an explicit interpretation. [Kingma and Welling](https://arxiv.org/html/1312.6114v11), sections 2–3, present amortized VAE inference using a reparameterized ELBO estimator.

## 5. Derive the bound and the implemented objective

Let \(H\) collect random unknowns. Suppressing fixed observed conditioning information for readability,

\[
\mathcal L=\mathbb E_q[\log p_\theta(X_{\rm obs},H)-\log q_\phi(H)],\qquad
\log p_\theta(X_{\rm obs})=\mathcal L+
\mathrm{KL}(q_\phi(H)\Vert p_\theta(H\mid X_{\rm obs})).
\]

This identity states the target, direction of KL, and bound interpretation ([Blei et al., 2017](https://arxiv.org/html/1601.00670v9), section 2). Derive the terms for the actual factorization rather than importing “reconstruction + KL” by analogy.

For the hierarchical example and variational family above,

\[
\begin{aligned}
\mathcal L={}&-\mathrm{KL}(q(g)\Vert p(g))\\
&+\sum_i\mathbb E_q[\log p(x_{i,\rm obs}\mid z_i,u_i,g,c_i)]\\
&-\sum_i\mathbb E_{q(g)}\mathrm{KL}(q(z_i\mid I_i)\Vert p(z_i\mid g,c_i))\\
&-\sum_i\mathbb E_{q(g)q(z_i\mid I_i)}
\mathrm{KL}(q(u_i\mid z_i,g,I_i)\Vert p(u_i\mid z_i,g,c_i)).
\end{aligned}
\]

Conditional KL terms require the outer expectation over their parents. Closed-form KLs are convenient, not required. A mixture-prior KL often needs Monte Carlo evaluation of the mixture log density via log-sum-exp.

Maintain a loss ledger with term, mathematical origin, sign, tensor shape, reductions, coefficient/schedule, and parameters receiving gradients. Write a minimization objective explicitly, for example

\[
J=-\mathcal L+\lambda_{\rm dep}R_{\rm dep}
+\lambda_{\rm sup}R_{\rm sup}+\lambda_{\rm aux}R_{\rm aux}.
\]

These penalties are examples, not default ingredients. An adversary may require separate opposing optimizer objectives rather than this single minimization. A supervised term can be part of a probabilistic model if derived as such; otherwise label it auxiliary. A prior on a point-estimated parameter contributes a MAP penalty. Weight decay is not automatically a scientifically specified prior.

KL warmup, free bits, rescaled KLs, stop-gradient paths, and substituted priors must be documented. They do not automatically implement the canonical ELBO of the written joint. Some weighted objectives remain lower bounds under additional conditions; establish that claim instead of declaring all modified objectives either valid or invalid. Log a canonical evaluation objective separately when it is available.

For uniformly sampled minibatches \(B\) of a model with conditionally independent local factors given its globals,

\[
\widehat{\mathcal L}=\frac{N}{|B|}\sum_{i\in B}\mathcal L_i
-\mathrm{KL}(q(g)\Vert p(g)).
\]

Equivalently, divide the whole expression by \(N\): average local terms and use global KL divided by \(N\). Do not scale global KL as if it occurred once per observation. Nonuniform samples, oversampling, graph neighborhoods, and group-balanced batches require their own weighting argument. Stochastic VI separates local and global updates ([Hoffman et al., 2013](https://jmlr.org/papers/v14/hoffman13a.html)).

For held-out density evaluation an optional importance-weighted estimator is
\(\log[ K^{-1}\sum_k p(x,z^{(k)})/q(z^{(k)}\mid x)]\), evaluated with log-sum-exp. Its expectation gives the IWAE bound under its assumptions, not an exact finite-sample log likelihood. Extra samples do not establish calibration or identifiability ([Burda et al.](https://arxiv.org/html/1509.00519v4), section 3).

## 6. Define outputs as posterior queries

Distinguish:

- **Latent summary:** posterior mean/sample of a specified block, with coordinate ambiguity acknowledged.
- **Denoised signal:** expectation or samples of a defined signal variable, not automatically the observed likelihood mean.
- **Posterior predictive measurement:** draw latent quantities and then observation noise; this differs from uncertainty in a conditional mean.
- **Condition-standardized decoding:** infer a unit, then decode at a specified reference covariate or average over a stated reference distribution.
- **Missing-value prediction:** integrate the model's conditional distribution given actually observed features and covariates.
- **Population contrast:** define groups, aggregation/replication unit, effect scale, reference covariates, uncertainty, and any multiple-testing decision.

Condition-switched decoding is a model-based standardized prediction. A causal intervention claim additionally needs the relevant causal assumptions and support. A standard VAE with fitted decoder weights does not include full parameter uncertainty merely because latent variables are sampled.

For new units, specify whether shared/global latent posteriors are frozen, updated with new observations, or propagated forward in time, and what data may inform each operation. Freezing a reference posterior can be a useful modular approximation; do not describe it as the full joint posterior update. Preserve shared latent draws when reporting joint predictive dependence across units.

## 7. Portable example

For repeated sensor readings from different instruments, the target may be a latent physical state; manufacturer and physical-instrument IDs are observed; device-specific drift is latent nuisance; missing channels form a mask. Manufacturer effects and individual-device drift occupy different levels. First try a conditional measurement model with one state block. Add drift only if crossed measurements or calibration anchors can distinguish it from state: repeated readings from one object on one aging device may leave them confounded. Use overlap among instruments to assess standardization and leave instruments or independent experiments out only when that matches the intended deployment. This transfers the papers' modeling logic without importing cells, spatial graphs, negative-binomial counts, or antibody panels.
