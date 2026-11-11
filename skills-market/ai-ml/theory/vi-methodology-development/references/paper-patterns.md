# Source evidence and transferable patterns

Use for provenance, literature-informed design, or extending the skill with another paper. This is a synthesis of design logic, not a unified model attributed to all three papers. The source annotations below are retained from the originating review, not new reproduction claims from this collection import. Page numbers are one-based PDF pages of the editions inspected there. That review covered main text, Methods, figures/Extended Data and reporting sections, with equation pages inspected visually. ResolVI and CytoVI supplementary notes referenced outside those PDFs were not read. Relevant official SIMVI supplement sections were additionally checked as identified below.

## Common structure, different choices

| Design question | SIMVI example | ResolVI example | CytoVI example | Transferable decision |
|---|---|---|---|---|
| What explains an observation? | Two state blocks with relational information | Target-state emission plus contamination sources | Latent state and observed measurement conditions | Define scientific and measurement roles before architecture |
| What information constrains inference? | Unit inputs and neighborhood summaries routed differently | Focal inputs plus reused neighbor predictions; mixed parameter ownership | Shared observed features, metadata, optional labels | Write inference inputs and information access explicitly |
| Where is complexity placed? | Latent dependencies and asymmetric regularization | Observation composition, nuisance parameters and priors | Likelihood/preprocessing, conditional decoder and prior | Add complexity at the layer explaining the failure |
| What is optimized? | Practical surrogate plus selectively routed dependence loss | VI/MAP hybrid with optional supervision and training approximations | Masked conditional VAE objective plus optional adversary | Separate ELBO, MAP, auxiliary terms and gradient algorithm |
| What is returned? | Latent summaries and separate downstream effects | Generated signal versus corrected observed counts | Conditional predictions and distinct downstream estimators | Define each output as a query or additional estimator |
| What supports success? | Component preservation and targeted ablations | Artifact removal and signal preservation controls | Fit, imputation, preservation and false-alignment controls | Match evidence to each claim; no universal embedding score |

None of these columns mandates a graph, multiple latent blocks, Gaussian-mixture prior, ZINB, adversary, numerical default, or biological interpretation for a new task.

## SIMVI: model, approximation, and gradient flow are distinct

**Source:** Dong et al. (2025), *SIMVI disentangles intrinsic and spatial-induced cellular states in spatial omics data*, [DOI](https://doi.org/10.1038/s41467-025-58089-7). The originating review used the article PDF; the DOI and official supplement below provide public source locations.

**Verified source choices.** Methods p. 10, Eqs. 1–3 describe an unordered Gaussian state collection, a graph-dependent allocation/permutation, a second state conditional on neighboring allocated states, a scale variable (optionally replaced by observed exposure), and a count decoder. Unit and neighborhood information parameterize different variational factors. The theoretical generative dependence is richer than “two independent normal priors plus a graph encoder.”

Methods pp. 10–11, Eqs. 4–10 derive a full-data objective and then drop an intractable allocation term and replace the graph-conditional state KL with a weak standard-normal KL. The paper calls the practical result an effective ELBO; it is not established by those substitutions as the exact ELBO of the original joint. Eq. 14 adds a dependence penalty whose gradients update only one encoder branch. A scalar loss formula alone therefore under-specifies the algorithm. The Gaussian covariance penalty assumes Gaussianity for its MI interpretation; the MMD alternative matches the concatenated distribution to a Gaussian and affects marginals as well as dependence.

The [official supplement](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-025-58089-7/MediaObjects/41467_2025_58089_MOESM1_ESM.pdf), Supplementary Note 1, pp. 3–6, 11, 16–17, makes recovery claims under specific graph, decoder, variability/support and minimum-dimension assumptions. It acknowledges the difficulty of enforcing minimum dimension in a VAE. The theorem is about recovery up to stated transformations, not semantic identification of arbitrary coordinates by a generic penalty. Supplement Eq. 76 and inspected code also clarify an encoder-input notation discrepancy in the main equation.

Methods p. 11 use full-graph inference with loss-selected nodes, which is transductive context access. Downstream effects use a separate archetypal/residual-regression procedure (pp. 11–12), not merely a decoder output. Some evaluation annotations are model-derived (pp. 13–14), which limits their independence as truth.

**Transfer.** Keep separate generative dependencies, inference information access, and gradient flow. State the exact bound before approximations. Attach theoretical guarantees to their assumptions and implemented scope. Distinguish representation learning from downstream estimation and independent evaluation. Do not inherit numerical KL weights, graph architecture, independence penalties, or its effect estimator.

## ResolVI: represent the measurement mechanism and parameter ownership

**Source:** Ergen and Yosef (2026), *ResolVI: addressing noise and bias in spatial transcriptomics*, [DOI](https://doi.org/10.1038/s41592-026-03212-9). The originating review used the article PDF.

**Verified source choices.** Figure 1 and Methods pp. 13–14 describe own-state, neighbor-state and background contributions. A shared decoder emits normalized profiles; local mixture weights determine amounts; another set of weights allocates the neighbor contribution. The observation mechanism combines Gamma–Poisson variation for some sources with a background intensity offset. It is not automatically a single ordinary NB distribution or a categorical mixture selecting one source.

The paper distinguishes amortized MAP source proportions, nonamortized MAP neighbor weights, learned mixture-prior parameters and latent inference. A Gaussian-mixture prior does not specify the variational posterior. The paper does not print a full q factorization or fully expanded objective; do not invent one and label it source-verified. Optional labels influence mixture assignments and introduce a classifier loss. KL warmup, detached neighbor predictions, input augmentation and parameter-specific update rates are part of the practical algorithm (pp. 13–14).

Its output APIs distinguish generated signal, which may impute zero observations, from corrected observed counts, which preserve zeros through count reweighting (pp. 13–14). Validation separately considers artifact removal and preservation; the Discussion acknowledges bottleneck/prior sensitivity and imperfect reference truth (p. 11).

**Source ambiguities.** The printed exponential-rate signs and dispersion/inverse-dispersion notation require checking; independent Gamma intensities do not become an exactly normalized random vector merely because their means sum to one. An auxiliary check of the retained legacy scvi-tools implementation found positive-rate priors, diagonal-Gaussian q for state, and Delta/MAP nuisance guides, with some defaults different from the paper. That is implementation evidence, not a complete reproduction of the publication. New work should check the maintained owner and selected version; see [scvi alignment](scvi-tools-alignment.md).

**Transfer.** Explicitly model how target signal becomes an observation. Separate random effects, MAP parameters and fixed quantities; track their index sets, amortization and update frequency. Derive moment/support checks before coding a compound likelihood. Export different corrected/generated quantities through distinct query definitions. Do not assume a bottleneck alone identifies sources or that all uncertainty is Bayesian.

## CytoVI: likelihood scale, masks and query conditioning

**Source:** Ingelfinger et al. (2026), *CytoVI: deep generative modeling of antibody-based single cell data*, [DOI](https://doi.org/10.1038/s41592-026-03224-5). The originating review used the article PDF.

**Verified source choices.** Methods p. 13 models transformed/scaled continuous observations using Gaussian or Beta alternatives, with a decoder conditional on known measurement conditions. A standard or mixture Gaussian prior is paired with a diagonal-Gaussian variational posterior; optional labels affect prior weights. Transformation, likelihood, and metadata are therefore substantive model choices.

For incomplete panels, the encoder uses shared features while the decoder targets the union. Only measured entries contribute to reconstruction (pp. 13–14, Eqs. 7–9). An adversarial classifier is an additional objective, separate from the displayed ELBO. Imputation decodes inferred states under a condition where a target feature was measured (p. 14, Eqs. 10–11). Nearest-neighbor label transfer and external-modality averaging are separate procedures, not additional likelihoods in the fitted VAE.

The paper investigates measurement distributions and posterior predictive fit (p. 15), hides observed features to evaluate imputation (p. 16), and tests false alignment when populations are absent (pp. 17–18). An association between uncertainty and prediction error is useful but weaker than calibrated coverage.

**Source ambiguities.** Displayed label-biased mixture weights omit a clear normalization step; encoder conditioning and variance notation vary across equations/prose; a downstream density-ratio equation is ambiguous about density versus log density. Resolve these against the desired mathematical estimator and a pinned implementation instead of copying them into a specification.

**Transfer.** Design measurement scale and likelihood together. Separate inference features, reconstruction features and missingness masks. Audit label access and optional losses. Define condition-switched predictions and uncertainty sources precisely. Evaluate desired alignment and false alignment together. Do not generalize known panel masking into a solution for arbitrary informative missingness.

## Foundational extensions

These sources inform the general VI layer, not the biological target. Mathematical constructions elsewhere in the skill are explicit generic examples and synthesis.

| Source | Inspected anchor | Reusable contribution |
|---|---|---|
| [Kingma & Welling, Auto-Encoding Variational Bayes](https://arxiv.org/html/1312.6114v11) (2013 preprint / 2014 conference) | Sections 2–3 | Amortized inference, reparameterized stochastic optimization, explicit probabilistic decoder |
| [Blei, Kucukelbir & McAuliffe, VI review](https://arxiv.org/html/1601.00670v9) (2017 journal) | Sections 2, 4 | Posterior approximation through optimization, ELBO identity, variational factorization and limitations |
| [Hoffman et al., Stochastic Variational Inference](https://jmlr.org/papers/v14/hoffman13a.html) (2013) | Local/global formulation and stochastic updates | Separate local/global unknowns and justify minibatch scaling |
| [Burda, Grosse & Salakhutdinov, Importance Weighted Autoencoders](https://arxiv.org/html/1509.00519v4) (2015 preprint / 2016 conference) | Section 3 | Alternative multi-sample bound; distinguish it from exact likelihood and scientific validity |
| [Locatello et al., Challenging Common Assumptions…](https://proceedings.mlr.press/v97/locatello19a.html) (2019) | Theoretical result and empirical conclusions | Make inductive assumptions and supervision explicit when claiming disentanglement |

## How to learn from another VI paper

Extract a short evidence record:

1. Target quantity, observational unit and measurement assumptions.
2. Observed, random, deterministic and point-estimated variables; normalized joint and sampling story.
3. Variational family, input access, amortization, and inference limitations.
4. Exact objective, approximation steps, auxiliary losses, gradient routing and estimator.
5. Exported queries and any separate downstream estimators.
6. Assumptions, identifiable object/equivalence class, and claim-specific validation.
7. Paper page/equation, code version if checked, discrepancies and unread supplements.

Then state **what transfers, why it transfers, the conditions needed, and what should not be copied**. A missing equation stays unresolved until derived and labeled as a reconstruction or verified in code. Prefer an additional paper that fills a specific gap (for example, discrete inference, missingness, structured posterior dependence or calibration) over accumulating a generic reading list.
