# Distances, tests, and cell-type prioritization

## Population distances

Choose a common representation and feature order before comparing groups. Keep cell types, donors, batches, doses, and time points separate or model them according to the question. UMAP visualization coordinates are not a default quantitative effect space; use a justified expression or latent representation.

| Metric | What it emphasizes |
|---|---|
| `euclidean`, `mse`, `pearson_distance`, `cosine_distance` | Differences between aggregate mean profiles |
| `edistance` | Between- versus within-population cell distances |
| `mmd` | Distributional discrepancy, dependent on kernel choices |
| `wasserstein` | Transport between cell distributions; requires JAX |

Metric names are literal API values; e.g. `pearson_distance` differs from `pearson` used by some space-comparison helpers. Not every supported score is symmetric or a mathematical metric. Consult the class API for specialized likelihood/classifier scores.

Template: `adata` already contains the chosen `X_pca`, group labels, and the actual `control` category.

```python
import pertpy as pt

distance = pt.tl.Distance("edistance", obsm_key="X_pca")
pairwise = distance.pairwise(adata, groupby="perturbation", n_jobs=1)
to_control = distance.onesided_distances(
    adata, groupby="perturbation", selected_group="control", n_jobs=1
)
```

The instantiated tool can also be called as `distance(X, Y)` with two cell-by-feature arrays. `layer_key` selects a matrix layer and `obsm_key` selects an embedding; use one. Explicit representation selection avoids reliance on default `X_pca`. Bootstrap results summarize distance variability under the implemented cell resampling; they do not automatically account for donor-level dependence.

Inspect group sizes and finite outputs. For large screens, compare to a control or a justified subset first; all-cell distance storage can grow quadratically even when the group-level result is small. Record any subsampling. Use comparable preprocessing and selected features for real, predicted, and control populations.

## Distance-based permutation testing

```python
import pertpy as pt

test = pt.tl.DistanceTest(
    "edistance",
    obsm_key="X_pca",
    n_perms=1000,
    padj_threshold=0.05,
    correction="holm-sidak",
)
table = test(adata, groupby="perturbation", contrast="control")
```

Results include `distance`, `pvalue`, `pvalue_adj`, `significant`, and `significant_adj`. Use adjusted columns for the multiple-comparison claim; raw and adjusted flags differ. `contrast` is a group label. `alpha` is a deprecated constructor alias.

The built-in test permutes cells and does not expose a donor/block argument in this version. Establish exchangeability for the proposed use; a donor-level experiment may need a separately justified sample-level or restricted-permutation analysis. Keep the effect-size calculation available even if the requested inferential design needs clarification.

In 1.4.0 `DistanceTest` exposes no seed argument and constructs internal unseeded `numpy.random.default_rng()` generators. Do not invent `random_state`, and do not claim `numpy.random.seed(...)` makes these permutations reproducible. Record the run and its results. Larger permutation counts improve resolution but do not repair confounding.

## Augur

Augur ranks cell types by how well a model distinguishes conditions within each type, using repeated subsampling and cross-validation. It quantifies predictability under the chosen representation/design, not causal importance or a direct gene effect size.

Template: normalized-expression `adata` contains `condition` and `cell_type`. Each included cell type has enough cells of each selected condition for the chosen subsampling and folds.

```python
import pertpy as pt

augur = pt.tl.Augur("random_forest_classifier", random_state=0)
loaded = augur.load(
    adata,
    label_col="condition",
    cell_type_col="cell_type",
    condition_label="control",
    treatment_label="treated",
)
scored, results = augur.predict(
    loaded, subsample_size=20, n_threads=4, random_state=0
)
ranking = results["summary_metrics"].loc["mean_augur_score"].sort_values(ascending=False)
```

`predict` returns `(AnnData, results)`; the annotated cells include `augur_score`. For binary classification, assess AUC relative to chance and inspect skipped types; multiclass/regression scores require their own interpretation. Check condition–donor/batch confounding because default cell-wise cross-validation does not establish generalization to new donors. Do not silently present a pooled cell split as a donor-held-out evaluation.

For differential prioritization, use default and `augur_mode="permute"` runs for both comparisons, then `predict_differential_prioritization`; subtracting scores alone provides no p-value. Variance-feature selection uses LOESS and can fail on unsuitable data; inspect `span`, sample size, and feature distributions rather than suppressing the failure.

Sources: [Distance API](https://pertpy.scverse.org/en/stable/api/tools/pertpy.tools.Distance.html), [DistanceTest API](https://pertpy.scverse.org/en/stable/api/tools/pertpy.tools.DistanceTest.html), [distance test tutorial](https://pertpy.scverse.org/en/stable/tutorials/notebooks/distance_tests.html), [Augur API](https://pertpy.scverse.org/en/stable/api/tools/pertpy.tools.Augur.html), [Augur tutorial](https://pertpy.scverse.org/en/stable/tutorials/notebooks/augur.html). RNG behavior was checked in the published 1.4.0 wheel's `_distance_tests.py`.
