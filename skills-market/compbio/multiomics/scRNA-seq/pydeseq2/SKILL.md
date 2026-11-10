---
name: pydeseq2
domain: compbio
description: Design, run, or review PyDESeq2 differential-expression analysis on bulk RNA-seq or biologically replicated pseudobulk counts, with sample alignment, estimable designs, explicit contrasts, and FDR interpretation.
license: MIT license
metadata:
  version: "2.0.0"
  skill-author: K-Dense Inc.
---

# PyDESeq2 differential expression

Inspect PyDESeq2 version, count provenance, sample/feature IDs, biological replicates, design variables, requested contrast, and analysis output scope. Use the installed API and official example rather than a fixed dependency-version list.

## Input and design gates

- Supply samples-by-genes non-negative finite integer counts with uniquely indexed sample metadata. Use actual identifiers/source metadata to determine orientation; matrix dimensions do not prove that transposition is needed.
- Verify matching sample sets, then reorder metadata to count rows explicitly. Do not silently take an intersection, discard missing samples, round normalized expression into counts, or densify a large sparse matrix without a memory plan.
- Check missing design values, factor levels/reference coding, replication, paired/repeated structure, full-rank design, residual degrees of freedom, and contrast estimability before fitting. Report any exclusions and their reason.
- Complete batch-condition confounding cannot be repaired by dropping batch or adding an interaction. State the unsupported comparison; obtain informative samples or change the scientific question explicitly.
- State the exact contrast and positive fold-change direction. Additive formula term order does not determine an explicitly specified condition contrast; interactions change the question and require an appropriate coefficient/contrast.

## Fit and test

Choose a documented low-count filtering policy and normalization assumptions. Fit `DeseqDataSet` with the chosen design, then `DeseqStats` with an explicit supported contrast and alpha. Inspect fitting warnings, size factors, dispersion, outliers/Cook's filtering, independent filtering, and missing p-values; there is no universal required size-factor or p-value histogram shape.

Separate statistical tests, effect-size thresholds, and optional LFC shrinkage. Verify the coefficient chosen for shrinkage matches the intended comparison and is supported by the method/version. Preserve unshrunk results and label the effect estimate used for ranking/plots. Do not replace missing adjusted p-values with zero or change alpha only in the narrative.

For single-cell data, aggregate verified counts to the independent sample-by-cell-type unit when a pseudobulk design is appropriate. Cells from the same donor are not independent bulk replicates.

## Resources and verification

Use [API notes](references/api_reference.md) for lookup and the [workflow guide](references/workflow_guide.md) for design examples, checking them against the installed version. The [CLI helper](scripts/run_deseq2_analysis.py) supports a standard CSV workflow; inspect its orientation/options and limitations before use, especially for complex contrasts or interactions. CSV input defaults to genes by samples; use `--no-transpose` for samples by genes. Shrinkage is opt-in through `--shrink-coeff` after verifying the coefficient matches the contrast; unshrunk results are retained separately.

Check selected input values, sample mapping, design/contrast, warnings, result columns, effect direction, filtering counts, and plot labels. Save all tested genes with estimates, uncertainty, raw/adjusted p-values, filtering status, design/configuration and versions. Save trusted local state only when needed for reuse; pickle is not a portable or safe untrusted interchange format.

Use the [official PyDESeq2 example](https://pydeseq2.readthedocs.io/en/stable/auto_examples/plot_minimal_pydeseq2_pipeline.html) for supported fitting, testing, shrinkage and inference interfaces. A script smoke test does not validate a biological conclusion.
