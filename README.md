# AI Skills

A collection of skills for AI agents covering document workflows, website maintenance, Python library development, AI/ML, computational biology, and writing tools.

## Overview

This repository provides AI agent skills designed to work with Claude Code and Codex. The skills cover six main domains:

- **AI/ML**: Deep learning, LLM fine-tuning, and distributed training
- **Computational Biology**: Single-cell, multi-omics, and spatial omics analysis
- **Document Processing**: Word, Excel, PowerPoint, PDF manipulation
- **Website Maintenance**: Repo-specific frontend and academic-site maintenance skills
- **Python Library Development**: Project setup, testing, packaging, performance, and API design
- **Writing**: LaTeX, Obsidian, and technical documentation

## Skill Categories

### Document Skills (22 skills)

| Category | Skills |
|----------|--------|
| Office | officecli, officecli-docx, officecli-pptx, officecli-xlsx, docx, pptx, xlsx, pdf |
| Design & Art | algorithmic-art, canvas-design, theme-factory, brand-guidelines |
| Web | frontend-design, web-artifacts-builder, webapp-testing |
| Tools | mcp-builder, skill-creator, skill-seekers, slack-gif-creator, internal-comms, doc-coauthoring, imgur-cli |

### Font_end Skills (2 skills)

| Category | Skills |
|----------|--------|
| Website Maintenance | page-keeper, chen-academic-page-maintainer |

### AI/ML Skills (10 skills)

| Category | Skills |
|----------|--------|
| Deep Learning | PyTorch |
| LLM Ecosystem | Transformers, HuggingFace Hub, PEFT, TRL, BitsAndBytes |
| Training Tools | Accelerate, DeepSpeed, PyTorch Lightning, Datasets |

### Python Skills (12 skills)

| Category | Skills |
|----------|--------|
| Foundations | project-setup, code-quality, testing-strategy |
| Distribution | packaging, release-management, cli-development |
| Quality | security-audit, performance, api-design, library-review |
| Documentation & Community | documentation, community |

### Computational Biology Skills (35 skills)

| Category | Skills |
|----------|--------|
| Single-Cell Analysis | scanpy, Seurat, scvi-tools, cellxgene, AnnData |
| Data Integration | Harmony, Scanorama, BBKNN, Seurat v5 |
| Multi-Omics | PyDESeq2, ArchR, Signac, Metabolomics, UniProt, KEGG, Reactome |
| Spatial Omics | Squidpy, Giotto, SpatialData, Vitessce, Visium, Stereo-seq |
| Databases | GEO, Ensembl, Human Cell Atlas |
| Workflows | Snakemake, Nextflow |
| Bioinformatics Tools | draft-spatial-methods, explain-bio-dl-model, critique-bio-manuscript |

### Writing Skills (9 skills)

| Category | Skills |
|----------|--------|
| General Academic | academic-writing-editor, humanizer |
| LaTeX | Latex_writing, Compile_latex |
| Obsidian | obsidian-markdown, obsidian-cli, obsidian-bases, json-canvas, defuddle |

## Documentation

The top-level `README.md` is the fast entry point for installation and repository structure. The formal documentation hub lives at [docs/README.md](docs/README.md), with domain catalogs under `docs/catalogs/` and practical examples under `docs/guides/`.

## Quick Start

### For AI/ML Tasks

```python
# Example: Using Transformers for text classification
from transformers import pipeline

classifier = pipeline("sentiment-analysis")
result = classifier("I love using AI skills!")
```

### For Computational Biology Tasks

```python
# Example: Using scanpy for single-cell analysis
import scanpy as sc

adata = sc.read_h5ad("data.h5ad")
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)
sc.tl.pca(adata)
sc.pp.neighbors(adata)
sc.tl.umap(adata)
```

## Installation

These skills work best when each installed skill lives in its own directory containing a `SKILL.md` file. This repository supports both Claude Code and Codex, but they discover skills differently.

### Prerequisites

- Claude Code or Codex
- Python 3.8+

### Install for Codex

Codex installs user skills into `$CODEX_HOME/skills`, which defaults to `~/.codex/skills` when `CODEX_HOME` is unset. Codex only discovers a skill when each installed skill is a top-level directory under that path and that directory contains `SKILL.md`. Copy the leaf skill directories, not the category folders such as `document-skills/` or `compbio-skills/`.

Install all skills from this repository:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
find document-skills Font_end python-skills ai-ml-skills compbio-skills writing -name SKILL.md -print | while read -r skill_file; do
  skill_dir="$(dirname "$skill_file")"
  cp -R "$skill_dir" "${CODEX_HOME:-$HOME/.codex}/skills/"
done
```

Install a single skill:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R document-skills/pdf "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Verify the expected installed skill names:

```bash
find "${CODEX_HOME:-$HOME/.codex}/skills" -mindepth 1 -maxdepth 1 -type d -exec test -f '{}/SKILL.md' ';' -print \
  | xargs -n1 basename \
  | sort
```

Troubleshooting:
- If a skill does not load, confirm you copied the leaf skill directory itself, not a parent category directory.
- `SKILL.md` frontmatter must begin on line 1 with `---`. Comments or other text before the frontmatter can cause Codex to skip the skill.
- `.claude-plugin/marketplace.json` is used by Claude Code, not Codex.

Restart Codex to pick up new skills.

### Install for Claude Code

For a local install, copy the leaf skill directories into `~/.claude/skills/`:

```bash
mkdir -p ~/.claude/skills
find document-skills Font_end python-skills ai-ml-skills compbio-skills writing -name SKILL.md -print | while read -r skill_file; do
  skill_dir="$(dirname "$skill_file")"
  cp -R "$skill_dir" ~/.claude/skills/
done
```

Restart Claude Code or start a new session. Skills will be available:
- Use directly: `/skill-name` (e.g., `/pdf`, `/scanpy`, `/pytorch`)
- Auto-trigger: Claude will use relevant skills based on your task

### Alternative: Claude Code Marketplace Link (For Development)

If you want Claude Code to load this repository through its local marketplace config instead of copying skill directories:

1. Add to your global Claude settings (`~/.claude/settings.json`):
```json
{
  "extraKnownMarketplaces": {
    "ai-skills": {
      "source": {
        "type": "file",
        "path": "/path/to/ai_skills/.claude-plugin/marketplace.json"
      }
    }
  },
  "enabledPlugins": {
    "document-skills@ai-skills": true,
    "font-end-skills@ai-skills": true,
    "python-skills@ai-skills": true,
    "ai-ml-skills@ai-skills": true,
    "compbio-skills@ai-skills": true,
    "writing-skills@ai-skills": true
  }
}
```

This marketplace configuration is Claude Code-specific; Codex does not read `.claude-plugin/marketplace.json`.

### Adding New Skills

To add a new skill to this repository:

1. Create a skill directory:
```bash
mkdir -p document-skills/my-new-skill
# or under Font_end, python-skills, ai-ml-skills, compbio-skills, writing
```

2. Create `SKILL.md` with YAML frontmatter:
```markdown
---
name: my-new-skill
description: When to use this skill and what it does. Be specific about triggers.
---

Your skill instructions here...
```

3. Copy the skill directory into your local Codex or Claude skills folder:
```bash
cp -R document-skills/my-new-skill "${CODEX_HOME:-$HOME/.codex}/skills/"
# or
cp -R document-skills/my-new-skill ~/.claude/skills/
```

4. If you want the skill available through Claude Code's marketplace config, also update `.claude-plugin/marketplace.json`

### Verifying Installation

Verify that the installed skill directories contain `SKILL.md`:

```bash
find "${CODEX_HOME:-$HOME/.codex}/skills" ~/.claude/skills -maxdepth 2 -name SKILL.md 2>/dev/null | sort
```

For Claude Code, you can also run `/skills` to inspect the loaded skills.

## Project Structure

```
ai_skills/
├── document-skills/         # Document processing (21 skills)
│   ├── officecli, officecli-docx, officecli-pptx, officecli-xlsx, docx, pptx, xlsx, pdf
│   ├── algorithmic-art, canvas-design, theme-factory
│   ├── frontend-design, web-artifacts-builder
│   └── mcp-builder, skill-creator, skill-seekers, internal-comms, etc.
├── Font_end/               # Website maintenance skills (2 skills)
│   ├── page-keeper        # Generic site-maintenance skill generator
│   └── chen-academic-page-maintainer
├── python-skills/           # Python library engineering (12 skills)
│   ├── project-setup, code-quality, testing-strategy
│   ├── packaging, release-management, cli-development
│   └── security-audit, performance, api-design, documentation, community, library-review
├── ai-ml-skills/           # AI/ML skills (10 skills)
│   ├── deep-learning/      # PyTorch
│   ├── llm/                # Transformers, PEFT, TRL, etc.
│   └── training/           # Accelerate, DeepSpeed, etc.
├── compbio-skills/         # Computational biology (35 skills)
│   ├── single-cell/       # scanpy, Seurat, scvi-tools
│   ├── multiomics/         # PyDESeq2, ArchR, etc.
│   ├── spatial-omics/      # Squidpy, Giotto, etc.
│   ├── databases/          # GEO, Ensembl, etc.
│   └── workflows/         # Snakemake, Nextflow
├── writing/                # Writing skills (9 skills)
│   ├── General_academic/  # Academic editing and cleanup
│   ├── LaTex/             # LaTeX writing & compilation
│   └── Obsidian/          # Note-taking and vault tooling
├── docs/                   # Documentation hub
│   ├── catalogs/          # Domain inventories
│   ├── guides/            # Examples and practical notes
│   └── README.md          # Documentation index
└── .claude-plugin/         # Claude Code configuration
```

## Total Skills: 85

- Document Skills: 21
- Font_end Skills: 2
- Python Skills: 12
- AI/ML Skills: 10
- Computational Biology: 35
- Writing: 5

## License

MIT License - See [LICENSE.md](LICENSE.md)

## Contributing

Contributions welcome! Please submit pull requests for:
- New skills
- Improvements to existing skills
- Bug fixes
- Documentation updates
