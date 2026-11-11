# AI Skills — Eric Yiru's Personal Library

> **123 active skills** for Claude Code, Codex, and AI coding agents.
> Computational biology · Deep learning · Academic writing · Document automation · and more.

---

## What Is This

A **personal, production-grade skills library** for AI coding agents.
Each skill is a `SKILL.md` file that tells the agent *how* to do something well — not just *that* it can be done.

When you ask me to analyze a spatial transcriptomics dataset, fine-tune a Llama model, draft a LaTeX Methods section, or set up a Python library — I already know the right approach. These skills are how.

---

## Skills at a Glance

```
compbio (38)  ██████████████████████████████████████  single-cell · spatial omics · multi-omics · structural biology · databases · workflows
ai-ml  (14)  ██████████████  VI methods · identifiability · JEPA · deep learning · LLM training
programming (13) █████████████  project scaffolding · testing · packaging · API design
writing  (14)  ██████████████  academic editing · Marp slides · LaTeX · Zotero · Obsidian
documents (20) ████████████████████  office automation · scientific figures · design · web artifacts
agents   (7)  ███████  Claude Code · Codex · MCP · handoffs · backups · agent guidelines
platforms (10) ██████████  GitHub workflows · Google Workspace CLI · Drive transfers
frontend  (2) ██  site maintenance
core     (5) █████  skill authoring · auditing · security · research workflows
```

---

## Skill versions

Every active skill has a quoted `metadata.version` in `SKILL.md`, matching its `version` in `registry/skills.yaml`. Run `python scripts/list_skills.py` to list versions. Previously unversioned skills start at the local baseline `1.0.0`; existing versions are preserved.

Bump PATCH for compatible fixes, MINOR for compatible capabilities, and MAJOR for incompatible changes. Compare actual file differences before resolving conflicts, including when two copies have the same version. See the [version and conflict policy](docs/guides/architecture.md#skill-versions-and-conflicts) and the [individual audit of the 111 skills reviewed on 2026-11-10](docs/audits/2026-11-10-active-skills-audit.md).

The [implemented improvements](docs/audits/2026-11-10-improvements.md) cover the previous 111-skill catalog: 108 updated and 3 retained. The report includes individual version changes, validation, content hashes, and unresolved limits. Review the [PyDESeq2 2.0.0](skills-market/compbio/multiomics/scRNA-seq/pydeseq2/SKILL.md) CLI change before updating an existing copy; [Scribble](skills-market/compbio/multiomics/integration-tools/scribble/SKILL.md) remains an identification-only entry with an unverified package identity.

The [reviewed import of 11 selected skills](docs/audits/2026-11-11-selected-skill-import.md) added 11 skills before subsequent archiving. It records per-skill cutter decisions, before/after sizes, version normalization, checks, and verification limits.

## By Domain

### Computational Biology — 38 skills

Single-cell RNA-seq, spatial omics, multi-omics integration, structural biology, databases, and workflow engineering.

| Category | Skills |
|---------|--------|
| Single-cell analysis | [`scanpy`](skills-market/compbio/single-cell/analysis/scanpy/SKILL.md), [`seurat`](skills-market/compbio/single-cell/analysis/seurat/SKILL.md), [`scvi-tools`](skills-market/compbio/single-cell/analysis/scvi-tools/SKILL.md), [`anndata`](skills-market/compbio/single-cell/analysis/anndata/SKILL.md) |
| Perturbation analysis | [`pertpy`](skills-market/compbio/single-cell/analysis/pertpy/SKILL.md) |
| H5AD interchange | [`anndatar`](skills-market/compbio/single-cell/analysis/anndatar/SKILL.md), [`schard`](skills-market/compbio/single-cell/analysis/schard/SKILL.md) |
| Trajectory analysis | [`monocle3`](skills-market/compbio/single-cell/analysis/monocle3/SKILL.md) |
| Integration | [`seurat-v5`](skills-market/compbio/single-cell/integration/seurat-v5/SKILL.md), [`harmony`](skills-market/compbio/single-cell/integration/harmony/SKILL.md), [`scanorama`](skills-market/compbio/single-cell/integration/scanorama/SKILL.md), [`bbknn`](skills-market/compbio/single-cell/integration/bbknn/SKILL.md) |
| Visualization | [`cellxgene`](skills-market/compbio/single-cell/visualization/cellxgene/SKILL.md), [`cellxgene-census`](skills-market/compbio/single-cell/visualization/cellxgene-census/SKILL.md) |
| Spatial omics | [`squidpy`](skills-market/compbio/spatial-omics/analysis/squidpy/SKILL.md), [`giotto`](skills-market/compbio/spatial-omics/analysis/giotto/SKILL.md), [`spatialdata`](skills-market/compbio/spatial-omics/analysis/spatialdata/SKILL.md), [`vitessce`](skills-market/compbio/spatial-omics/visualization/vitessce/SKILL.md) |
| Platforms | [`stereo-seq`](skills-market/compbio/spatial-omics/platforms/stereo-seq/SKILL.md) |
| Multi-omics | [`pydeseq2`](skills-market/compbio/multiomics/scRNA-seq/pydeseq2/SKILL.md), [`archr`](skills-market/compbio/multiomics/scATAC-seq/archr/SKILL.md), [`signac`](skills-market/compbio/multiomics/scATAC-seq/signac/SKILL.md), [`scribble`](skills-market/compbio/multiomics/integration-tools/scribble/SKILL.md), [`uniprot`](skills-market/compbio/multiomics/proteomics/uniprot/SKILL.md), [`metabolomics-workbench`](skills-market/compbio/multiomics/metabolomics/metabolomics-workbench/SKILL.md) |
| Structural biology | [`chimerax-mcp`](skills-market/compbio/structural-biology/chimerax-mcp/SKILL.md) |
| Databases | [`kegg`](skills-market/compbio/databases/kegg/SKILL.md), [`reactome`](skills-market/compbio/databases/reactome/SKILL.md), [`geo`](skills-market/compbio/databases/geo/SKILL.md), [`ensembl`](skills-market/compbio/databases/ensembl/SKILL.md), [`human-cell-atlas`](skills-market/compbio/databases/human-cell-atlas/SKILL.md) |
| Workflows | [`snakemake`](skills-market/compbio/workflows/snakemake/SKILL.md), [`nextflow`](skills-market/compbio/workflows/nextflow/SKILL.md) |
| Expert workflows | [`draft-spatial-methods`](skills-market/compbio/expert-workflows/draft-spatial-methods/SKILL.md), [`explain-bio-dl-model`](skills-market/compbio/expert-workflows/explain-bio-dl-model/SKILL.md), [`critique-bio-manuscript`](skills-market/compbio/expert-workflows/critique-bio-manuscript/SKILL.md), [`computational-biology-retrospective`](skills-market/compbio/expert-workflows/computational-biology-retrospective/SKILL.md) |
| Project continuity | [`computational-biology-project-manager`](skills-market/compbio/expert-workflows/computational-biology-project-manager/SKILL.md) |

### AI / ML — 14 skills

Latent-model identifiability, JEPA model development, deep learning, LLM fine-tuning, and distributed training infrastructure.

| Category | Skills |
|---------|--------|
| Model theory | [`latent-identifiability`](skills-market/ai-ml/theory/latent-identifiability/SKILL.md), [`vi-methodology-development`](skills-market/ai-ml/theory/vi-methodology-development/SKILL.md) |
| Deep learning | [`pytorch`](skills-market/ai-ml/deep-learning/pytorch/SKILL.md), [`jepa-pytorch-development`](skills-market/ai-ml/deep-learning/jepa-pytorch-development/SKILL.md) |
| LLM ecosystem | [`transformers`](skills-market/ai-ml/llm/transformers/SKILL.md), [`huggingface-hub`](skills-market/ai-ml/llm/huggingface-hub/SKILL.md), [`peft`](skills-market/ai-ml/llm/peft/SKILL.md), [`trl`](skills-market/ai-ml/llm/trl/SKILL.md), [`bitsandbytes`](skills-market/ai-ml/llm/bitsandbytes/SKILL.md), [`browser-use`](skills-market/ai-ml/llm/browser-use/SKILL.md) |
| Training | [`pytorch-lightning`](skills-market/ai-ml/training/pytorch-lightning/SKILL.md), [`accelerate`](skills-market/ai-ml/training/accelerate/SKILL.md), [`datasets`](skills-market/ai-ml/training/datasets/SKILL.md), [`deepspeed`](skills-market/ai-ml/training/deepspeed/SKILL.md) |

### Programming / Python — 13 skills

Python library development from zero to production.

| Category | Skills |
|---------|--------|
| Foundation | [`project-setup`](skills-market/programming/python/project-setup/SKILL.md), [`code-quality`](skills-market/programming/python/code-quality/SKILL.md), [`testing-strategy`](skills-market/programming/python/testing-strategy/SKILL.md), [`documentation`](skills-market/programming/python/documentation/SKILL.md) |
| Distribution | [`packaging`](skills-market/programming/python/packaging/SKILL.md), [`release-management`](skills-market/programming/python/release-management/SKILL.md), [`cli-development`](skills-market/programming/python/cli-development/SKILL.md) |
| Quality | [`performance`](skills-market/programming/python/performance/SKILL.md), [`api-design`](skills-market/programming/python/api-design/SKILL.md), [`library-review`](skills-market/programming/python/library-review/SKILL.md), [`community`](skills-market/programming/python/community/SKILL.md) |
| Utilities | [`sqlite`](skills-market/programming/python/sqlite/SKILL.md), [`jupyter`](skills-market/programming/python/jupyter/SKILL.md) |

### Writing — 14 skills

Academic writing, literature review, LaTeX, and Obsidian knowledge management.

| Category | Skills |
|---------|--------|
| Academic | [`academic-writing-editor`](skills-market/writing/academic/academic-writing-editor/SKILL.md), [`humanizer`](skills-market/writing/academic/humanizer/SKILL.md), [`humanizer-zh`](skills-market/writing/academic/humanizer-zh/SKILL.md) |
| Technical English | [`asd-ste100`](skills-market/writing/technical/asd-ste100/SKILL.md) |
| Literature | [`zotpilot`](skills-market/writing/literature/zotpilot/SKILL.md) |
| Academic slides | [`duke-nus-marp`](skills-market/writing/presentations/duke-nus-marp/SKILL.md) |
| LaTeX | [`latex-writing`](skills-market/writing/latex/latex-writing/SKILL.md), [`compile-latex`](skills-market/writing/latex/compile-latex/SKILL.md) |
| Obsidian | [`obsidian-markdown`](skills-market/writing/obsidian/obsidian-markdown/SKILL.md), [`obsidian-cli`](skills-market/writing/obsidian/obsidian-cli/SKILL.md), [`obsidian-bases`](skills-market/writing/obsidian/obsidian-bases/SKILL.md), [`json-canvas`](skills-market/writing/obsidian/json-canvas/SKILL.md), [`defuddle`](skills-market/writing/obsidian/defuddle/SKILL.md), [`wiki-keeper`](skills-market/writing/obsidian/wiki-keeper/SKILL.md) |

### Documents — 20 skills

Office automation, design, and media.

| Category | Skills |
|---------|--------|
| Office | [`officecli`](skills-market/documents/office/officecli/SKILL.md), [`officecli-docx`](skills-market/documents/office/officecli-docx/SKILL.md), [`officecli-pptx`](skills-market/documents/office/officecli-pptx/SKILL.md), [`officecli-xlsx`](skills-market/documents/office/officecli-xlsx/SKILL.md) |
| Formats | [`docx`](skills-market/documents/formats/docx/SKILL.md), [`pptx`](skills-market/documents/formats/pptx/SKILL.md), [`xlsx`](skills-market/documents/formats/xlsx/SKILL.md), [`pdf`](skills-market/documents/formats/pdf/SKILL.md) |
| Design | [`frontend-design`](skills-market/documents/design/frontend-design/SKILL.md), [`canvas-design`](skills-market/documents/design/canvas-design/SKILL.md), [`theme-factory`](skills-market/documents/design/theme-factory/SKILL.md), [`brand-guidelines`](skills-market/documents/design/brand-guidelines/SKILL.md), [`algorithmic-art`](skills-market/documents/design/algorithmic-art/SKILL.md), [`web-artifacts-builder`](skills-market/documents/design/web-artifacts-builder/SKILL.md), [`webapp-testing`](skills-market/documents/design/webapp-testing/SKILL.md), [`scientific-figure-polish`](skills-market/documents/design/scientific-figure-polish/SKILL.md) |
| Collaboration | [`doc-coauthoring`](skills-market/documents/collaboration/doc-coauthoring/SKILL.md), [`internal-comms`](skills-market/documents/collaboration/internal-comms/SKILL.md) |
| Media | [`imgur-cli`](skills-market/documents/media/imgur-cli/SKILL.md), [`slack-gif-creator`](skills-market/documents/media/slack-gif-creator/SKILL.md) |

### Agents — 7 skills

Coding agents, MCP development, session handoffs, and engineering guidelines.

| Category | Skills |
|---------|--------|
| Coding agents | [`claude-code`](skills-market/agents/claude-code/SKILL.md), [`codex`](skills-market/agents/codex/SKILL.md) |
| MCP | [`mcp-builder`](skills-market/agents/mcp/mcp-builder/SKILL.md) |
| Guidelines | [`ub-mode`](skills-market/agents/guidelines/ub-mode/SKILL.md) |
| Session transfer | [`handoff`](skills-market/agents/workflows/handoff/SKILL.md) |
| Chat backup | [`codex-backup`](skills-market/agents/workflows/codex-backup/SKILL.md), [`macos-codex-backup`](skills-market/agents/workflows/macos-codex-backup/SKILL.md) |

### Platforms — 10 skills

GitHub workflows and Google Workspace integrations.

| Category | Skills |
|---------|--------|
| GitHub | [`github-auth`](skills-market/platforms/github/github-auth/SKILL.md), [`github-code-review`](skills-market/platforms/github/github-code-review/SKILL.md), [`github-issues`](skills-market/platforms/github/github-issues/SKILL.md), [`github-pr-workflow`](skills-market/platforms/github/github-pr-workflow/SKILL.md), [`github-repo-management`](skills-market/platforms/github/github-repo-management/SKILL.md), [`github-codebase-inspection`](skills-market/platforms/github/codebase-inspection/SKILL.md) |
| Google Workspace | [`gws-shared`](skills-market/platforms/google-workspace/gws-shared/SKILL.md), [`gws-drive`](skills-market/platforms/google-workspace/gws-drive/SKILL.md), [`gws-drive-upload`](skills-market/platforms/google-workspace/gws-drive-upload/SKILL.md), [`yiru-google-drive`](skills-market/platforms/google-workspace/yiru-google-drive/SKILL.md) |

### Frontend — 2 skills

Website maintenance.

| Category | Skills |
|---------|--------|
| Site maintenance | [`page-keeper`](skills-market/frontend/site-maintenance/page-keeper/SKILL.md), [`chen-academic-page-maintainer`](skills-market/frontend/site-maintenance/chen-academic-page-maintainer/SKILL.md) |

### Core — 5 skills

Security, skill authoring, and scientific research workflows.

| Category | Skills |
|---------|--------|
| Skill authoring | [`skill-creator`](skills-market/core/dev/skill-creator/SKILL.md), [`skill-cutter`](skills-market/core/dev/skill-cutter/SKILL.md) |
| Security | [`security-audit`](skills-market/core/security/security-audit/SKILL.md) |
| Research workflows | [`scientific-brainstorming`](skills-market/core/research/scientific-brainstorming/SKILL.md), [`scientific-coding-governance`](skills-market/core/research/scientific-coding-governance/SKILL.md) |

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

**Core rule**: skills are referenced by **stable ID** (e.g., [`scanpy`](skills-market/compbio/single-cell/analysis/scanpy/SKILL.md)), never by folder path. The registry is the source of truth. See `docs/guides/architecture.md` for the full design.

---

## License

MIT — see `LICENSE.md`
