---
name: computational-biology-retrospective
description: "Review computational biology algorithm-development projects and consolidate past experiments into an evidence-linked Markdown experience report. Use for experiment retrospectives, learning from biological or technical failures, and recovering reusable lessons from mixed project folders. Start from the project index or research log, then trace relevant scripts, configurations, results, and reports. Not for running new experiments or drafting a manuscript alone."
---

# Computational Biology Retrospective

Turn a mixed research folder into a concise, traceable account of what was attempted, what worked, what failed, and what remains uncertain. Preserve lessons that another agent can retrieve and apply without the original conversation.

Treat algorithm behavior, implementation correctness, statistical evidence, and biological interpretation as distinct questions. A completed run or improved benchmark does not by itself establish biological validity. An unsuccessful experiment does not by itself refute the biological hypothesis.

## Scope and output

- Use the user's folder, question, and requested output path. Otherwise use the active project root, follow its existing reporting convention, and fall back to `EXPERIENCE.md` in that root. Use the user's requested language or the established project language; default to English if neither is clear.
- Review existing evidence. Reading artifacts and computing small, transparent summaries is part of this work; running project pipelines, retraining models, or changing analyses requires a request that includes that work. List proposed experiments separately from completed ones.
- Write the Markdown report without asking for routine confirmation. Preserve original scripts, datasets, logs, and reports. Add an index link only if requested or required by the project's documented convention.
- If the folder is unavailable or the working directory contains unrelated projects with no identifiable target, request the project location. Otherwise make useful progress before asking about an ambiguity; explicitly state the review scope when no narrow question was supplied.

## 1. Find the project record before exploring the experiments

Read applicable `AGENTS.md` instructions and make a bounded inventory of the root and likely documentation directories. Prefer `rg --files` for discovery and `rg -n` for targeted text searches. Do not dump large data directories or entire notebooks into context.

Look first for an index or recording document: `INDEX.md`, `README.md`, experiment registries, research logs, lab notebooks, `HANDOFF.md`, progress notes, and any existing experience report. Names are hints; identify which document actually maps the work. Follow Obsidian links or other local link conventions if present.

Use this record to establish:

- The biological question and intended computational task.
- The experiment sequence, branch points, run identifiers, and previous conclusions.
- Links to relevant code, configurations, datasets, outputs, figures, and reports.
- Which experiments matter to the user's current request.

The index is a navigation map and an account of intent, not proof of the results. Verify its important claims against the linked artifacts. If several indexes conflict, record the discrepancy and resolve it using run identities and evidence. File modification time alone does not establish experiment chronology or authority.

If no useful index exists, construct a small project map from filenames, manifests, and targeted reads. State that navigation was reconstructed; do not invent an authoritative history. A missing link or unreadable artifact limits coverage but need not stop the rest of the review.

## 2. Trace the evidence for each relevant experiment

Follow the chain appropriate to the question:

`research question → experiment record → script/configuration → execution record → result artifact → interpretation`

Not every link will exist. Track missing links rather than filling them with assumptions. Prioritize the artifacts needed to settle the requested claims; expand the search when a contradiction or broken link requires it.

Build a compact experiment ledger. Preserve existing experiment/run IDs; assign stable report-local IDs only when needed. For each experiment, recover what is material and available:

- Hypothesis, intended change, baseline/control, and recorded success criterion.
- Dataset/version, organism or biological system, assay, sample inclusion, preprocessing, labels, split, and unit of evaluation.
- Algorithm variant, relevant parameters, script/configuration, recorded code revision, seed, and environment when relevant to the outcome.
- Execution status, output metrics with units and direction, biological observations, and provenance.

Inspect the code that explains a result, especially transformations, splitting, labels, losses, metric calculations, and output writing. Code expresses possible or intended behavior; it does not prove that a particular run executed it. Current code or the current Git commit may differ from the code that generated archived results. Record that uncertainty when provenance cannot be established.

Use data summaries, tables, logs, and saved figures as appropriate. Inspect a figure when its visual structure supports a claim; a filename or caption alone is insufficient. Treat saved notebook outputs as artifacts with their own provenance, not as evidence that the current cells were rerun. Use format-appropriate readers; do not execute project code just to read its outputs.

Keep source IDs and precise locators while reading. A material result or explanation in the final report must point to evidence a future agent can locate: path plus run/table row, configuration key, code lines, notebook cell, PDF page, or figure panel. Use relative Markdown links where possible. Distinguish direct artifact inspection from a result merely reported in a summary.

## 3. Evaluate outcomes and possible explanations

Read [evidence and interpretation](references/evidence-and-interpretation.md) when assessing scientific outcomes or explaining failures. Select the relevant lenses; do not turn the reference into a mandatory checklist for every experiment.

Keep separate judgments for:

1. **Execution:** completed, partial, failed, or unverified.
2. **Computational outcome:** met the stated objective, did not meet it, mixed, or inconclusive.
3. **Biological support:** supported within scope, not supported by this experiment, mixed, inconclusive, or not assessed.

Use the recorded objective and criterion. If none was recorded, describe the observed change and label any reconstructed objective as inferred. Do not invent a threshold or redefine success after seeing the result. Record useful negative and mixed results as carefully as improvements.

For each important finding, separate:

- **Observation:** what an inspected artifact shows, including relevant numbers and conditions.
- **Interpretation:** what those observations support within the tested setting.
- **Possible explanation:** a proposed biological, algorithmic, technical, or evaluation cause.
- **Unresolved evidence:** what prevents a stronger conclusion and what would distinguish the remaining explanations.

Call a cause confirmed only when the evidence isolates it sufficiently, such as a traced execution error or an intervention that changed that factor while controlling relevant alternatives. Otherwise use supported explanation, hypothesis, or unknown, with a short reason. A report's confident wording, a plausible story, or the order of events is not causal verification.

Compare runs only after checking the comparability factors that matter to the claim. If datasets, splits, preprocessing, labels, metrics, or tuning budgets differ, report those differences and qualify the comparison. Do not silently combine unlike runs into a ranking or attribute their differences entirely to the algorithm.

## 4. Consolidate reusable experience

Group findings by research question, algorithm component, evaluation issue, or biological assumption. Use chronology only where it explains a decision or change. Merge duplicate lessons while retaining their supporting and contradicting experiment IDs.

Each retained lesson should specify:

- **When it applies:** biological setting, data conditions, algorithm stage, or recognizable symptom.
- **What to do or check next time:** a concrete decision or diagnostic.
- **Why:** the observation and supporting source/experiment IDs.
- **How certain it is:** evidence strength, limitations, and counterexamples.

Keep untested explanations in open questions, not among established practices. Separate a scoped, reusable lesson from an interesting one-off observation. Do not convert a dataset-specific result into a universal biological rule, or turn repeated anecdotes into stronger causal evidence just by counting them.

This skill produces project experience documentation. It does not automatically edit global instructions, create additional skills, or claim that future agents will remember the report without reading it.

## 5. Write a report that supports later retrieval

Read [report format](references/report-format.md) and adapt it to the project. Always retain the review scope, consolidated findings, evidence links, reusable lessons, and unresolved questions. Include only the experiment detail needed to understand or audit those findings.

Make the report self-contained: identify the project root, reviewed question, primary index, review date, evidence cutoff if known, and important coverage gaps. Include a short retrieval map so a future agent can locate lessons by biological question, algorithm component, or symptom. The report must distinguish evidence actually reviewed from material merely discovered.

If an experience report already exists, read it before updating. Preserve useful IDs and evidence links, merge duplicate findings, and explicitly mark materially revised conclusions as superseded with the new evidence. Do not silently erase a contradiction or append a second copy of the whole history. Follow an established append-only convention when the project has one.

Write direct, neutral prose. Preserve effect sizes, units, sample counts, and uncertainty when available. Use “not recorded,” “not inspected,” or “unavailable” for missing evidence; none means zero, failure, or absence of a biological effect. External literature may contextualize an interpretation, but it cannot establish what happened in this project. Consult it only when needed for the requested explanation, cite it separately, and label the distinction.

## 6. Verify and return

Before delivering:

- Verify the material claims against their cited artifacts, including run identity, numeric transcription, metric direction, and sample unit.
- Check local links and locators where possible. Clearly label missing or inaccessible sources.
- Check that explanations have appropriate evidence status and that lessons retain their conditions and exceptions.
- Check that the report is useful without the chat and does not imply unperformed reruns or broader coverage than was achieved.

Return the report path with a brief statement of its scope and any material limitation. Do not represent a document review as an independently reproduced experiment.

## Design influences

This workflow adapts the record-and-consolidate approach of [self-improvement](https://github.com/pskoett/pskoett-ai-skills/blob/main/skills/self-improvement/SKILL.md), selective extraction of verified knowledge from [Claudeception](https://github.com/blader/Claudeception/blob/main/SKILL.md), and validation and pruning ideas from [self-improving-skills](https://github.com/chemny/self-improving-skills/blob/main/SKILL.md). The instructions here are self-contained; these links are provenance, not dependencies for routine use.
