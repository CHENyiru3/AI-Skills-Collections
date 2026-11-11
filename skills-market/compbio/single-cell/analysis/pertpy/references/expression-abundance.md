# Differential expression and abundance

## Differential expression

For count-model DE, sum verified raw RNA counts into **independent sample × condition × cell-type** units. Analyze a specified cell type or a justified model of cell-type effects. Retain donor pairing/covariates, filter low-information genes/samples transparently, and check design rank and residual degrees of freedom. A single aggregate per condition cannot support replicate-based inference.

For `PseudobulkSpace.compute`, `target_col` and optional `groups_col` jointly define groups. Within a cell type, `target_col="condition", groups_col="sample"` preserves both dimensions. If more dimensions are needed, create an explicit composite grouping column or use the project's aggregation tool; inspect the resulting `.obs` to ensure covariates survived. Only metadata constant within an aggregate is retained.

Template: `pb` is one cell population's sample-level raw-count AnnData, `.X` holds summed counts, `condition` contains `control` and `treated`, and `batch` is an estimable covariate. Adapt the design to the actual experiment.

```python
import pertpy as pt

model = pt.tl.PyDESeq2(pb, design="~ batch + condition")
model.fit()
contrast = model.contrast(
    column="condition", baseline="control", group_to_compare="treated"
)
results = model.test_contrasts(contrast)
```

Positive `log_fc` denotes increased expression in the group compared with the baseline. Pertpy standardizes results to columns including `variable`, `log_fc`, `p_value`, and `adj_p_value`; inspect the returned table instead of copying PyDESeq2's printed native column names. `EdgeR` follows the same fit/contrast interface and additionally needs R dependencies. `.cond(...)` constructs model conditions for complex contrasts; do not replace an interaction question with a main-effect comparison.

`WilcoxonTest`, `TTest`, `PermutationTest`, and `Statsmodels` cover other test/model choices. Inspect their input assumptions and exact interface before substituting them. A cell-level test does not automatically model donor replication. Adjusted p-values and effect sizes answer different questions; retain both.

## Milo: abundance changes across neighborhoods

Use a justified cell-state representation to build a KNN graph, then count cells **per biological sample per neighborhood**. Inspect representation, neighbor count, neighborhood size distribution, sample coverage, and confounding. Do not substitute a condition label for a sample identifier.

Template: `adata` has `obsm["X_pca"]`, valid `sample` IDs, and two-level `condition` metadata constant within sample. Set category order/contrast to match the intended comparison; this example sets control as baseline.

```python
import pandas as pd
import pertpy as pt
import scanpy as sc

work = adata.copy()
work.obs["condition"] = pd.Categorical(
    work.obs["condition"], categories=["control", "treated"]
)
milo = pt.tl.Milo()
mdata = milo.load(work)
sc.pp.neighbors(mdata["rna"], use_rep="X_pca", n_neighbors=30)
milo.make_nhoods(mdata["rna"], prop=0.1, seed=0)
mdata = milo.count_nhoods(mdata, sample_col="sample")
milo.da_nhoods(mdata, design="~ condition", solver="pydeseq2")
results = mdata["milo"].var.copy()
```

Check labels before setting categories so unexpected values do not become missing. `.count_nhoods` returns MuData; `.da_nhoods` mutates results. The `milo` modality is samples × neighborhoods, with test results in `.var`, including `logFC`, `PValue`, and `SpatialFDR`. Use the spatial multiple-testing correction for DA interpretation. Plotting a neighborhood graph additionally requires a suitable layout and `build_nhood_graph`.

The 1.4.0 default solver is `pydeseq2`; `edger` is optional. Multi-level contrasts and random effects need the matching API specification; do not improvise a contrast string or add a saturated design. `de_nhoods` tests gene expression within neighborhoods and is a separate question from DA.

## scCODA and tascCODA: composition

`Sccoda` models **sample × cell-type counts** jointly and reports changes relative to a reference cell type. Use actual counts rather than normalized proportions. `Tasccoda` additionally uses a biologically meaningful cell-type hierarchy; do not infer a tree from arbitrary label order.

Template: `adata` has cell-level sample, cell-type, and condition annotations; `reference_cell_type` is a selected reference category whose stability/coverage has been assessed.

```python
import pertpy as pt

coda = pt.tl.Sccoda()
mdata = coda.load(
    adata,
    type="cell_level",
    cell_type_identifier="cell_type",
    sample_identifier="sample",
    covariate_obs=["condition"],
)
mdata = coda.prepare(
    mdata, formula="condition", reference_cell_type=reference_cell_type
)
coda.run_nuts(mdata, rng_key=0)
effects = coda.get_effect_df(mdata)
credible = coda.credible_effects(mdata)
```

Inspect `mdata["coda"]` to verify counts and sample covariates. `formula` here follows the documented scCODA convention. Automatic reference selection is available, but document the selected category and evaluate sensitivity when interpretation depends on it. `run_nuts` defaults to 1,000 warmup and 10,000 posterior samples in this snapshot; a tiny smoke run is not a convergence assessment. Use posterior diagnostics, `summary`, and `make_arviz` as appropriate. Interpret credible compositional effects relative to the reference; they do not establish absolute cell-number changes. `set_fdr` changes the posterior selection threshold, not a frequentist p-value.

Sources: [DE tutorial](https://pertpy.scverse.org/en/stable/tutorials/notebooks/differential_gene_expression.html), [PyDESeq2 API](https://pertpy.scverse.org/en/stable/api/preprocessing/pertpy.tools.PyDESeq2.html), [Milo API](https://pertpy.scverse.org/en/stable/api/tools/pertpy.tools.Milo.html), [scCODA tutorial](https://pertpy.scverse.org/en/stable/tutorials/notebooks/sccoda.html), [Sccoda API](https://pertpy.scverse.org/en/stable/api/tools/pertpy.tools.Sccoda.html), [tascCODA tutorial](https://pertpy.scverse.org/en/stable/tutorials/notebooks/tasccoda.html).
