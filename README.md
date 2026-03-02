# AI Skills

A collection of skills for AI agents covering AI/ML, computational biology, document processing, and writing tools.

## Overview

This repository provides AI agent skills designed to work with Claude Code and Claude Code. The skills cover four main domains:

- **AI/ML**: Deep learning, LLM fine-tuning, and distributed training
- **Computational Biology**: Single-cell, multi-omics, and spatial omics analysis
- **Document Processing**: Word, Excel, PowerPoint, PDF manipulation
- **Writing**: LaTeX, Obsidian, and technical documentation

## Skill Categories

### Document Skills (16 skills)

| Category | Skills |
|----------|--------|
| Office | docx, pptx, xlsx, pdf |
| Design & Art | algorithmic-art, canvas-design, theme-factory, brand-guidelines |
| Web | frontend-design, web-artifacts-builder, webapp-testing |
| Tools | mcp-builder, skill-creator, slack-gif-creator, internal-comms, doc-coauthoring |

### AI/ML Skills (10 skills)

| Category | Skills |
|----------|--------|
| Deep Learning | PyTorch |
| LLM Ecosystem | Transformers, HuggingFace Hub, PEFT, TRL, BitsAndBytes |
| Training Tools | Accelerate, DeepSpeed, PyTorch Lightning, Datasets |

### Computational Biology Skills (32 skills)

| Category | Skills |
|----------|--------|
| Single-Cell Analysis | scanpy, Seurat, scvi-tools, cellxgene, AnnData |
| Data Integration | Harmony, Scanorama, BBKNN, Seurat v5 |
| Multi-Omics | PyDESeq2, ArchR, Signac, Metabolomics, UniProt, KEGG, Reactome |
| Spatial Omics | Squidpy, Giotto, SpatialData, Vitessce, Visium, Stereo-seq |
| Databases | GEO, Ensembl, Human Cell Atlas |
| Workflows | Snakemake, Nextflow |
| Bioinformatics Tools | draft-spatial-methods, explain-bio-dl-model, critique-bio-manuscript |

### Writing Skills (4 skills)

| Category | Skills |
|----------|--------|
| LaTeX | Latex_writing, Compile_latex |
| Notes | notes_taking |
| Academic Editing | academic-writing-editor |

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

These skills are designed to work with Claude Code AI agents.

### Prerequisites

- Claude Code AI agent (v2.1+)
- Python 3.8+

### Quick Install (Copy to Claude's Skills Folder)

Copy all skills to Claude Code's personal skills directory:

```bash
# Copy all skills to ~/.claude/skills/
cp -r document-skills/* ~/.claude/skills/
cp -r ai-ml-skills/* ~/.claude/skills/
cp -r compbio-skills/* ~/.claude/skills/
cp -r writing/* ~/.claude/skills/
```

**Restart Claude Code** or start a new session. Skills will be available:
- Use directly: `/skill-name` (e.g., `/pdf`, `/scanpy`, `/pytorch`)
- Auto-trigger: Claude will use relevant skills based on your task

### Alternative: Link Repository (For Development)

If you want to keep skills in this repo and reference them:

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
    "ai-ml-skills@ai-skills": true,
    "compbio-skills@ai-skills": true,
    "writing-skills@ai-skills": true
  }
}
```

### Adding New Skills

To add a new skill to this repository:

1. Create a skill directory:
```bash
mkdir -p document-skills/my-new-skill
# or under ai-ml-skills, compbio-skills, writing
```

2. Create `SKILL.md` with YAML frontmatter:
```markdown
---
name: my-new-skill
description: When to use this skill and what it does. Be specific about triggers.
---

Your skill instructions here...
```

3. Update `.claude-plugin/marketplace.json` to include the new skill

4. Copy to Claude's skills folder:
```bash
cp -r document-skills/my-new-skill ~/.claude/skills/
```

### Verifying Installation

Run `/skills` in Claude Code to see all available skills.

## Project Structure

```
ai_skills/
├── document-skills/         # Document processing (16 skills)
│   ├── docx, pptx, xlsx, pdf
│   ├── algorithmic-art, canvas-design, theme-factory
│   ├── frontend-design, web-artifacts-builder
│   └── mcp-builder, skill-creator, etc.
├── ai-ml-skills/           # AI/ML skills (10 skills)
│   ├── deep-learning/      # PyTorch
│   ├── llm/                # Transformers, PEFT, TRL, etc.
│   └── training/           # Accelerate, DeepSpeed, etc.
├── compbio-skills/         # Computational biology (29 skills)
│   ├── single-cell/       # scanpy, Seurat, scvi-tools
│   ├── multiomics/         # PyDESeq2, ArchR, etc.
│   ├── spatial-omics/      # Squidpy, Giotto, etc.
│   ├── databases/          # GEO, Ensembl, etc.
│   └── workflows/         # Snakemake, Nextflow
├── writing/                # Writing skills (3 skills)
│   ├── LaTex/             # LaTeX writing & compilation
│   └── Obsidian/          # Note-taking
├── docs/                   # Documentation
└── .claude-plugin/         # Claude Code configuration
```

## Total Skills: 62

- Document Skills: 16
- AI/ML Skills: 10
- Computational Biology: 32
- Writing: 4

## License

MIT License - See [LICENSE.md](LICENSE.md)

## Contributing

Contributions welcome! Please submit pull requests for:
- New skills
- Improvements to existing skills
- Bug fixes
- Documentation updates
