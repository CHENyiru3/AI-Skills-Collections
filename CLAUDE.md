# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an **AI Skills repository** - a collection of skills for AI agents covering AI/ML, computational biology, and writing tools. The skills are designed to work with Claude Code AI agents and are loaded via the Claude Code plugin system.

## Repository Structure

```
ai_skills/
├── document-skills/         # Document processing skills (16 skills)
│   ├── docx, pptx, xlsx, pdf
│   ├── algorithmic-art, canvas-design, theme-factory, brand-guidelines
│   ├── frontend-design, web-artifacts-builder, webapp-testing
│   └── mcp-builder, skill-creator, slack-gif-creator, internal-comms, doc-coauthoring
├── ai-ml-skills/           # AI/ML skills (10 skills)
│   ├── deep-learning/      # PyTorch
│   ├── llm/                # Transformers, HuggingFace Hub, PEFT, TRL, BitsAndBytes
│   └── training/           # Accelerate, DeepSpeed, PyTorch Lightning, Datasets
├── compbio-skills/         # Computational biology skills (29 skills)
│   ├── single-cell/        # scanpy, Seurat, scvi-tools, AnnData, cellxgene
│   ├── integration/        # Harmony, Scanorama, BBKNN, Seurat v5
│   ├── multiomics/         # PyDESeq2, ArchR, Signac, metabolomics, proteomics
│   ├── spatial-omics/      # Squidpy, Giotto, SpatialData, Visium, Stereo-seq
│   ├── databases/          # KEGG, Reactome, GEO, Ensembl, Human Cell Atlas
│   └── workflows/         # Snakemake, Nextflow
├── writing/                # Writing skills (3 skills)
│   ├── LaTex/             # LaTeX writing and compilation
│   └── Obsidian/          # Note-taking with Obsidian
├── docs/                   # Documentation catalogs
└── .claude-plugin/         # Claude Code marketplace configuration
```

## Skill System

### How Skills Work

Each skill is a directory containing a `SKILL.md` file with YAML frontmatter:
- `name`: Skill identifier
- `description`: When to use this skill
- `license`: License for the skill
- `metadata.skill-author`: Author name

### Adding New Skills

1. Create a new directory under the appropriate category
2. Add a `SKILL.md` file with the required frontmatter and content
3. Update `.claude-plugin/marketplace.json` to include the new skill in the appropriate plugin's `skills` array
4. If using local-only (not in marketplace), update `.claude/settings.local.json` with the path

### Skill Categories

- **Document Processing**: docx, pptx, xlsx, pdf, algorithmic-art, canvas-design, theme-factory, frontend-design, web-artifacts-builder, webapp-testing, mcp-builder, skill-creator
- **AI/ML**: PyTorch, Transformers, PEFT, TRL, BitsAndBytes, HuggingFace Hub, Accelerate, DeepSpeed, PyTorch Lightning, Datasets
- **Computational Biology**: scanpy, scvi-tools, Seurat, AnnData, cellxgene, PyDESeq2, ArchR, Signac, Squidpy, Giotto, SpatialData, and more
- **Writing**: LaTeX, Obsidian

## Configuration Files

- `.claude-plugin/marketplace.json`: Defines all available plugins and their skills
- `.claude/settings.local.json`: User settings including permissions and extra marketplace paths

## Common Tasks

### Adding a New Skill
1. Create directory: `category/skill-name/SKILL.md`
2. Add frontmatter with name, description, license, author
3. Add content following the existing skill format
4. Register in marketplace.json or settings.local.json

### Modifying Existing Skills
Edit the `SKILL.md` file directly. Each skill contains:
- Overview and when to use the skill
- Quick start code examples
- Detailed usage patterns
- Key parameters
- Common pitfalls and best practices
