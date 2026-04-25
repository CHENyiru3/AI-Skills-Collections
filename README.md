# AI Skills — Eric Yiru's Personal Library

> **111 skills** for Claude Code, Codex, and AI coding agents.
> Computational biology · Deep learning · Academic writing · Document automation · and more.

---

## What Is This

A **personal, production-grade skills library** for AI coding agents.
Each skill is a `SKILL.md` file that tells the agent *how* to do something well — not just *that* it can be done.

When you ask me to analyze a spatial transcriptomics dataset, fine-tune a Llama model, draft a LaTeX Methods section, or set up a Python library — I already know the right approach. These skills are how.

---

## Skills at a Glance

```
compbio (35)  ████████████████████████████████████  single-cell · spatial omics · multi-omics · databases · workflows
ai-ml  (12)  ████████████  deep learning · LLM fine-tuning · distributed training
programming (13) █████████████  project scaffolding · testing · packaging · API design
writing  (12)  ████████████  academic editing · LaTeX · Zotero · Obsidian
documents (19) ███████████████████  office automation · design · web artifacts
agents   (7)  ███████  Claude Code · Codex · MCP · agent guidelines
platforms (6) ██████  GitHub workflows · code review · PR management
frontend  (2) ██  site maintenance
core     (4) ████  skill authoring · security · bitwarden
```

---

## By Domain

### Computational Biology — 35 skills

Single-cell RNA-seq, spatial omics, multi-omics integration, databases, and workflow engineering.

| Category | Skills |
|---------|--------|
| Single-cell analysis | `scanpy`, `seurat`, `scvi-tools`, `anndata` |
| H5AD interchange | `anndatar`, `schard` |
| Trajectory analysis | `monocle3` |
| Integration | `seurat-v5`, `harmony`, `scanorama`, `bbknn` |
| Visualization | `cellxgene`, `cellxgene-census` |
| Spatial omics | `squidpy`, `giotto`, `spatialdata`, `vitessce` |
| Platforms | `visium`, `stereo-seq` |
| Multi-omics | `pydeseq2`, `archr`, `signac`, `scribble`, `uniprot`, `metabolomics-workbench` |
| Databases | `kegg`, `reactome`, `geo`, `ensembl`, `human-cell-atlas` |
| Workflows | `snakemake`, `nextflow` |
| Expert workflows | `draft-spatial-methods`, `explain-bio-dl-model`, `critique-bio-manuscript` |

### AI / ML — 12 skills

Deep learning, LLM fine-tuning, and distributed training infrastructure.

| Category | Skills |
|---------|--------|
| Deep learning | `pytorch` |
| LLM ecosystem | `transformers`, `huggingface-hub`, `peft`, `trl`, `bitsandbytes`, `cursor-usage-checker`, `browser-use` |
| Training | `pytorch-lightning`, `accelerate`, `datasets`, `deepspeed` |

### Programming / Python — 13 skills

Python library development from zero to production.

| Category | Skills |
|---------|--------|
| Foundation | `project-setup`, `code-quality`, `testing-strategy`, `documentation` |
| Distribution | `packaging`, `release-management`, `cli-development` |
| Quality | `security-audit`, `performance`, `api-design`, `library-review`, `community` |
| Utilities | `sqlite`, `jupyter` |

### Writing — 12 skills

Academic writing, literature review, LaTeX, and Obsidian knowledge management.

| Category | Skills |
|---------|--------|
| Academic | `academic-writing-editor`, `humanizer`, `humanizer-zh` |
| Literature | `zotpilot` |
| LaTeX | `latex-writing`, `compile-latex` |
| Obsidian | `obsidian-markdown`, `obsidian-cli`, `obsidian-bases`, `json-canvas`, `defuddle`, `wiki-keeper` |

### Documents — 19 skills

Office automation, design, and media.

| Category | Skills |
|---------|--------|
| Office | `officecli`, `officecli-docx`, `officecli-pptx`, `officecli-xlsx` |
| Formats | `docx`, `pptx`, `xlsx`, `pdf` |
| Design | `frontend-design`, `canvas-design`, `theme-factory`, `brand-guidelines`, `algorithmic-art`, `web-artifacts-builder`, `webapp-testing` |
| Collaboration | `doc-coauthoring`, `internal-comms` |
| Media | `imgur-cli`, `slack-gif-creator` |

### Agents — 7 skills

Coding agents, MCP development, and behavioral guidelines.

| Category | Skills |
|---------|--------|
| Coding agents | `claude-code`, `codex`, `hermes-agent`, `opencode`, `zed` |
| MCP | `mcp-builder` |
| Guidelines | `karpathy-guidelines` |

### Platforms — 6 skills

GitHub workflow integration.

| Category | Skills |
|---------|--------|
| GitHub | `github-auth`, `github-code-review`, `github-issues`, `github-pr-workflow`, `github-repo-management`, `github-codebase-inspection` |

### Frontend — 2 skills

Website maintenance.

| Category | Skills |
|---------|--------|
| Site maintenance | `page-keeper`, `chen-academic-page-maintainer` |

### Core — 4 skills

Security, performance tooling, and skill authoring.

| Category | Skills |
|---------|--------|
| Skill authoring | `skill-creator`, `skill-seekers` |
| Security | `security-audit`, `bitwarden` |

---

## Workflow Bundles (Taskpacks)

Taskpacks group skills by **workflow**, not machine:

| Taskpack | Description |
|---------|-------------|
| `paper-writing` | Academic paper, thesis, literature review |
| `document-export` | Office, PDF, Word, PowerPoint, Excel |
| `single-cell-analysis` | scRNA-seq from raw reads to annotated clusters |
| `spatial-omics-analysis` | Spatial transcriptomics — Visium, Squidpy, Giotto |
| `llm-finetuning` | LoRA, QLoRA, RLHF, DPO fine-tuning |
| `pytorch-model-dev` | PyTorch model development and optimization |
| `bio-databases` | KEGG, Reactome, GEO, Ensembl, UniProt access |
| `workflow-engineering` | Snakemake and Nextflow pipelines |
| `codebti` | CODEBTI project bundle |
| `feast` | Multi-omics integration — RNA, ATAC, proteomics, metabolomics |
| `thesis-defense` | Thesis defense preparation |
| `zotpilot-literature-map` | Literature embedding map and recommendation system |

---

## Architecture

```
skills-market/   canonical skill library (human-readable organization)
registry/        source of truth: stable IDs, paths, metadata
deployments/     machine/profile install plans
taskpacks/       workflow-specific skill bundles
scripts/          tooling: validate, migrate, install, query
```

**Core rule**: skills are referenced by **stable ID** (e.g., `scanpy`), never by folder path. The registry is the source of truth. See `docs/guides/architecture.md` for the full design.

---

## Missing Skills

4 skills are registered but not yet implemented:

- `native-mcp` — Native MCP client
- `ag-ui` — AG-UI agent framework
- `token-usage-checker` — Token usage monitoring
- `provider-usage-checker` — Provider usage monitoring

---

## License

MIT — see `LICENSE.md`
