---
name: snakemake
domain: compbio
description: Create, inspect, or debug Snakemake rules, dependency graphs, configuration, environments, resources, and execution profiles for a reproducible computational workflow.
license: MIT license
metadata:
  version: "1.0.1"
  skill-author: Eric Yiru
---

# Snakemake workflows

Read the installed Snakemake version, existing Snakefile/modules, config, sample sheet, environments, profiles, and intended final targets. Preserve the project's execution conventions.

## Rule and scientific contracts

- Define final deliverables in the default target, then trace dependencies backward. Every declared output must be produced with the expected path and format by its rule; unused rules are not part of a completed pipeline.
- Specify named inputs/outputs, constrained wildcards, parameters, logs, threads, and resources. Keep sample identity and read pairing explicit. Use proper shell quoting, including Snakemake's `:q` formatting where appropriate.
- Validate config/sample metadata before launching work. Separate reference FASTA, aligner index, annotation, organism/assembly, assay, and library layout; a tool name is not enough to choose a pipeline.
- A SAM stream does not become BAM by changing its filename. An aligner command needs its actual index/reference and conversion/sorting steps if BAM is the declared output. Verify each tool's real output names.
- For droplet single-cell assays, preserve barcode/UMI extraction, chemistry, cell calling, and count semantics. Bulk alignment plus featureCounts is not a complete generic scRNA-seq pipeline.

## Environments and execution

Pin the relevant tool/environment or container revisions. Use installed executor/storage plugins and profiles supported by this Snakemake version; do not copy retired cloud/remote flags blindly. Set resources for the actual executor and bounded local cores for local runs.

Keep temporary/intermediate outputs, directory outputs, checkpoints, and protected outputs deliberate. Avoid cleanup, overwrite, rerun-all, or unlock operations unless the actual state justifies them and they fit the task. Do not discard a running workflow's lock.

## Verify

1. Run the version's lint and a dry run for the requested targets. Inspect the DAG for missing steps, wildcard expansion, duplicate outputs, and unintended samples.
2. Exercise a small representative fixture when rule commands or file contracts changed. Check file content/format and promised QC metrics, not only process exit.
3. Record environment, config, sample/reference versions, commands, output locations, and failed/incomplete jobs. A dry run validates planning, not the scientific result or runtime tool compatibility.

Consult [official Snakemake documentation](https://snakemake.readthedocs.io/) for version-specific rules, modules, profiles, plugins, and CLI options. Reuse a maintained assay-specific workflow when appropriate instead of labeling an incomplete sketch as a full analysis.
