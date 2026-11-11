# Setup, compatibility, and data

## Environment

Inspect the environment selected by the project, rather than assuming the shell's default interpreter is the notebook kernel:

```python
import sys
from importlib.metadata import version

print(sys.executable)
print(version("pertpy"))
```

The inspected PyPI release is **pertpy 1.4.0**, requiring **Python >=3.12**. Query release metadata again when choosing a different version. An import failure can reflect a missing optional dependency rather than a missing base package; lazy-loaded classes may fail only on first access.

Install into the selected project environment when installation is part of the task. For example:

```bash
python -m pip install 'pertpy==1.4.0'
# Choose extras for the requested workflow, e.g.:
python -m pip install 'pertpy[de]==1.4.0'
```

| Workflow | Extra for 1.4.0 | Additional requirement |
|---|---|---|
| Most core tools, threshold guide assignment, Mixscape, Augur | Base package | No JAX requirement for these tools |
| DGE interface, Milo's `pydeseq2` solver | `de` | Use sample-level raw counts for count models |
| scCODA, CINEMA-OT, scGen, MLPClassifierSpace, Wasserstein distance, guide mixture model | `jax` | GPU execution needs a compatible JAX backend; the extra does not guarantee it |
| tascCODA | `tcoda` | Includes JAX and tree-related dependencies |
| Milo's `edger` solver | `milo-edger` | R with Bioconductor `edgeR` and `statmod` |
| `pt.tl.EdgeR` DGE | `de` plus `rpy2` | R with Bioconductor `edgeR` |

The stable installation page combines `de,milo-edger` in its Milo command even while describing the Python solver. The release metadata makes the split clear: `de` supplies PyDESeq2; `milo-edger` supplies `rpy2`. Select the solver explicitly and install its requirements. `all` in this release does not include `milo-edger`.

## Matrix and metadata contract

Inspect `shape`, `obs.columns`, `var_names`, `layers`, `obsm`, and `uns`. For MuData, inspect `mod` and the modality actually consumed by the method. Preserve original gene identifiers; do not silently collapse duplicate symbols.

| Input | Appropriate use |
|---|---|
| Cells × guides, observed guide counts | Guide assignment; separate from RNA expression |
| Cells × genes, verified raw counts | Retain as counts; aggregate for count-based DE |
| Cells × genes, log-normalized expression | Mixscape/Mixscale signature input, scGen, many enrichment workflows |
| Cells × dimensions, e.g. `obsm["X_pca"]` | Distances and neighborhood graph construction |
| Samples × genes, summed raw counts | PyDESeq2/EdgeR for a specified cell population |
| Samples × cell types, counts of captured cells | scCODA/tascCODA |

Check control spelling, missing labels, sample-condition consistency, and a sample × condition × cell-type count table. Do not normalize data twice because a tutorial contains normalization. Verify provenance, not just integer-like values or a layer name.

If metadata is only at MuData's top level, copy selected columns by index after checking coverage:

```python
rna = mdata["rna"]
columns = ["perturbation", "sample", "cell_type"]
assert rna.obs_names.is_unique and mdata.obs_names.is_unique
assert rna.obs_names.isin(mdata.obs_names).all()
rna.obs[columns] = mdata.obs.reindex(rna.obs_names)[columns]
```

These are example column names; substitute the actual schema. Do not align by row position after independently filtering modalities.

## Version-sensitive differences

- `pt.ds` was added alongside `pt.dt` in 1.4.0. For older installed versions, check the available dataset alias.
- Current scGen is `pt.tl.Scgen`, implemented with JAX since 1.3.0. The linked prediction notebook still contains old `pt.tl.SCGEN`/scvi-tools calls; use the class API and installed signatures.
- Perturbation spaces were redesigned in 1.2.0. Use current `.compute(...)` methods; do not assume old `compute_*` examples still apply.
- `DistanceTest` uses `padj_threshold`; `alpha` is deprecated.
- 1.4.0 includes changes affecting Mixscape classifications and distance values. Version-lock a reproduction instead of treating changed numerical results as proof of an implementation error.

Use `inspect.signature` or `help` on the exact installed method when a tutorial differs. Retain meaningful warnings; do not copy tutorial-wide `warnings.filterwarnings("ignore")`.

Sources: [Installation](https://pertpy.scverse.org/en/stable/installation.html), [PyPI 1.4.0 metadata](https://pypi.org/pypi/pertpy/1.4.0/json), [Changelog](https://pertpy.scverse.org/en/stable/changelog.html).
