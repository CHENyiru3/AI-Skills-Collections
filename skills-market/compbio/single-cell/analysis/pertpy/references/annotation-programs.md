# Metadata, enrichment, and multicellular programs

## Metadata annotation

Use `pt.md` to enrich an existing dataset with external identifiers and annotations. Preserve original labels and distinguish unmatched identifiers from biological absence.

| Class | Typical purpose |
|---|---|
| `CellLine` | DepMap/CancerRxGene identifiers, cell-line properties, bulk profiles, drug-response metadata |
| `Compound` | Compound identifiers, synonyms, and chemical representations from PubChem |
| `Moa` | Mechanisms of action and target annotations from CLUE |
| `Drug` | Gene–drug target annotations; default ChEMBL, with other supported sources |
| `LookUp` | Inspect available metadata and identifier coverage |

Specify `query_id` and `reference_id` where supported; these are dataset-specific identifier fields, not interchangeable labels. Inspect current methods with `help` before calling, especially `Compound` and database-specific cell-line methods. Metadata retrieval can access external services and download reference tables. Record the source and retrieval date, cache useful responses, and report match rates.

Drug target annotation operates on genes (`.var`) and expects the relevant nomenclature, such as HGNC symbols. Cell-line and perturbagen metadata typically attach to observations. For external expression correlations, intersect **and reorder** gene identifiers explicitly; matching the set without matching order gives invalid correlations.

Source: [Metadata overview](https://pertpy.scverse.org/en/stable/api/metadata_index.html), [annotation tutorial](https://pertpy.scverse.org/en/stable/tutorials/notebooks/metadata_annotation.html).

## Gene-set enrichment

`pt.tl.Enrichment` supports cell-level gene-set scoring, overrepresentation, ranked enrichment, and signature reversal. These have different inputs and interpretations.

Template: `adata.X` is log-normalized expression and `gene_sets` maps names to gene lists in the same identifier system as `adata.var_names`.

```python
import pertpy as pt

enrichment = pt.tl.Enrichment()
enrichment.score(adata, targets=gene_sets, method="mean", random_state=0)
```

The default key prefix is `pertpy_enrichment`, with scores and associated metadata in `.uns`; inspect those keys to align scores with target names. `method="seurat"` uses expression-matched control genes and is distinct from mean scoring. Report gene-set overlap/coverage before interpreting weak or missing scores.

`.hypergeometric` and `.gsea` can consume Scanpy `rank_genes_groups` results. Confirm the rank-results key, intended contrast, score direction, gene universe, and identifier overlap. A dot plot of cell-level scores is not itself an enrichment significance test.

`signature_reversal` requires a **perturbation × gene** AnnData containing finite signed effects relative to matched controls, rather than raw or mean expression. Supply a signed query profile or up/down gene sets. Current outputs include `obs["signature_reversal_score"]` and `obs["signature_reversal_rank"]`. Higher reversal scores indicate stronger opposition to the query. This is an unnormalized connectivity-derived ranking; it does not provide tau, p-values, or FDR. A reversal ranking alone does not establish therapeutic efficacy.

Sources: [Enrichment API](https://pertpy.scverse.org/en/stable/api/tools/pertpy.tools.Enrichment.html), [enrichment tutorial](https://pertpy.scverse.org/en/stable/tutorials/notebooks/enrichment.html).

## DIALOGUE

Use `pt.tl.Dialogue` to discover programs that covary across cell types within shared samples. This needs meaningful sample/niche identifiers, sufficient representation of each modeled cell type across samples, a precomputed feature space such as PCA, and an appropriate per-cell quality covariate.

Template: `adata` has `cell_type`, `sample`, `cellQ`, and `X_pca`. Check their biological meaning and sample coverage before fitting; `cellQ` is not a universal column provided by pertpy.

```python
import pertpy as pt

dialogue = pt.tl.Dialogue(
    celltype_key="cell_type",
    sample_key="sample",
    cell_quality_key="cellQ",
    feature_space_key="X_pca",
    n_programs=3,
    random_state=0,
)
dialogue.fit_programs(adata)
dialogue.test_celltype_pairs(adata)
dialogue.refine_scores(adata)
```

These phases write program information into `.uns["dialogue"]`, embeddings such as `.obsm["X_dialogue"]`, and per-cell scores such as `.obs["mcp_0"]`. Use `get_program_genes` and the model's plotting methods for interpretation, and `test_phenotype_association` for the separately specified association question. Correlated programs across cell types do not by themselves demonstrate direct cell–cell signaling. Check which samples and cell-type pairs contributed and whether quality/batch covariates explain the association.

Sources: [Dialogue API](https://pertpy.scverse.org/en/stable/api/tools/pertpy.tools.Dialogue.html), [DIALOGUE tutorial](https://pertpy.scverse.org/en/stable/tutorials/notebooks/dialogue.html).
