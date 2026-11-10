# Documentation

This directory is the documentation hub for the repository.

Use the top-level [README.md](../README.md) for repository overview, installation, and contributor-facing setup. Use the pages here for structured catalogs and example workflows.

## Layout

| Section | Purpose |
|---------|---------|
| [`catalogs/`](./catalogs/) | Domain-by-domain skill inventories with links to the source `SKILL.md` files |
| [`guides/`](./guides/) | Worked examples and practical usage notes |
| [`audits/`](./audits/) | Dated skill reviews, evidence, and prioritized update plans |

## Catalogs

| Domain | Coverage |
|--------|----------|
| [Document Skills](./catalogs/document-skills.md) | Office workflows, design, web, and skill-building utilities |
| [Frontend Skills](./catalogs/font-end.md) | Website maintenance and repo-specific frontend upkeep skills |
| [AI/ML Skills](./catalogs/ai-ml.md) | Model identifiability, deep learning, LLM tooling, and training infrastructure |
| [Python Skills](./catalogs/python.md) | Python library engineering, quality, packaging, and release workflows |
| [Computational Biology Skills](./catalogs/computational-biology.md) | Single-cell, multi-omics, spatial omics, structural biology, databases, and workflow tools |
| [Writing Skills](./catalogs/writing.md) | Academic editing, technical English, Marp slides, LaTeX, and note-taking |

## Guides

| Guide | Scope |
|-------|-------|
| [Workflow Examples](./guides/examples.md) | Example analysis and pipeline snippets, currently focused on computational biology |

## Audits

- [2026-11-10: implemented improvements](./audits/2026-11-10-improvements.md) — all 111 decisions, version changes, helper repairs, validation, and remaining limits; [structured ledger](./audits/2026-11-10-improvements.json).
- [2026-11-10: all 111 active skills](./audits/2026-11-10-active-skills-audit.md) — individual findings, update priorities, version baseline, and validation limits.
- [Version and conflict policy](./guides/architecture.md#skill-versions-and-conflicts) — version locations, bump rules, and comparing conflicting copies.

## Documentation Conventions

- Catalog pages should link to real repository paths, not hypothetical examples.
- Keep catalogs inventory-oriented; detailed operational guidance belongs in the individual skills.
- Add new domain pages under `catalogs/` and practical walkthroughs under `guides/`.
