# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an **AI Skills repository** — a collection of skills for AI agents organized around a four-layer architecture. The repo serves as a **skills-market** (what skills exist), **registry** (stable identity), **deployments** (machine install plans), and **taskpacks** (workflow-specific bundles).

Skills cover document workflows, website maintenance, Python library development, AI/ML, computational biology, and writing tools.

## Core Design Principle

**Do not use folder path as the real identity.** Folder paths are human-readable organization only. The registry is the source of truth.

```yaml
# Bad: path as identity
skills:
  - compbio-skills/single-cell/analysis/scanpy

# Good: stable ID resolves through registry
skills:
  - scanpy
```

```yaml
# registry/skills.yaml
scanpy:
  id: scanpy
  canonical_path: skills-market/compbio/single-cell/analysis/scanpy
  domain: compbio
  status: active
```

This decoupling lets you reorganize folders without breaking deployments.

## Architecture: Four Layers

```text
skills-market/   ← canonical skill library (human-readable org)
registry/        ← source of truth: stable IDs, paths, metadata
deployments/     ← machine/profile install plans
taskpacks/      ← project/workflow-specific skill bundles
```

## Repository Structure

```text
ai_skills/
  README.md
  CLAUDE.md
  pyproject.toml

  skills-market/
    core/
      dev/
        skill-creator/
        skill-seekers/
      documentation/
      security/
        security-audit/
        bitwarden/
      performance/
        performance/
      usage/

    programming/
      python/
        project-setup/
        code-quality/
        testing-strategy/
        api-design/
        documentation/
        packaging/
        release-management/
        cli-development/
        community/
        library-review/
        jupyter/
        sqlite/

    ai-ml/
      deep-learning/
        pytorch/
      llm/
        transformers/
        huggingface-hub/
        peft/
        trl/
        bitsandbytes/
        cursor-usage-checker/
      training/
        pytorch-lightning/
        accelerate/
        datasets/
        deepspeed/
      utility/
        token-usage-checker/
        provider-usage-checker/

    compbio/
      single-cell/
        analysis/
          scanpy/
          seurat/
          scvi-tools/
          anndata/
        integration/
          seurat-v5/
          harmony/
          scanorama/
          bbknn/
        visualization/
          cellxgene/
          cellxgene-census/
      spatial-omics/
        analysis/
          squidpy/
          giotto/
          spatialdata/
        visualization/
          vitessce/
        platforms/
          stereo-seq/
          visium/
      multiomics/
        scRNA-seq/
          pydeseq2/
        scATAC-seq/
          archr/
          signac/
        integration-tools/
          scribble/
        metabolomics/
          metabolomics-workbench/
        proteomics/
          uniprot/
      databases/
        kegg/
        reactome/
        geo/
        human-cell-atlas/
        ensembl/
      workflows/
        snakemake/
        nextflow/

    writing/
      academic/
        academic-writing-editor/
        humanizer/
        humanizer-zh/
      literature/
        zotpilot/
      latex/
        latex-writing/
        compile-latex/
      obsidian/
        obsidian-markdown/
        obsidian-cli/
        obsidian-bases/
        json-canvas/
        defuddle/
        wiki-keeper/

    documents/
      office/
        officecli/
        officecli-docx/
        officecli-pptx/
        officecli-xlsx/
      formats/
        xlsx/
        docx/
        pptx/
        pdf/
      design/
        algorithmic-art/
        brand-guidelines/
        canvas-design/
        frontend-design/
        theme-factory/
        web-artifacts-builder/
        webapp-testing/
      collaboration/
        doc-coauthoring/
        internal-comms/
      media/
        imgur-cli/
        slack-gif-creator/

    agents/
      claude-code/
      codex/
      hermes-agent/
      opencode/
      ag-ui/
      mcp/
        mcp-builder/
      guidelines/
        karpathy-guidelines/

    frontend/
      site-maintenance/
        page-keeper/
        chen-academic-page-maintainer/

    projects/
      codebti/

    experimental/
      incubating/
      deprecated/
      unregistered/

  registry/
    skills.yaml          # every skill: id, canonical_path, domain, status, tags, profiles, taskpacks
    aliases.yaml         # old_path → skill id (for backward compatibility)
    deprecated.yaml      # deprecated skills with replacement IDs
    missing.yaml         # expected-but-absent skills with proposed paths
    schema.skill.yaml    # JSON Schema for skill entries
    schema.profile.yaml  # JSON Schema for deployment profiles

  deployments/           # machine profiles
    base.yaml
    macos-personal.yaml
    research-server.yaml
    gpu-server.yaml
    hpc.yaml
    writing-workstation.yaml
    frontend-workstation.yaml
    agent-coding.yaml

  taskpacks/             # workflow/project bundles
    paper-writing.yaml
    document-export.yaml
    zotpilot-literature-map.yaml
    pytorch-model-dev.yaml
    llm-finetuning.yaml
    single-cell-analysis.yaml
    spatial-omics-analysis.yaml
    bio-databases.yaml
    workflow-engineering.yaml
    codebti.yaml
    feast.yaml
    thesis-defense.yaml

  scripts/
    migrate_skills.py
    validate_registry.py
    validate_profiles.py
    install_profile.py
    list_skills.py
    resolve_alias.py

  docs/
    architecture.md
    migration-plan.md
    naming-conventions.md
    profile-design.md
    skill-authoring.md
```

## Registry Schema

Each skill in `registry/skills.yaml`:

```yaml
scanpy:
  id: scanpy
  name: Scanpy
  canonical_path: skills-market/compbio/single-cell/analysis/scanpy
  old_paths:
    - compbio-skills/single-cell/analysis/scanpy
  domain: compbio
  category: single-cell-analysis
  tags:
    - single-cell
    - anndata
    - preprocessing
    - visualization
  supported_hosts:
    - macos
    - linux
    - server
    - hpc
  profiles:
    - single-cell-analysis
    - spatial-omics-analysis
    - research-server
  taskpacks:
    - single-cell-analysis
    - spatial-omics-analysis
  install_weight: medium
  dependencies: []
  status: active
```

### Status values

```yaml
status:
  - active        # available for use
  - experimental  # works but may change
  - deprecated    # use replacement instead
  - missing       # expected but not yet implemented
  - alias-only    # only exists as an alias
```

### Install weights

```yaml
install_weight:
  - light          # trivial, fast
  - medium         # moderate
  - heavy          # large or slow
  - host-specific  # GPU/HPC required
```

## Deployment Profiles

Profiles describe **machines**, not tasks. All profiles extend `base`.

### `base.yaml` — install everywhere

```yaml
id: base
description: Minimal general skills for all machines.
skills:
  - project-setup
  - code-quality
  - testing-strategy
  - security-audit
  - documentation
  - performance
  - cli-development
  - token-usage-checker
  - provider-usage-checker
```

### `macos-personal.yaml` — extends base

Personal Mac: writing, Obsidian, Office, frontend, academic page.

### `research-server.yaml` — extends base

General Linux research server: Python, data, computational biology.

### `gpu-server.yaml` — extends research-server

GPU machine: PyTorch, LLM, large model training.

### `hpc.yaml` — extends base

HPC cluster: workflow reproducibility.

### `writing-workstation.yaml` — extends base

Writing-heavy machine: academic, literature, LaTeX, Obsidian.

### `frontend-workstation.yaml` — extends base

Web artifacts, UI, academic page, frontend development.

### `agent-coding.yaml` — extends base

Coding-agent environment: Codex, Claude Code, OpenCode, MCP, agent UI.

## Taskpacks

Taskpacks describe **workflows/projects**, not machines. They can reference other taskpacks via `includes` (resolved into skill IDs internally).

### `paper-writing.yaml`

Academic paper, thesis, proposal, literature review.

### `document-export.yaml`

Office, PDF, Word, PowerPoint, Excel, export workflow.

### `zotpilot-literature-map.yaml`

Local literature recommendation, embedding map, paper clustering, review system.

### `pytorch-model-dev.yaml`

PyTorch model development, training, debugging, optimization.

### `llm-finetuning.yaml`

LLM fine-tuning and lightweight adaptation.

### `single-cell-analysis.yaml`

scRNA-seq analysis, integration, visualization, annotation.

### `spatial-omics-analysis.yaml`

Spatial transcriptomics and spatial omics analysis.

### `bio-databases.yaml`

Biological database access and annotation.

### `workflow-engineering.yaml`

Reproducible computational biology workflow engineering.

### `codebti.yaml`

CODEBTI project-specific bundle.

## Skill ID Naming Convention

Use stable kebab-case IDs. IDs must be unique, lowercase, kebab-case, and **never embed path separators**.

```text
# Good
scanpy
scvi-tools
latex-writing
compile-latex
cellxgene-census
provider-usage-checker

# Bad
writing/latex/Latex_writing
compbio_scanpy
skill_54_scanpy
```

Rules:
1. lowercase only
2. kebab-case only
3. no path separators in IDs
4. avoid category prefixes unless needed
5. ID must not change when folder changes

## Migration: Legacy Path Support

Old paths are preserved in `old_paths[]` and resolved via `registry/aliases.yaml`. Profiles and taskpacks reference **skill IDs**, never folder paths.

During migration, old paths remain valid until the compatibility window closes.

## Adding New Skills

1. Create the skill directory under `skills-market/<domain>/.../`
2. Add `SKILL.md` with required frontmatter
3. Add entry to `registry/skills.yaml` with a unique ID
4. If the skill has old paths, add them to `old_paths[]`
5. Register in relevant profiles and/or taskpacks by ID
6. Run `scripts/validate_registry.py` to verify

## Modifying Existing Skills

Edit the `SKILL.md` file directly. To move a skill to a new path:
1. Update `canonical_path` in `registry/skills.yaml`
2. Keep old paths in `old_paths[]` for compatibility
3. Validate before committing

## Configuration Files

- `registry/skills.yaml`: All skill definitions and metadata
- `registry/aliases.yaml`: Legacy path → skill ID mappings
- `registry/deprecated.yaml`: Deprecated skills with replacements
- `registry/missing.yaml`: Expected-but-absent skills
- `deployments/*.yaml`: Machine install plans
- `taskpacks/*.yaml`: Workflow-specific bundles
- `.claude-plugin/marketplace.json`: Claude Code plugin marketplace
- `.claude/settings.local.json`: Local user settings

## Validation Scripts

```bash
# Dry-run migration
python scripts/migrate_skills.py --dry-run

# Apply migration
python scripts/migrate_skills.py --apply

# Validate registry integrity
python scripts/validate_registry.py

# Validate all profiles
python scripts/validate_profiles.py

# List skills by domain/tag/profile
python scripts/list_skills.py --domain compbio
python scripts/list_skills.py --profile gpu-server

# Resolve a skill ID or legacy path
python scripts/resolve_alias.py scanpy
python scripts/resolve_alias.py compbio-skills/single-cell/analysis/scanpy
```
