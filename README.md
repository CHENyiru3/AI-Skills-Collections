# AI Skills

A collection of AI/ML skills for deep learning, LLM fine-tuning, and computational biology research.

## Overview

This repository provides AI agent skills designed to work with Claude Code and Codex AI agents. The skills cover two main domains:

- **AI/ML**: Deep learning, LLM fine-tuning, and distributed training
- **Computational Biology**: Single-cell, multi-omics, and spatial omics analysis

## Skill Categories

### AI/ML Skills (10 skills)

| Category | Skills |
|----------|--------|
| Deep Learning | PyTorch |
| LLM Ecosystem | Transformers, HuggingFace Hub, PEFT, TRL, BitsAndBytes |
| Training Tools | Accelerate, DeepSpeed, PyTorch Lightning, Datasets |

### Computational Biology Skills (29 skills)

| Category | Skills |
|----------|--------|
| Single-Cell Analysis | scanpy, Seurat, scvi-tools, cellxgene, AnnData |
| Data Integration | Harmony, Scanorama, BBKNN, Seurat v5 |
| Multi-Omics | PyDESeq2, ArchR, Signac, Metabolomics, UniProt, KEGG, Reactome |
| Spatial Omics | Squidpy, Giotto, SpatialData, Vitessce, Visium, Stereo-seq |
| Databases | GEO, Ensembl, Human Cell Atlas |
| Workflows | Snakemake, Nextflow |

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

These skills are designed to work with Claude Code and Codex AI agents.

### Prerequisites

- Claude Code or Codex AI agent
- Python 3.8+

### Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/ai_skills.git
   ```

2. Configure Claude Code to use these skills by updating your settings:
   ```json
   {
     "skills": {
       "enabled": true,
       "directories": ["./ai_skills"]
     }
   }
   ```

3. Skills will be available when working with relevant tasks

## Skills

### AI/ML Skills

| Skill | Description |
|-------|-------------|
| [PyTorch](ai-ml-skills/deep-learning/pytorch/) | Deep learning framework with neural networks, autograd, GPU acceleration |
| [Transformers](ai-ml-skills/llm/transformers/) | Pre-trained models (BERT, GPT, Llama), NLP pipelines, fine-tuning |
| [HuggingFace Hub](ai-ml-skills/llm/huggingface-hub/) | Model/dataset management, version control, sharing |
| [PEFT](ai-ml-skills/llm/peft/) | Parameter-efficient fine-tuning (LoRA, QLoRA) |
| [TRL](ai-ml-skills/llm/trl/) | RLHF, DPO, supervised fine-tuning |
| [BitsAndBytes](ai-ml-skills/llm/bitsandbytes/) | 8-bit/4-bit quantization for LLMs |
| [PyTorch Lightning](ai-ml-skills/training/pytorch-lightning/) | Simplified training loops, built-in logging |
| [Accelerate](ai-ml-skills/training/accelerate/) | Distributed training, mixed precision |
| [Datasets](ai-ml-skills/training/datasets/) | Loading/processing datasets from Hub |
| [DeepSpeed](ai-ml-skills/training/deepspeed/) | ZeRO optimization, large-scale training |

### Computational Biology Skills

See [docs/computational-biology-skills.md](docs/computational-biology-skills.md) for the complete catalog.

## Documentation

- [AI/ML Skills Catalog](docs/ai-ml-skills.md)
- [Computational Biology Skills Catalog](docs/computational-biology-skills.md)

## Project Structure

```
ai_skills/
├── ai-ml-skills/           # AI/ML skills
│   ├── deep-learning/      # PyTorch
│   ├── llm/                # Transformers, PEFT, TRL, etc.
│   └── training/           # Accelerate, DeepSpeed, etc.
├── compbio-skills/         # Computational biology skills
│   ├── single-cell/       # scanpy, Seurat, scvi-tools
│   ├── multiomics/         # PyDESeq2, ArchR, etc.
│   ├── spatial-omics/      # Squidpy, Giotto, etc.
│   ├── databases/          # GEO, Ensembl, etc.
│   └── workflows/          # Snakemake, Nextflow
├── docs/                   # Documentation
└── .claude-plugin/         # Claude Code configuration
```

## License

MIT License - See [LICENSE.md](LICENSE.md)

## Contributing

Contributions welcome! Please submit pull requests or open issues for:
- New skills
- Improvements to existing skills
- Bug fixes
- Documentation updates

## Resources

### AI/ML
- [PyTorch Documentation](https://pytorch.org/docs/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers)
- [PEFT Documentation](https://huggingface.co/docs/peft)
- [DeepSpeed Documentation](https://www.deepspeed.ai/)

### Computational Biology
- [Scanpy Documentation](https://scanpy.readthedocs.io/)
- [scverse Ecosystem](https://scverse.org/)
- [Seurat Documentation](https://satijalab.org/seurat/)
