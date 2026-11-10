---
name: scanpy
domain: compbio
description: Implement or review Scanpy scRNA-seq QC, preprocessing, feature selection, graphs, clustering, markers, annotation, and visualization with explicit AnnData layer and biological-replicate contracts.
license: SD-3-Clause license
metadata:
  version: "1.0.1"
  skill-author: K-Dense Inc.
---

# Scanpy single-cell analysis

Inspect Scanpy/AnnData versions, assay, organism/reference, feature IDs, samples/donors, matrix provenance, and the requested biological comparison. Preserve counts and sample identity before preprocessing.

## Expression and preprocessing contract

- Determine whether `X`, layers, and `raw` contain integer counts, normalized values, log expression, scaled values, or corrected data. `adata.raw` is a snapshot of the selected `X`/features, not automatically raw counts. Preserve counts in an explicitly named layer before normalization when available.
- Assess per-sample QC distributions, mitochondrial annotation, doublets/background, and cell/gene coverage before thresholds. `MT-` is not a universal organism/identifier rule.
- Match HVG flavor to its required input: some expect log-normalized expression, others counts. Make batch-aware selection and retained feature space explicit.
- Normalize/log/scale only as required by the chosen workflow. Regression and scaling can remove biology or densify large matrices; do not apply them universally.

## Graphs, clusters, and annotation

1. Build PCA or the intended representation, select supported components, then build the named neighbor graph. UMAP visualizes that graph; it is not evidence of integration or cluster validity by itself.
2. Run clustering before plotting its key. Assess sample composition, marker consistency, depth effects, and stability at a justified resolution rather than choosing the most visually separated UMAP.
3. Rank markers using the intended expression layer and test. Keep effect sizes, detection rates, multiple testing, and cluster-selection bias visible.
4. Annotate from multiple positive/negative markers and relevant references, retaining ambiguous/unknown labels. Cluster numbers have no fixed PBMC cell-type meaning.
5. For trajectory work, build required graph/diffusion representations and justify a real root from evidence. Pseudotime does not establish a causal lineage.

## Condition comparisons and outputs

Use independent biological replicates for condition inference, often donor-by-cell-type pseudobulk with an estimable design. A cell-level Wilcoxon test across thousands of correlated cells is not a replacement for donor replication. Separate exploratory cluster markers from confirmatory condition DE.

Save counts/processed-layer descriptions, sample and feature IDs, graphs/reductions, parameters/seeds, annotations and evidence, and software versions. Reopen a selected output and verify shapes, IDs, matrix values, and required keys.

## Optional resources

- [Standard workflow](references/standard_workflow.md): use for step ordering and adapt assumptions to the data.
- [API reference](references/api_reference.md): lookup aid; verify signatures against the installed release.
- [Plotting guide](references/plotting_guide.md): choose plots and inspect the matrix/layer being shown.
- [QC helper](scripts/qc_analysis.py): inspect configurable thresholds and input semantics before running.
- [Analysis template](assets/analysis_template.py): customize paths, QC, features, and annotations; it is not an automatic biological interpretation.

Use [official Scanpy documentation](https://scanpy.readthedocs.io/) for version-specific methods. Verify the relevant small input/graph/statistical contract before a long run; do not claim an end-to-end analysis from a static review.
