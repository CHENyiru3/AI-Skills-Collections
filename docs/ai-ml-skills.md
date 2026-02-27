# AI/ML Skills Catalog

This document provides a comprehensive catalog of AI/ML skills available in this repository.

## Skills Overview

| Skill | Category | Description |
|-------|----------|-------------|
| pytorch | Deep Learning | PyTorch deep learning framework |
| transformers | LLM | Hugging Face Transformers library |
| huggingface-hub | LLM | Hugging Face Hub for model management |
| peft | LLM | Parameter-Efficient Fine-Tuning (LoRA, QLoRA) |
| trl | LLM | Transformer Reinforcement Learning (SFT, RLHF, DPO) |
| bitsandbytes | LLM | Quantization for LLM fine-tuning |
| pytorch-lightning | Training | PyTorch Lightning training framework |
| accelerate | Training | Distributed training and mixed precision |
| datasets | Training | Hugging Face Datasets library |
| deepspeed | Training | DeepSpeed distributed training |

## Deep Learning

### PyTorch

PyTorch is an open-source machine learning framework that accelerates the path from research prototyping to production deployment.

**Key Features:**
- Neural network building (nn.Module)
- Automatic differentiation (autograd)
- GPU acceleration
- TorchScript and ONNX export

**Use Cases:**
- Building custom neural networks
- Training deep learning models
- Research prototyping
- Production deployment

**Related Skills:**
- For distributed training: accelerate, deepspeed
- For pre-trained models: transformers

---

## LLM Ecosystem

### Transformers

Hugging Face Transformers provides thousands of pre-trained models for NLP, vision, and audio tasks.

**Key Features:**
- Pre-trained models (BERT, GPT, Llama, T5, etc.)
- Pipelines for quick inference
- Fine-tuning support
- Tokenizers

**Use Cases:**
- Text classification
- Named Entity Recognition
- Question Answering
- Text Generation
- Summarization
- Translation

**Related Skills:**
- For efficient fine-tuning: peft
- For RLHF training: trl

### Hugging Face Hub

The platform for sharing machine learning models, datasets, and demos.

**Key Features:**
- Model downloading/uploading
- Dataset access
- Version control
- Model cards

**Use Cases:**
- Downloading pre-trained models
- Sharing trained models
- Accessing datasets

### PEFT (Parameter-Efficient Fine-Tuning)

PEFT provides methods for efficiently fine-tuning large models by training only a small fraction of parameters.

**Key Features:**
- LoRA (Low-Rank Adaptation)
- QLoRA (4-bit fine-tuning)
- Adapters
- Prefix/Prompt Tuning

**Memory Comparison:**
| Method | 7B Model VRAM | Trainable Params |
|--------|---------------|------------------|
| Full FT | ~28GB | 100% |
| LoRA (r=16) | ~14GB | ~0.5% |
| QLoRA (4-bit) | ~6GB | ~0.5% |

### TRL (Transformer Reinforcement Learning)

TRL provides tools for training language models with RLHF and DPO.

**Key Features:**
- Supervised Fine-Tuning (SFT)
- Reward Modeling
- RLHF with PPO
- Direct Preference Optimization (DPO)

**Use Cases:**
- Instruction tuning
- Preference learning
- Model alignment

### BitsAndBytes

Quantization library for efficient LLM loading and inference.

**Key Features:**
- 8-bit quantization (LLM.int8)
- 4-bit NF4 quantization
- Mixed precision support
- CPU offloading

---

## Training Tools

### PyTorch Lightning

A lightweight wrapper for PyTorch that handles training loop complexity.

**Key Features:**
- Reduced boilerplate
- Built-in logging
- Multi-GPU/TPU support
- Automatic checkpointing

### Accelerate

Hugging Face Accelerate provides simple APIs for distributed training.

**Key Features:**
- Multi-GPU training
- TPU support
- Mixed precision (FP16/BF16)
- Gradient accumulation
- DeepSpeed integration

### Datasets

Hugging Face Datasets for loading and processing datasets.

**Key Features:**
- Loading from Hub or local files
- Tokenization with map/batch
- Caching and memory-mapping
- Streaming large datasets

### DeepSpeed

Microsoft's deep learning optimization library.

**Key Features:**
- ZeRO optimization (Stage 1-3)
- Pipeline parallelism
- Mixed precision training
- Memory offloading

**ZeRO Memory Savings:**
| Stage | Description | Memory Savings |
|-------|-------------|----------------|
| Stage 1 | Optimizer state | ~4x |
| Stage 2 | + Gradients | ~8x |
| Stage 3 | + Parameters | ~N x |

---

## Skill Dependencies

```
pytorch (core)
├── transformers
│   ├── huggingface-hub
│   ├── peft
│   │   └── bitsandbytes
│   └── trl
├── accelerate
├── datasets
├── pytorch-lightning
└── deepspeed
```

## Recommended Learning Path

### For Beginners
1. PyTorch fundamentals
2. Transformers for NLP
3. Datasets for data handling

### For Intermediate
1. Accelerate for distributed training
2. PEFT for efficient fine-tuning
3. BitsAndBytes for quantization

### For Advanced
1. DeepSpeed for large-scale training
2. TRL for RLHF/DPO
3. Full LLM fine-tuning pipeline

## Quick Reference

### Installation

```bash
# Core
pip install torch

# Transformers ecosystem
pip install transformers accelerate datasets peft trl bitsandbytes

# Training
pip install pytorch-lightning deepspeed
```

### Loading Models

```python
# PyTorch model
import torch
model = torch.nn.Linear(10, 10)

# Transformers model
from transformers import AutoModel
model = AutoModel.from_pretrained("bert-base-uncased")

# Quantized model
from transformers import AutoModelForCausalLM
from bitsandbytes import BitsAndBytesConfig
config = BitsAndBytesConfig(load_in_4bit=True)
model = AutoModelForCausalLM.from_pretrained("model", quantization_config=config)
```

### Training

```python
# Standard PyTorch
for batch in dataloader:
    optimizer.zero_grad()
    loss = model(batch)
    loss.backward()
    optimizer.step()

# With Accelerate
model, optimizer, dataloader = accelerator.prepare(model, optimizer, dataloader)
for batch in dataloader:
    optimizer.zero_grad()
    loss = model(batch)
    accelerator.backward(loss)
    optimizer.step()

# With Lightning
trainer = pl.Trainer(max_epochs=5)
trainer.fit(model, dataloader)
```

---

## Additional Resources

- [PyTorch Documentation](https://pytorch.org/docs/)
- [Transformers Documentation](https://huggingface.co/docs/transformers)
- [PEFT Documentation](https://huggingface.co/docs/peft)
- [TRL Documentation](https://huggingface.co/docs/trl)
- [Accelerate Documentation](https://huggingface.co/docs/accelerate)
- [DeepSpeed Documentation](https://www.deepspeed.ai/)
- [Lightning Documentation](https://pytorch-lightning.readthedocs.io/)
