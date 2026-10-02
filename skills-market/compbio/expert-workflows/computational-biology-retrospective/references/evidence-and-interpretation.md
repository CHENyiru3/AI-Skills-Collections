# Evidence and interpretation

Use these lenses selectively to explain computational biology experiments. The aim is an evidence-supported reconstruction, not a list of every conceivable flaw.

## Match the evidence to the claim

| Claim | Relevant evidence | What that evidence alone cannot establish |
| --- | --- | --- |
| A run completed | Matching run log, completion marker, output manifest | Correctness or scientific validity |
| A score improved | Comparable result rows, metric definition, evaluation set and uncertainty | Generalization or biological mechanism |
| An implementation bug caused an outcome | Run-linked code/configuration, execution trace, or controlled correction | That the underlying method or biological hypothesis is invalid |
| An algorithm component helped | Matched ablation/control with relevant settings held consistent | Universal usefulness across datasets |
| A biological pattern was recovered | Appropriate biological controls, independent validation, relevant assay/readout | Causality, mechanism, or validity outside the tested setting |
| A biological effect was absent | Appropriate design, sensitivity, uncertainty and controls | Absence solely from a nonsignificant test or failed algorithm |

No source type wins every dispute. Prefer evidence directly tied to the claim and run: a result table for a recorded number, run configuration for parameters, and inspected code for implemented behavior. A report may contain essential biological context that a metric file lacks. Explain conflicts instead of assuming that “raw” means correct or “latest” means authoritative.

For code, record whether it is a run-linked revision or only the current implementation. For derived summaries, give inputs, filters, aggregation, and calculation. For unreadable artifacts, state the limit rather than treating neighboring prose as direct inspection.

## Technical and algorithmic lenses

Investigate those suggested by the observed failure or comparison:

- **Execution and provenance:** exit status, partial output, resource exhaustion, convergence, stale caches, reused filenames, mixed run directories, checkpoint selection, code/configuration drift.
- **Data and indexing:** sample/cell/gene alignment, identifiers, duplicated observations, missingness, filtering, transformation order, normalization, sparse/dense handling, dimensions, units and coordinate systems.
- **Algorithm assumptions:** objective versus evaluation target, optimization stability, initialization, sensitivity to hyperparameters, graph construction, regularization, numerical behavior and scaling limits.
- **Comparison design:** matched inputs, splits, preprocessing, baselines, tuning budgets and selection criteria; preprocessing or tuning fitted on held-out data; labels used directly or indirectly during training.
- **Metrics:** definition and direction, averaging and weighting, imbalance, small or degenerate clusters, subgroup effects, selection of favorable seeds or datasets, and disagreement between proxy metrics and the actual task.

Distinguish an implementation failure from a limitation of the method. A resource failure may establish a limitation under the recorded hardware and input size; it need not say anything about accuracy. A parameter association suggests sensitivity, but an unmatched parameter sweep may not isolate its cause.

## Biological and statistical lenses

Start from the organism/system, assay, experimental design, and intended use. Follow only questions relevant to the project:

- **Independent replication:** distinguish donors, animals, specimens, sections, cells, spots, and technical replicates. Cells from one donor are not independent donor replicates. Multiple random seeds characterize computational variability, not biological replication.
- **Confounding:** examine whether phenotype, donor, batch, assay platform, tissue region, processing date, or quality covary. If batch and condition are inseparable in the design, state the resulting identifiability limit rather than assigning an observed difference to one cause.
- **Biological preservation:** a cleaner embedding, stronger mixing, or smoother spatial map can coexist with loss of cell states, rare populations, boundaries, or condition-specific signal. Evaluate the intended biological target with appropriate independent evidence.
- **Reference validity:** distinguish observed biology from annotations, marker-based proxies, inferred labels, simulations and imperfect gold standards. Agreement with labels used to build or tune a method is not independent validation.
- **Assay and sampling limits:** consider dropout, depth, coverage, cell composition, resolution, contamination, segmentation and tissue quality when the artifacts support their relevance. Do not assert these as causes from plausibility alone.
- **Biological coherence:** distinguish reproducible and externally supported patterns from attractive plots or post hoc pathway narratives. Record contradictory markers or subgroups as well as confirming examples.
- **Uncertainty and testing:** preserve effect size, dispersion or intervals, sample unit, multiple-testing treatment, split strategy and sensitivity where available. Do not manufacture uncertainty estimates or mistake lack of significance for equivalence.
- **Generalization:** distinguish within-dataset, held-out donor, cross-cohort, cross-assay, cross-tissue and cross-species evidence. Simulated recovery and observed-data validation answer different questions.

Do not diagnose a biological mechanism from a software result alone. When the evidence cannot separate biological variation, measurement artifacts, algorithmic assumptions and implementation effects, state the alternatives and the limit.

## Explain without overclaiming

Use this compact reasoning pattern for an important failure or success:

1. State the observation and its source.
2. State the narrow conclusion it supports.
3. Identify the leading explanation only if evidence favors it.
4. Name a material alternative or missing control when it changes the conclusion.
5. Suggest the smallest discriminating check, if useful, as work not yet performed.

The explanation's status should be explicit:

| Status | Meaning |
| --- | --- |
| Confirmed within scope | Direct evidence adequately isolates the proposed cause for the stated setting. |
| Supported explanation | Evidence favors it, but an important alternative remains. |
| Hypothesis | Plausible and testable; the reviewed evidence does not discriminate it. |
| Unknown | Evidence is insufficient to propose or rank explanations responsibly. |

These statuses describe explanations. The underlying observation may be directly verified even when its cause is unknown. Do not turn status labels into invented probabilities.

## Worked reasoning examples

### Higher score, uncertain generalization

A table shows that variant B outperforms A. The configurations reveal different donor splits and normalization. Preserve the scores and their provenance, but classify the method comparison as inconclusive. A matched rerun is a proposed check; the existing difference does not isolate the algorithm change.

### Successful integration, possible biological loss

An integration score improves, while a report says condition-associated markers weaken. If only the score table is inspected, the score is directly observed and marker loss is report-only. Inspect the marker outputs and design before drawing a stronger conclusion. Overcorrection may be a hypothesis; a confounded study may not distinguish removed batch effects from removed biology.

### Implementation error without a failed biological hypothesis

A run-linked error trace and code show a cell-to-label indexing mismatch, and a correction restores alignment. This supports a technical cause for that error. It does not establish the performance of a completed corrected experiment or the truth of the biological hypothesis unless those outcomes are also available.

### Negative result worth retaining

A matched ablation shows no consistent improvement across the evaluated cohorts. Record the tested settings, uncertainty, and any subgroup tradeoffs. A reusable lesson can be that this component lacked demonstrated benefit under those conditions; it should not become “the component never works.”
