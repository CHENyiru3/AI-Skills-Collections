# AI/ML Skills Catalog

This catalog covers the 10 skills under `ai-ml-skills/`.

## Deep Learning

| Skill | Location | Focus |
|-------|----------|-------|
| [`pytorch`](../../ai-ml-skills/deep-learning/pytorch/SKILL.md) | `ai-ml-skills/deep-learning/pytorch` | Core PyTorch modeling and training workflows |

## LLM Ecosystem

| Skill | Location | Focus |
|-------|----------|-------|
| [`transformers`](../../ai-ml-skills/llm/transformers/SKILL.md) | `ai-ml-skills/llm/transformers` | Model loading, inference, and fine-tuning with Hugging Face Transformers |
| [`huggingface-hub`](../../ai-ml-skills/llm/huggingface-hub/SKILL.md) | `ai-ml-skills/llm/huggingface-hub` | Model and dataset repository workflows |
| [`peft`](../../ai-ml-skills/llm/peft/SKILL.md) | `ai-ml-skills/llm/peft` | LoRA, QLoRA, and adapter-based fine-tuning |
| [`trl`](../../ai-ml-skills/llm/trl/SKILL.md) | `ai-ml-skills/llm/trl` | SFT, DPO, PPO, and preference-learning workflows |
| [`bitsandbytes`](../../ai-ml-skills/llm/bitsandbytes/SKILL.md) | `ai-ml-skills/llm/bitsandbytes` | 8-bit and 4-bit quantization for large models |

## Training Infrastructure

| Skill | Location | Focus |
|-------|----------|-------|
| [`accelerate`](../../ai-ml-skills/training/accelerate/SKILL.md) | `ai-ml-skills/training/accelerate` | Distributed training, mixed precision, and scaling |
| [`datasets`](../../ai-ml-skills/training/datasets/SKILL.md) | `ai-ml-skills/training/datasets` | Dataset loading, mapping, batching, and preprocessing |
| [`deepspeed`](../../ai-ml-skills/training/deepspeed/SKILL.md) | `ai-ml-skills/training/deepspeed` | ZeRO optimization and large-scale training |
| [`pytorch-lightning`](../../ai-ml-skills/training/pytorch-lightning/SKILL.md) | `ai-ml-skills/training/pytorch-lightning` | Structured training loops, checkpoints, and logging |

## Notes

- Start with `pytorch` for custom model work.
- Layer `transformers`, `peft`, `trl`, and `bitsandbytes` on top when the task is model-centric.
- Use `accelerate` or `deepspeed` when scale or hardware complexity becomes the bottleneck.
