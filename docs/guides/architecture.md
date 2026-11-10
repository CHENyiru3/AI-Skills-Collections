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
skills-market/   ← active canonical skill library (human-readable org)
archive/         ← retired skill files and metadata, excluded from active discovery
registry/        ← source of truth: stable IDs, paths, metadata
deployments/     ← machine/profile install plans
taskpacks/      ← project/workflow-specific skill bundles
scripts/         ← tooling layer
```

## Invariants (enforced by CI/validation)

These rules are checked by `scripts/validate_registry.py` and `scripts/check_skill_docs.py`:

1. **Registry is authoritative for current skills.** Every current skill has an entry in `registry/skills.yaml`; retired entries are preserved separately in `archive/registry/skills.yaml`.
2. **Profiles and taskpacks reference skill IDs, never paths.** Use `scanpy`, not `skills-market/compbio/single-cell/analysis/scanpy`.
3. **Active skills must have `SKILL.md`.** `status: active` implies `canonical_path/SKILL.md` exists on disk.
4. **Active canonical paths live only under `skills-market/`.** Retired files live under `archive/` and are excluded from active registries and installation.
5. **Old paths are represented only in `aliases.yaml`.** Do not create new paths outside `skills-market/`.
6. **Deprecated entries are not installable.** They point to the replacement ID.
7. **Missing skills are not installable.** `status: missing` means no `SKILL.md` exists yet.
8. **Marketplace is generated, not hand-maintained.** Run `python scripts/build_marketplace.py` after editing `registry/skills.yaml`. Use `python scripts/build_marketplace.py --check` to verify generated-file agreement, plugin-relative skill paths, containment, and `SKILL.md` existence without writing.
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
  version: "1.0.0"                    # matches SKILL.md metadata.version
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

## Skill Versions and Conflicts

Every active skill carries a quoted `metadata.version` in its `SKILL.md` frontmatter and the same `version` in `registry/skills.yaml`. Use three numeric components, `MAJOR.MINOR.PATCH`, without leading zeros:

```yaml
---
name: example-skill
description: A specific capability and its trigger conditions.
metadata:
  version: "1.0.0"
---
```

Existing version declarations were retained during initial versioning, with `3.0` normalized to `3.0.0`. Previously unversioned skills start at `1.0.0` as a local market baseline; this does not claim an upstream release. Legacy top-level `version` fields were moved to `metadata.version`.

For subsequent edits to instructions, scripts, references, UI metadata, or assets, bump PATCH for compatible corrections, MINOR for compatible added capabilities, and MAJOR for incompatible behavioral or file-contract changes. Update the skill and registry together. Purely external catalog edits do not change a skill's version. The marketplace's own plugin/package version is separate from individual skill versions.

Use `python scripts/list_skills.py` to see versions, or `--format json` for structured output. `validate_registry.py` checks the version format; `check_skill_docs.py` also checks that the frontmatter and registry agree.

`validate_registry.py` rejects duplicate YAML keys so a repeated skill ID or field cannot silently replace another value. The [2026-11-10 implementation ledger](../audits/2026-11-10-improvements.json) records per-skill versions, changed files, and folder content hashes for that update.

When two copies conflict, first compare their stable IDs and versions, then inspect their actual differences. A higher version indicates intended release order, not permission to overwrite local work. Different content at the same version requires review and a version bump after reconciliation. Do not infer the newer release from file modification times or compare version strings lexicographically.

## Archiving and Restoring Skills

The active registry, catalogs, deployment profiles, taskpacks, and generated marketplace contain current skills only. Keep retired names and recovery records inside `archive/`; do not add archived entries to the active registry with a new lifecycle status.

To archive a skill:

1. Move its complete folder from `skills-market/<relative-path>` to `archive/skills/<relative-path>`, preserving scripts, references, and assets.
2. Save its full registry entry in `archive/registry/skills.yaml`, wrapped with `archived_on`, `reason`, and `archived_path`. Keep the original entry under `original_entry`. For an already missing skill, use `archived_path: null`; do not create placeholder content.
3. Remove the entry from `registry/skills.yaml`. Move its legacy aliases to `archive/registry/aliases.yaml`.
4. Remove references from deployment profiles and active taskpacks, and record removed skill IDs by source file in `archive/registry/removed-references.yaml`. Move a taskpack dedicated to the retired skill into `archive/taskpacks/`.
5. Remove its listings from README, catalogs, and architecture examples; update active counts. Preserve historical migration logs.
6. Regenerate the marketplace and run the registry, skill-documentation, and profile validators.

To restore a skill, move the archived folder back to its original `canonical_path`, return `original_entry` to the active registry, and restore the needed aliases and profile/taskpack references. Add matching registry and frontmatter versions if the archived record predates versioning. A missing record needs a real `SKILL.md` before it can become active. Update catalogs and counts, regenerate the marketplace, validate, then remove the restored record from the archive manifest.

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
| `projects` | Project-specific bundles | Project-specific workflows |
| `writing` | Academic, literature, notes | zotpilot, latex-writing |
