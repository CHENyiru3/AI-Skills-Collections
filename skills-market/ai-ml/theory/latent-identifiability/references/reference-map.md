# Reference map by proof obligation

Use primary sources to verify a result before importing it. The access notes below distinguish checked theorem statements from bibliographic verification; they do not certify an entire paper or its applicability to a new model. Links and metadata were checked on 2026-10-26 unless indicated otherwise. No external full texts are redistributed in this skill.

## Identification architecture

**[SIMVI25]** Dong, M., Su, D. G., Kluger, H., Fan, R., and Kluger, Y. (2025). *SIMVI disentangles intrinsic and spatial-induced cellular states in spatial omics data*. Nature Communications 16, 2990. [Publisher and supplementary files](https://www.nature.com/articles/s41467-025-58089-7). DOI: `10.1038/s41467-025-58089-7`.

- Use: two-block proof architecture; NB signal-law identification; support/dimension lemmas; conditional Gaussian contrasts; local-to-global gluing.
- Checked: supplied supplementary PDF `41467_2025_58089_MOESM1_ESM.pdf`, pp. 3-19. Definitions 1-3 p. 5; assumptions pp. 5-6; Lemmas 1-4 pp. 6-11; Theorem 1 pp. 11-16; architecture pp. 16-17; effects pp. 17-19.
- Boundary: the [case study](simvi-case-study.md) distinguishes the paper's claims from independent audit calculations. Do not cite the latter as an author correction.

**[IVA20]** Khemakhem, I., Kingma, D., Monti, R., and Hyvarinen, A. (2020). *Variational Autoencoders and Nonlinear ICA: A Unifying Framework*. PMLR 108, 2207-2217. [Proceedings](https://proceedings.mlr.press/v108/khemakhem20a.html), [paper](https://proceedings.mlr.press/v108/khemakhem20a/khemakhem20a.pdf).

- Use: conditional exponential-family identification and explicit separation of identification from estimation.
- Checked: Section 4, Theorem 1, subsequent ambiguity restrictions, and Theorem 4 statements (PDF pp. 5-6). Theorem 1 concerns an affine ambiguity of sufficient statistics, not automatic semantic coordinate recovery. Theorem 4 has ideal posterior-family and optimization premises.
- Boundary: observed auxiliary information and sufficient variability cannot be replaced by an unverified learned latent. Read the supplement before adapting its proof.

**[HYV19]** Hyvarinen, A., Sasaki, H., and Turner, R. (2019). *Nonlinear ICA Using Auxiliary Variables and Generalized Contrastive Learning*. PMLR 89, 859-868. [Proceedings](https://proceedings.mlr.press/v89/hyvarinen19a.html), [supplement](https://proceedings.mlr.press/v89/hyvarinen19a/hyvarinen19a-supp.pdf).

- Use: auxiliary-variable and contrastive alternatives when external context is available.
- Checked: primary abstract and metadata. Exact theorem assumptions must be read for each use; no theorem-number mapping is asserted here.

## Nonidentifiability and symmetry attacks

**[HP99]** Hyvarinen, A., and Pajunen, P. (1999). *Nonlinear independent component analysis: Existence and uniqueness results*. Neural Networks 12(3), 429-439. [Author publication page](https://www.cs.helsinki.fi/u/ahyvarin/papers/ICA.shtml).

- Use: baseline nonuniqueness of unrestricted nonlinear ICA and the need for structural restrictions.
- Checked: author-page bibliographic entry and summary. Full theorem text was not checked in preparing this skill; verify the precise model before citing a formal impossibility statement.

**[LOC19]** Locatello, F., Bauer, S., Lucic, M., Raetsch, G., Gelly, S., Schölkopf, B., and Bachem, O. (2019). *Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations*. PMLR 97, 4114-4124. [Proceedings](https://proceedings.mlr.press/v97/locatello19a.html).

- Use: distinguish unsupervised likelihood fitting from recovery of intended factors; identify the required inductive bias.
- Checked: primary abstract and metadata. Do not extend its impossibility claim indiscriminately to supervised, multi-view, temporal, or otherwise restricted models.

## Observation inversion and moment determinacy

**[LIN17]** Lin, G. D. (2017). *Recent developments on the moment problem*. Journal of Statistical Distributions and Applications 4, 5. [Open article](https://link.springer.com/article/10.1186/s40488-017-0059-2). DOI: `10.1186/s40488-017-0059-2`.

- Use: checkable moment-determinacy criteria and the distinction between moments existing and determining a law.
- Checked: Theorem 1 and surrounding Carleman/growth criteria. Determinacy conditions can be sufficient without being necessary.

**[PET82]** Petersen, L. C. (1982). *On the relation between the multidimensional moment problem and the one-dimensional moment problem*. Mathematica Scandinavica 51, 361-366. [DOI](https://doi.org/10.7146/math.scand.a-11986).

- Use: joint determinacy from coordinate determinacy and the complete mixed moment sequence.
- Checked: publisher metadata; the supplied SIMVI proof also cites this work. Full-text retrieval was unavailable during preparation. Verify the source statement before using a numbered theorem. Equal marginals alone do not identify a joint law.

## Smooth maps, rank, and local inversion

**[SARD42]** Sard, A. (1942). *The measure of the critical values of differentiable maps*. Bulletin of the American Mathematical Society 48, 883-890. [DOI](https://doi.org/10.1090/S0002-9904-1942-07811-6).

- Use: critical-value measure-zero arguments; in particular, exclude smooth surjections from lower to higher dimension.
- Checked: publisher index metadata. Original full text was unavailable during preparation. Verify the required differentiability threshold for any use beyond the smooth setting.

**[LEE12]** Lee, J. M. (2012). *Introduction to Smooth Manifolds*, second edition. Graduate Texts in Mathematics 218, Springer. [Publisher](https://link.springer.com/book/10.1007/978-1-4419-9982-5).

- Use: inverse/rank theorems, smooth manifolds, and Sard's theorem; distinguish local diffeomorphisms from global invertibility.
- Checked: publisher metadata and topic coverage. No unverified theorem or page numbers are supplied; locate the needed theorem in the edition used.

## Optional downstream estimation

**[DML18]** Chernozhukov, V., Chetverikov, D., Demirer, M., Duflo, E., Hansen, C., Newey, W., and Robins, J. (2018). *Double/debiased machine learning for treatment and structural parameters*. The Econometrics Journal 21(1), C1-C68. [Journal](https://academic.oup.com/ectj/article/21/1/C1/5056401), [author working-paper version](https://www.nber.org/papers/w23564.pdf).

- Use: orthogonal scores, nuisance estimation, and cross-fitting when connecting an identified representation to effect estimation.
- Checked: primary abstract and metadata. This is not a blanket theorem for arbitrary residualization, learned treatments, graph dependence, or individual treatment effects. Read the relevant estimator theorem and verify its hypotheses separately.

## Citation practice

Keep a source ledger with the exact statement used, location, assumptions matched, and unverified conditions. New calculations in this skill (normalizer checks, Gaussian contrasts, simplex counterexamples) should be presented as derivations, with their premises, rather than attributed verbatim to a source. Cite a paper for what it establishes, not for a stronger conclusion suggested by its title.
