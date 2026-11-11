# Guide assignment and perturbation efficacy

## Assign guides

Use `pt.pp.GuideAssignment()` on a **cells × guides** AnnData, often `mdata["gdo"]`. Map guide IDs to biological targets separately; do not use the RNA gene matrix as guide counts.

| Method | Interpretation | Default AnnData output |
|---|---|---|
| `assign_by_threshold` | All guide signals meeting a chosen threshold | `layers["assigned_guides"]`, binary calls |
| `assign_to_max_guide` | Highest-count guide if it reaches the threshold | `obs["assigned_guide"]` |
| `assign_mixture_model` | Probabilistic per-guide assignment; supports multiple guides | `obs["assigned_guide"]`, plus fit-related annotations |

Threshold and maximum-guide methods require `assignment_threshold`; do not select a universal value. Maximum assignment forces at most one label and can conceal expected combinations. The mixture model needs the `jax` extra. Its default negative label (`negative`) differs in case from the maximum-guide method (`Negative`).

Template: `guide_counts` contains the selected count matrix; `chosen_threshold` comes from the experiment's assignment policy and count distributions.

```python
import pertpy as pt

ga = pt.pp.GuideAssignment()
ga.assign_by_threshold(guide_counts, assignment_threshold=chosen_threshold)
ga.assign_to_max_guide(
    guide_counts,
    assignment_threshold=chosen_threshold,
    obs_key="max_guide",
)
```

Validate fractions with no guide, one guide, and multiple guides; inspect guide-level count distributions and assignment sensitivity. Align assignment labels back to RNA cells by cell ID. A detected guide establishes exposure, not a successful transcriptional perturbation.

## Mixscape: responding versus nonresponding cells

Start with log-normalized, unscaled RNA expression in `.X` and a suitable neighbor representation. Keep counts elsewhere. Identify matched controls within each replicate/cell-type stratum; ensure each split contains enough controls for `n_neighbors`.

Two columns may serve different purposes: one distinguishes treated/control cells for signature calculation; another names the target gene for classification. Both must represent the specified control correctly.

Template: `adata` already contains log-normalized `.X`, `obsm["X_pca"]`, and columns `perturbation`, `gene_target`, `replicate`; `NT` is the actual control label in both target columns.

```python
import pertpy as pt

ms = pt.tl.Mixscape()
ms.perturbation_signature(
    adata,
    pert_key="perturbation",
    control="NT",
    split_by="replicate",
    use_rep="X_pca",
    n_neighbors=20,
)
ms.mixscape(
    adata,
    pert_key="gene_target",
    control="NT",
    layer="X_pert",
    split_by="replicate",
    random_state=0,
)
```

The signature is expression relative to selected controls and is written to `layers["X_pert"]`. Classification adds `obs["mixscape_class"]`, `obs["mixscape_class_global"]`, and a posterior column such as `mixscape_class_p_ko` under default KO labeling. `de_layer` selects the expression used for marker testing; it is distinct from the signature `layer`.

Inspect responding/nonresponding fractions by target, guide, and replicate; check sparse or low-DE targets and convergence warnings. An NP call is evidence of an undetected transcriptional response under this model, not proof that editing failed. Do not silently remove NP cells from the primary analysis.

Use `ms.lda(...)` after classification for a discriminant visualization, and `ms.plot_barplot`, `plot_perturbscore`, or `plot_heatmap` for diagnostics. LDA is supervised and should not be presented as independent validation. Signature calculation supports `batch_size` to limit memory use.

## Mixscale: continuous efficacy

`pt.tl.Mixscale()` shares `perturbation_signature(...)`, followed by `.mixscale(..., layer="X_pert")`. It estimates continuous efficacy rather than Mixscape's discrete KO/NP classes; the default score name is `mixscale_score`. Guide-level `fine_mode`, supplied DE-gene sets, and harmonization change interpretation, so inspect those options only when needed and retain the selected settings.

Sources: [GuideAssignment API](https://pertpy.scverse.org/en/stable/api/preprocessing/pertpy.preprocessing.GuideAssignment.html), [Efficacy tutorial](https://pertpy.scverse.org/en/stable/tutorials/notebooks/perturbation_efficacy.html), [Mixscape API](https://pertpy.scverse.org/en/stable/api/tools/pertpy.tools.Mixscape.html), [Mixscale API](https://pertpy.scverse.org/en/stable/api/tools/pertpy.tools.Mixscale.html).
