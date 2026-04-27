# AI/ML Skills Catalog

This catalog covers the 13 skills under `skills-market/ai-ml/`.

## Deep Learning

| Skill | Location | Focus |
|-------|----------|-------|
| [`pytorch`](../../skills-market/ai-ml/deep-learning/pytorch/SKILL.md) | `ai-ml/deep-learning/pytorch` | Core PyTorch modeling and training workflows |

## LLM Ecosystem

| Skill | Location | Focus |
|-------|----------|-------|
| [`transformers`](../../skills-market/ai-ml/llm/transformers/SKILL.md) | `ai-ml/llm/transformers` | Model loading, inference, and fine-tuning with Hugging Face Transformers |
| [`huggingface-hub`](../../skills-market/ai-ml/llm/huggingface-hub/SKILL.md) | `ai-ml/llm/huggingface-hub` | Model and dataset repository workflows |
| [`peft`](../../skills-market/ai-ml/llm/peft/SKILL.md) | `ai-ml/llm/peft` | LoRA, QLoRA, and adapter-based fine-tuning |
| [`trl`](../../skills-market/ai-ml/llm/trl/SKILL.md) | `ai-ml/llm/trl` | SFT, DPO, PPO, and preference-learning workflows |
| [`bitsandbytes`](../../skills-market/ai-ml/llm/bitsandbytes/SKILL.md) | `ai-ml/llm/bitsandbytes` | 8-bit and 4-bit quantization for large models |
| [`cursor-usage-checker`](../../skills-market/ai-ml/llm/cursor-usage-checker/SKILL.md) | `ai-ml/llm/cursor-usage-checker` | Monitor Cursor IDE usage and limits |
| [`browser-use`](../../skills-market/ai-ml/llm/browser-use/SKILL.md) | `ai-ml/llm/browser-use` | Browser-use agent workflows with LLMs |
| [`minimax-cli`](../../skills-market/ai-ml/llm/minimax-cli/SKILL.md) | `ai-ml/llm/minimax-cli` | Unified MiniMax CLI workflows for text, image, video, speech, music, vision, search, and quota checks |

## Training Infrastructure

| Skill | Location | Focus |
|-------|----------|-------|
| [`accelerate`](../../skills-market/ai-ml/training/accelerate/SKILL.md) | `ai-ml/training/accelerate` | Distributed training, mixed precision, and scaling |
| [`datasets`](../../skills-market/ai-ml/training/datasets/SKILL.md) | `ai-ml/training/datasets` | Dataset loading, mapping, batching, and preprocessing |
| [`deepspeed`](../../skills-market/ai-ml/training/deepspeed/SKILL.md) | `ai-ml/training/deepspeed` | ZeRO optimization and large-scale training |
| [`pytorch-lightning`](../../skills-market/ai-ml/training/pytorch-lightning/SKILL.md) | `ai-ml/training/pytorch-lightning` | Structured training loops, checkpoints, and logging |

## Notes

- Start with `pytorch` for custom model work.
- Layer `transformers`, `peft`, `trl`, and `bitsandbytes` on top when the task is model-centric.
- Use `minimax-cli` when the task is MiniMax-specific or needs a terminal-driven multimodal generation workflow.
- Use `accelerate` or `deepspeed` when scale or hardware complexity becomes the bottleneck.
