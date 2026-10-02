# Consolidated experience report

Use the following structure as a guide, adapting it to existing project conventions. A small review may combine sections. A large review should keep the main conclusions short and place detailed run information below them. Let the ledger hold run facts, findings explain their meaning, and lessons specify future actions; cross-reference instead of repeating the same narrative in all three. Do not leave empty template fields in a delivered report.

## Identity and review scope

At the top, record:

- Project and project root.
- Review date, user's question, and scope of experiments reviewed.
- Primary index/record, any previous experience report, and evidence cutoff when known.
- Review mode: artifact inspection; identify any summaries recomputed during review.
- Material coverage limits: unavailable, unreadable or uninspected evidence relevant to the question.

Distinguish the review date from experiment dates. Use run manifests, dated records or explicit IDs for chronology; do not substitute file modification times.

## Consolidated findings

Lead with what the evidence establishes. Cover successful, unsuccessful, mixed and unresolved outcomes in proportion to their relevance. Each material finding must link to experiment IDs and source IDs.

For important findings use short connected paragraphs or a compact record:

- **Finding and scope**
- **Observed evidence**
- **Interpretation and outcome**
- **Explanation and evidence status**
- **Limitations or conflicting evidence**

Do not force an explanation where none is supported. Distinguish “the experiment did not support the claim” from “the claim is false.”

## Experiment ledger

Preserve existing run IDs. A useful compact table is:

| Experiment/run | Question or change; comparator | Data and evaluation unit | Execution | Computational outcome | Biological support | Evidence |
| --- | --- | --- | --- | --- | --- | --- |

Use short entries and link to details below when a row would become unreadable. Include the values and conditions needed to interpret a result. Record parameters, dataset versions, splits, code revisions and seeds only when available and relevant. Use “not recorded” for unknown metadata.

If the request covers only a subset of the index, say so. Planned experiments belong in open questions or next checks, not as completed runs. Discovered runs with inaccessible outputs can appear as unverified; never silently count them as failures.

## Reusable lessons

Assign stable IDs such as `L001` and use one specific heading per lesson. Preserve IDs when updating an existing report. Include memorable search terms such as the relevant algorithm stage, assay, biological context or error symptom.

### Lesson record

- **Lesson:** a concise, scoped conclusion.
- **Applies when:** conditions under which another agent should retrieve it.
- **Action or diagnostic:** what to do or inspect next time.
- **Evidence:** experiment IDs and source links; indicate direct inspection versus report-only evidence.
- **Status and limits:** established within the tested scope, provisional, or superseded; explain the evidence strength and any exception.

A lesson's status is a document-management aid, not a claim of universal correctness. An observed local limitation can be established within scope even if its mechanism is unresolved. Keep speculative causal claims visibly provisional.

Prefer a few useful lessons to a list of generic advice. Do not include “be careful,” “validate results,” or “use better parameters” without a concrete trigger, check, and supporting observation.

## Open questions and discriminating checks

Keep this section focused on uncertainties that affect a conclusion or next decision.

| Question | Current evidence and alternatives | Smallest useful check | What the outcome would distinguish |
| --- | --- | --- | --- |

Make clear that these are proposed checks unless actually performed. Note substantial data or compute requirements when evident. Avoid presenting an unrequested future research programme as part of completed work.

## Retrieval map

Provide a brief entry point for a future agent:

| When the next task involves… | Read first | Evidence to revisit |
| --- | --- | --- |

Use a small number of biological questions, algorithm components, dataset conditions or recognizable symptoms. Link to the relevant lesson headings and sources. The purpose is to retrieve a scoped lesson without rereading the entire experiment history.

For portability, prefer standard Markdown heading anchors and relative links. Resolve paths relative to the report's actual location. Do not rely on tool-only citation tokens or chat history.

## Evidence register and coverage

Use stable source IDs such as `S001`, retaining existing IDs on updates. List sources actually used and any missing source essential to understanding a limitation.

| Source ID | Artifact/link | Locator and run identity | Inspection state | Supports or limits |
| --- | --- | --- | --- | --- |

Useful locators include:

- Markdown heading and an entry date or experiment ID.
- Script line numbers or function name, with the run-linked revision when known.
- Configuration key and configuration/run identity.
- CSV/TSV row key and column names, or workbook sheet and cells.
- Notebook cell ID/index and whether saved output or current code was inspected.
- Log run ID and relevant line or timestamp.
- PDF page, or figure panel with the plotted variables.

Use clear inspection states: inspected, partially inspected, summary-only, unavailable, or not inspected. A source mentioned by another document is not automatically inspected. For summary-only findings, cite the summary and identify the underlying evidence gap.

Report material exclusions without dumping every filename. If small calculations were performed, record the input sources, filters and formula or analysis method so another agent can reproduce them. Mark plot-derived approximate values as approximate.

## Updating an existing report

Consolidate new evidence into the relevant finding or lesson. Preserve IDs, useful context and source links. Add a brief dated revision note only when a conclusion materially changes, stating what changed and which evidence changed it. Mark a disproven or outdated lesson as superseded and link its replacement. Retain unresolved contradictions until the evidence resolves them.

Do not repeatedly append the same retrospective, overwrite the original experimental record, or treat the previous experience report as independent evidence for the claims it summarized.
