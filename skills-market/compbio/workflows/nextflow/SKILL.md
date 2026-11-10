---
name: nextflow
domain: compbio
description: Create, review, or debug Nextflow DSL2 workflows, process/channel contracts, sample sheets, resources, containers, execution profiles, and resume behavior, including nf-core workflows.
license: MIT license
metadata:
  version: "1.0.1"
  skill-author: Eric Yiru
---

# Nextflow workflows

Inspect the installed Nextflow version, DSL/parser mode, workflow/modules, parameters/schema, sample sheet, profiles, executor, and intended outputs. Follow the project's module and configuration conventions.

## Channel and process contracts

- Define the sample/metadata key and data shape at every channel boundary. A paired-file factory typically emits a tuple of sample identifier and a list of read paths; the process input must destructure that tuple rather than accepting it as an unrelated single `path`.
- Preserve pairing and sample identity through mapping, grouping, joins, branches, and emitted outputs. Queue and value channels have different consumption behavior; two unrelated queue inputs are not an automatic stable sample-wise join.
- Use valid parameter access such as `params.reads`; validate required reference/index/annotation parameters before task launch. Do not reference an undefined GTF or pass an index prefix as though it were a single staged file without accounting for all index files.
- Declare outputs that commands actually create in the task work directory. Quote shell paths appropriately and preserve task exit failures. A published filename is not proof that the data format is correct.
- Select assay-aware processing: bulk RNA alignment/counting does not include droplet barcode/UMI extraction, chemistry, cell calling, or a complete single-cell count matrix.

## Execution and provenance

Use supported DSL2 process/workflow composition. Pin pipeline/module/container versions, select the actual profile and executor, and specify resources in configuration. Do not assume a named SLURM/cloud profile exists in every repository or copy unsupported flags such as `-dockerize`.

Keep work/cache state for `-resume` when resumption matters. A resumed task must still match relevant inputs, scripts, and execution context; do not promise that cache reuse proves scientific validity. Publishing outputs and deleting work directories are separate operations with overwrite/concurrency implications.

For an nf-core workflow, read its versioned schema and documentation, choose a compatible assay/reference, and use its supplied test profile when suitable. Do not automatically pull or run an unrelated pipeline.

## Verify

Inspect channel contents and sample accounting on a tiny fixture; use the installed syntax/schema validation and preview facilities when available. Run a bounded local/test profile for command changes and verify expected outputs, pairing, task logs, trace/report, and any QC contract.

Report pipeline revision, parameters, environment/profile, output directory, execution versus preview scope, and failed/skipped tasks. Do not call a pipeline complete when the terminal targets omit the requested analysis.

Consult [official Nextflow documentation](https://www.nextflow.io/docs/latest/) and the selected pipeline's versioned documentation.
