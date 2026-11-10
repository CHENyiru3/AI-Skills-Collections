# AI Skills — Eric Yiru's Personal Library

> **111 active skills** for Claude Code, Codex, and AI coding agents.
> Computational biology · Deep learning · Academic writing · Document automation · and more.

---

## What Is This

A **personal, production-grade skills library** for AI coding agents.
Each skill is a `SKILL.md` file that tells the agent *how* to do something well — not just *that* it can be done.

When you ask me to analyze a spatial transcriptomics dataset, fine-tune a Llama model, draft a LaTeX Methods section, or set up a Python library — I already know the right approach. These skills are how.

---

## Skills at a Glance

```
compbio (36)  ████████████████████████████████████  single-cell · spatial omics · multi-omics · structural biology · databases · workflows
ai-ml  (13)  █████████████  identifiability theory · JEPA · deep learning · LLM fine-tuning · distributed training
programming (13) █████████████  project scaffolding · testing · packaging · API design
writing  (14)  ██████████████  academic editing · Marp slides · LaTeX · Zotero · Obsidian
documents (20) ████████████████████  office automation · scientific figures · design · web artifacts
agents   (4)  ████  Claude Code · Codex · MCP · agent guidelines
platforms (6) ██████  GitHub workflows · code review · PR management
frontend  (2) ██  site maintenance
core     (3) ███  skill authoring · skill auditing · security
```

---

## Skill versions

Every active skill has a quoted `metadata.version` in `SKILL.md`, matching its `version` in `registry/skills.yaml`. Run `python scripts/list_skills.py` to list versions. Previously unversioned skills start at the local baseline `1.0.0`; existing versions are preserved.

Bump PATCH for compatible fixes, MINOR for compatible capabilities, and MAJOR for incompatible changes. Compare actual file differences before resolving conflicts, including when two copies have the same version. See the [version and conflict policy](docs/guides/architecture.md#skill-versions-and-conflicts) and the [individual audit of all 111 active skills](docs/audits/2026-11-10-active-skills-audit.md).

The [implemented improvements](docs/audits/2026-11-10-improvements.md) cover all 111 active skills: 108 updated and 3 retained. The report includes individual version changes, validation, content hashes, and unresolved limits. Review the PyDESeq2 2.0.0 CLI change before updating an existing copy; Scribble remains an identification-only entry with an unverified package identity.

## By Domain

### Computational Biology — 36 skills

Single-cell RNA-seq, spatial omics, multi-omics integration, structural biology, databases, and workflow engineering.

| Category | Skills |
|---------|--------|
| Single-cell analysis | `scanpy`, `seurat`, `scvi-tools`, `anndata` |
| H5AD interchange | `anndatar`, `schard` |
| Trajectory analysis | `monocle3` |
| Integration | `seurat-v5`, `harmony`, `scanorama`, `bbknn` |
| Visualization | `cellxgene`, `cellxgene-census` |
| Spatial omics | `squidpy`, `giotto`, `spatialdata`, `vitessce` |
| Platforms | `stereo-seq` |
| Multi-omics | `pydeseq2`, `archr`, `signac`, `scribble`, `uniprot`, `metabolomics-workbench` |
| Structural biology | [`chimerax-mcp`](skills-market/compbio/structural-biology/chimerax-mcp/SKILL.md) |
| Databases | `kegg`, `reactome`, `geo`, `ensembl`, `human-cell-atlas` |
| Workflows | `snakemake`, `nextflow` |
| Expert workflows | `draft-spatial-methods`, `explain-bio-dl-model`, `critique-bio-manuscript`, [`computational-biology-retrospective`](skills-market/compbio/expert-workflows/computational-biology-retrospective/SKILL.md) |

### AI / ML — 13 skills

Latent-model identifiability, JEPA model development, deep learning, LLM fine-tuning, and distributed training infrastructure.

| Category | Skills |
|---------|--------|
| Model theory | [`latent-identifiability`](skills-market/ai-ml/theory/latent-identifiability/SKILL.md) |
| Deep learning | `pytorch`, [`jepa-pytorch-development`](skills-market/ai-ml/deep-learning/jepa-pytorch-development/SKILL.md) |
| LLM ecosystem | `transformers`, `huggingface-hub`, `peft`, `trl`, `bitsandbytes`, `browser-use` |
| Training | `pytorch-lightning`, `accelerate`, `datasets`, `deepspeed` |

### Programming / Python — 13 skills

Python library development from zero to production.

| Category | Skills |
|---------|--------|
| Foundation | `project-setup`, `code-quality`, `testing-strategy`, `documentation` |
| Distribution | `packaging`, `release-management`, `cli-development` |
| Quality | `performance`, `api-design`, `library-review`, `community` |
| Utilities | `sqlite`, `jupyter` |

### Writing — 14 skills

Academic writing, literature review, LaTeX, and Obsidian knowledge management.

| Category | Skills |
|---------|--------|
| Academic | `academic-writing-editor`, `humanizer`, `humanizer-zh` |
| Technical English | [`asd-ste100`](skills-market/writing/technical/asd-ste100/SKILL.md) |
| Literature | `zotpilot` |
| Academic slides | [`duke-nus-marp`](skills-market/writing/presentations/duke-nus-marp/SKILL.md) |
| LaTeX | `latex-writing`, `compile-latex` |
| Obsidian | `obsidian-markdown`, `obsidian-cli`, `obsidian-bases`, `json-canvas`, `defuddle`, `wiki-keeper` |

### Documents — 20 skills

Office automation, design, and media.

| Category | Skills |
|---------|--------|
| Office | `officecli`, `officecli-docx`, `officecli-pptx`, `officecli-xlsx` |
| Formats | `docx`, `pptx`, `xlsx`, `pdf` |
| Design | `frontend-design`, `canvas-design`, `theme-factory`, `brand-guidelines`, `algorithmic-art`, `web-artifacts-builder`, `webapp-testing`, [`scientific-figure-polish`](skills-market/documents/design/scientific-figure-polish/SKILL.md) |
| Collaboration | `doc-coauthoring`, `internal-comms` |
| Media | `imgur-cli`, `slack-gif-creator` |

### Agents — 4 skills

Coding agents, MCP development, and behavioral guidelines.

| Category | Skills |
|---------|--------|
| Coding agents | `claude-code`, `codex` |
| MCP | `mcp-builder` |
| Guidelines | `karpathy-guidelines` |

### Platforms — 6 skills

GitHub workflow integration.

| Category | Skills |
|---------|--------|
| GitHub | `github-auth`, `github-code-review`, `github-issues`, `github-pr-workflow`, `github-repo-management`, [`github-codebase-inspection`](skills-market/platforms/github/codebase-inspection/SKILL.md) |

### Frontend — 2 skills

Website maintenance.

| Category | Skills |
|---------|--------|
| Site maintenance | `page-keeper`, `chen-academic-page-maintainer` |

### Core — 3 skills

Security, performance tooling, and skill authoring.

| Category | Skills |
|---------|--------|
| Skill authoring | `skill-creator`, [`skill-cutter`](skills-market/core/dev/skill-cutter/SKILL.md) |
| Security | `security-audit` |

---

## Workflow Bundles (Taskpacks)

Taskpacks group skills by **workflow**, not machine:

| Taskpack | Description |
|---------|-------------|
| `paper-writing` | Academic paper, thesis, literature review |
| `document-export` | Office, PDF, Word, PowerPoint, Excel |
| `single-cell-analysis` | scRNA-seq from raw reads to annotated clusters |
| `spatial-omics-analysis` | Spatial transcriptomics — Squidpy, Giotto, Stereo-seq |
| `llm-finetuning` | LoRA, QLoRA, RLHF, DPO fine-tuning |
| `pytorch-model-dev` | PyTorch model development and optimization |
| `bio-databases` | KEGG, Reactome, GEO, Ensembl, UniProt access |
| `workflow-engineering` | Snakemake and Nextflow pipelines |
| `feast` | Multi-omics integration — RNA, ATAC, proteomics, metabolomics |
| `thesis-defense` | Thesis defense preparation |
| `zotpilot-literature-map` | Literature embedding map and recommendation system |

---

## Architecture

```
skills-market/   canonical skill library (human-readable organization)
archive/         retired skill files and metadata, excluded from active discovery
registry/        source of truth: stable IDs, paths, metadata
deployments/     machine/profile install plans
taskpacks/       workflow-specific skill bundles
scripts/          tooling: validate, migrate, install, query
```

**Core rule**: skills are referenced by **stable ID** (e.g., `scanpy`), never by folder path. The registry is the source of truth. See `docs/guides/architecture.md` for the full design.

---

## License

MIT — see `LICENSE.md`
