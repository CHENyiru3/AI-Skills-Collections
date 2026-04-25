# Architecture Guide

This document describes the architecture of the `ai_skills` repository — a registry-first, multi-layer system for managing AI agent skills.

## Core Design Principle

**The registry is the source of truth. Folder paths are human-readable organization only.**

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
  status: active
```

This decoupling lets you reorganize folders without breaking deployments.

## Four-Layer Architecture

```text
skills-market/   ← canonical skill library (human-readable org)
registry/        ← source of truth: stable IDs, paths, metadata
deployments/     ← machine/profile install plans
taskpacks/      ← project/workflow-specific skill bundles
scripts/         ← tooling layer
```

## Invariants (enforced by CI/validation)

These rules are checked by `scripts/validate_registry.py` and `scripts/check_skill_docs.py`:

1. **Registry is authoritative.** Every skill has an entry in `registry/skills.yaml`.
2. **Profiles and taskpacks reference skill IDs, never paths.** Use `scanpy`, not `skills-market/compbio/single-cell/analysis/scanpy`.
3. **Active skills must have `SKILL.md`.** `status: active` implies `canonical_path/SKILL.md` exists on disk.
4. **Canonical paths live only under `skills-market/`.** No skill is installed outside this directory.
5. **Old paths are represented only in `aliases.yaml`.** Do not create new paths outside `skills-market/`.
6. **Deprecated entries are not installable.** They point to the replacement ID.
7. **Missing skills are not installable.** `status: missing` means no `SKILL.md` exists yet.
8. **Marketplace is generated, not hand-maintained.** Run `python scripts/build_marketplace.py` after editing `registry/skills.yaml`.
9. **Deployment profiles describe machines.** Use `deployments/` for machine-level install plans (e.g., `gpu-server.yaml`, `macos-personal.yaml`).
10. **Taskpacks describe workflows/projects.** Use `taskpacks/` for task-specific bundles (e.g., `single-cell-analysis.yaml`, `paper-writing.yaml`).
11. **Skill IDs are unique, lowercase, kebab-case.** No path separators in IDs.
12. **All aliases resolve to a known skill ID.** `aliases.yaml` must not reference unknown skills.

## Directory Layout

```
ai_skills/
├── skills-market/           # canonical skill library
│   ├── agents/             # coding agents & protocols
│   ├── ai-ml/              # deep learning & LLM
│   ├── compbio/            # computational biology
│   ├── core/               # security, performance, skill authoring
│   ├── documents/          # office, formats, design, media
│   ├── frontend/            # site maintenance
│   ├── platforms/           # platform integrations (GitHub, etc.)
│   ├── programming/         # Python library development
│   ├── projects/           # project-specific bundles
│   └── writing/            # academic, literature, LaTeX, Obsidian
│
├── registry/               # source of truth
│   ├── skills.yaml         # all skill definitions
│   ├── aliases.yaml         # old path → skill ID
│   ├── deprecated.yaml      # deprecated entries
│   ├── missing.yaml         # planned but not yet implemented
│   ├── schema.skill.yaml    # JSON Schema for skill entries
│   └── schema.profile.yaml  # JSON Schema for profiles
│
├── deployments/             # machine install profiles
│   ├── base.yaml            # always installed
│   ├── macos-personal.yaml
│   ├── research-server.yaml
│   ├── gpu-server.yaml
│   ├── hpc.yaml
│   ├── writing-workstation.yaml
│   ├── frontend-workstation.yaml
│   └── agent-coding.yaml
│
├── taskpacks/                # workflow/project bundles
│   ├── paper-writing.yaml
│   ├── document-export.yaml
│   ├── single-cell-analysis.yaml
│   └── ...
│
└── scripts/                 # tooling
    ├── validate_registry.py  # check registry integrity
    ├── validate_profiles.py # check profiles & taskpacks
    ├── check_skill_docs.py  # check SKILL.md quality
    ├── build_marketplace.py  # generate marketplace.json
    ├── list_skills.py        # query skills
    ├── resolve_alias.py      # resolve ID or old path
    ├── migrate_skills.py     # move skills between paths
    └── install_profile.py    # install skills from profile
```

## Registry Schema

Each skill entry in `skills.yaml`:

```yaml
scanpy:
  id: scanpy                          # stable kebab-case ID
  name: Scanpy                        # display name
  canonical_path: skills-market/...   # path relative to repo root
  old_paths:                           # legacy paths (for alias resolution)
    - compbio-skills/single-cell/analysis/scanpy
  domain: compbio
  category: single-cell
  tags: [single-cell, scrna-seq, anndata]
  supported_hosts: [macos, linux, server]
  profiles: [research-server, single-cell-analysis]
  taskpacks: [single-cell-analysis, spatial-omics-analysis]
  install_weight: medium
  dependencies: []
  status: active                      # active | experimental | deprecated | missing
```

## Skill Status Lifecycle

| Status | SKILL.md exists | Installable | Description |
|--------|-----------------|--------------|-------------|
| `active` | Yes | Yes | Available for use |
| `experimental` | Yes | Yes | Works but may change |
| `deprecated` | No | No | Use replacement instead |
| `missing` | No | No | Planned but not yet implemented |
| `alias-only` | No | No | Only exists as a legacy alias |

## Adding a New Skill

1. Create the skill directory: `skills-market/<domain>/.../<skill-id>/`
2. Add `SKILL.md` with required frontmatter (`name`, `description`)
3. Add entry to `registry/skills.yaml`
4. Run `python scripts/build_marketplace.py` to update `marketplace.json`
5. Run `python scripts/validate_registry.py` to verify
6. Run `python scripts/check_skill_docs.py` to verify SKILL.md quality

## Migrating a Skill to a New Path

1. Update `canonical_path` in `registry/skills.yaml`
2. Keep old path(s) in `old_paths[]` for backward compatibility
3. Add alias to `registry/aliases.yaml` if needed
4. Run `python scripts/migrate_skills.py --dry-run` to preview
5. Run `python scripts/migrate_skills.py --apply` to move
6. Update any profiles/taskpacks referencing the old path (they should use IDs, not paths)

## Workflow: From Request to Published Skill

```
User requests → Skill author creates SKILL.md
    → Added to registry/skills.yaml
    → build_marketplace.py updates marketplace.json
    → validate_registry.py + check_skill_docs.py verify
    → Committed to repo
    → Skill available in Claude Code / Codex
```

## Naming Conventions

- **Skill IDs**: lowercase, kebab-case, no path separators
  - Good: `scanpy`, `latex-writing`, `cellxgene-census`, `provider-usage-checker`
  - Bad: `scanPy`, `latexWriting`, `scanpy_skill`, `writing/latex/Latex_writing`
- **Profile/Taskpack IDs**: lowercase, kebab-case
  - Good: `gpu-server`, `single-cell-analysis`, `paper-writing`
  - Bad: `gpuServer`, `SingleCellAnalysis`, `research server`
- **Canonical paths**: relative to repo root, under `skills-market/`
  - Good: `skills-market/compbio/single-cell/analysis/scanpy`
  - Bad: `compbio-skills/single-cell/analysis/scanpy`

## Domain Taxonomy

| Domain | Description | Example Skills |
|--------|-------------|----------------|
| `agents` | Coding agents & protocols | claude-code, codex, mcp-builder |
| `ai-ml` | Deep learning & LLM | pytorch, transformers, peft |
| `compbio` | Computational biology | scanpy, seurat, squidpy |
| `core` | Security, performance, authoring | security-audit, skill-creator |
| `documents` | Office, design, media | officecli, canvas-design |
| `frontend` | Site maintenance | page-keeper |
| `platforms` | Platform integrations | github-* |
| `programming` | Python library development | project-setup, testing-strategy |
| `projects` | Project-specific bundles | codebti |
| `writing` | Academic, literature, notes | zotpilot, latex-writing |
