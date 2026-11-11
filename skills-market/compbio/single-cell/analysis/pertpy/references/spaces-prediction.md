# Perturbation spaces and response prediction

## Represent perturbations

Current space APIs generally transform cell-level input to a perturbation-level AnnData. Inspect output axes before running downstream tools.

| Class | Representation |
|---|---|
| `PseudobulkSpace` | Aggregated expression or embedding, optionally stratified |
| `CentroidSpace` | Mean position per perturbation in a chosen representation |
| `DistanceSpace` | Per-perturbation distance profiles |
| `EmbeddingSpace` | Externally supplied perturbation/gene embeddings |
| `LRClassifierSpace`, `MLPClassifierSpace` | Representations learned through perturbation classification |

`KMeansSpace`, `HDBSCANSpace`, and `ClusteringSpace` provide clustering-related operations. Their mutation and return conventions differ; inspect the class rather than treating every `.compute` as aggregation.

Template: `adata` contains verified raw `layers["counts"]`, normalized-expression `.X`, `X_pca`, `perturbation`, and `sample`. It has already been restricted to the relevant cell population.

```python
import pertpy as pt

space = pt.tl.PseudobulkSpace()
pb = space.compute(
    adata,
    target_col="perturbation",
    groups_col="sample",
    layer_key="counts",
    mode="sum",
)
centroids = pt.tl.CentroidSpace().compute(
    adata, target_col="perturbation", embedding_key="X_pca"
)
```

Sum raw counts for count-model pseudobulks; use a justified mean/embedding representation for descriptive comparisons. `CentroidSpace` defaults to `X_umap`, so specify the intended quantitative representation. Covariates varying inside a pseudobulk are dropped; check sample IDs and condition metadata after aggregation.

`compute_control_diff` can subtract matched control profiles within `group_col`, e.g. cell line or experimental stratum. Each stratum needs an appropriate control. In 1.4.0, groups without controls can be left unchanged with a warning; do not mislabel those rows as control-relative effects. With no layer/embedding key, the returned copy's `.X` is changed. With `layer_key`, the default output is `layers["control_diff"]`; with `embedding_key`, it is `obsm["control_diff"]`. `copy=True` is the default.

`nearest_perturbations` and `plot_similarity` summarize relationships. `add`, `subtract`, and `evaluate_combinations` assess defined arithmetic hypotheses in the selected space; they do not establish biological synergy on their own. Separate single and combination perturbations and align the reference/control convention.

For dose analyses, `dose_response` creates a perturbation/dose representation; `fit_dose_response` fits Hill curves. Keep dose units and matched contexts consistent. Inspect fit failures, dose coverage, `ec50_in_range`, and uncertainty. An EC50 of a transcriptomic distance is not automatically a viability IC50.

## scGen: predict a held-out response

In 1.4.0 use **`pt.tl.Scgen`**, requiring `pertpy[jax]`. Its input is log-normalized expression, and `setup_anndata` registers condition and cell-type fields. This is the current JAX implementation; the stable tutorial's uppercase `SCGEN` and Lightning/scvi-specific details are historical.

Template: `adata` has log-normalized expression, `condition` values `control`/`treated`, and `cell_type`; `target_cell_type` identifies the type whose treated response is held out. Other cell types provide both conditions, and controls of the target type remain available.

```python
import pertpy as pt

held_out = (
    (adata.obs["cell_type"] == target_cell_type)
    & (adata.obs["condition"] == "treated")
)
train = adata[~held_out].copy()
pt.tl.Scgen.setup_anndata(train, batch_key="condition", labels_key="cell_type")
model = pt.tl.Scgen(train)
model.train(max_epochs=100, batch_size=64, early_stopping=True, seed=0)
predicted, delta = model.predict(
    ctrl_key="control", stim_key="treated", celltype_to_predict=target_cell_type
)
```

Here `batch_key` names the condition field used for latent perturbation arithmetic; do not substitute a technical batch column by habit. The training object's internal validation split is distinct from the externally held-out response. Fit feature selection and learned preprocessing within the allowed training data, and preserve the benchmark's donor/perturbation split. Use the held-out treated cells only for the declared evaluation.

Compare predictions with matched controls and observed treatment using the same gene order and scale. Include a control/no-change baseline; a high correlation over all gene means can be driven by baseline expression. A model directory written with `.save(...)` can be loaded with `.load(...)`; pass the associated AnnData when it was not saved using `save_anndata=True`. Do not assume a current model can load historical scvi checkpoints.

## CINEMA-OT and predicted-population comparisons

`pt.tl.Cinemaot()` uses a representation and optimal-transport matching to separate confounders from estimated treatment effects. Its workflow includes `causaleffect`, `causaleffect_weighted`, and `synergy`. Inspect the current signatures before adapting a notebook. `.causaleffect(...)` returns an effect AnnData and can write a confounder representation to the original input; the weighted method returns two objects. Keep matching diagnostics and the effect representation distinct from ordinary normalized RNA expression.

Select controls, representation, `preweight_label`, and tuning parameters based on the experiment. Matching quality and the causal assumptions determine interpretation; the method name alone does not validate those assumptions.

`PerturbationComparison.compare_classification`, `.compare_knn`, and `Distance.compare_distance` compare real, simulated, and optionally control populations. Align features, preprocessing, sample composition, and test splits before calling them; inspect score orientation and baselines before ranking models.

Sources: [PseudobulkSpace API](https://pertpy.scverse.org/en/stable/api/tools/pertpy.tools.PseudobulkSpace.html), [CentroidSpace API](https://pertpy.scverse.org/en/stable/api/tools/pertpy.tools.CentroidSpace.html), [spaces tutorial](https://pertpy.scverse.org/en/stable/tutorials/notebooks/perturbation_space.html), [Scgen API](https://pertpy.scverse.org/en/stable/api/tools/pertpy.tools.Scgen.html), [CINEMA-OT tutorial](https://pertpy.scverse.org/en/stable/tutorials/notebooks/cinemaot.html), [comparison API](https://pertpy.scverse.org/en/stable/api/tools/pertpy.tools.PerturbationComparison.html).
