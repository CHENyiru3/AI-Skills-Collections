---
name: pytorch
domain: ai-ml
description: Implement or debug PyTorch tensor operations, nn.Module models, autograd, custom training loops, checkpoints, and device or precision issues. Use for concrete PyTorch development; prefer a project-specific model skill when its contracts apply.
license: BSD-3-Clause license
metadata:
  version: "1.0.1"
  skill-author: Eric Yiru
---

# PyTorch development

Inspect the model, data contract, installed PyTorch version, and execution device before choosing an implementation. Preserve the project's training framework and numerical conventions.

## Correctness first

- Record batch and tensor shapes, dtype, device, target meaning, and loss reduction. Keep tensors participating in an operation on compatible devices; do not move only one operand to CUDA.
- Register trainable parameters and persistent buffers on `nn.Module`; call `super().__init__()`. Check parameter ownership before constructing the optimizer.
- Match loss semantics: classification logits versus probabilities, class-index versus soft targets, masks, ignored labels, and per-example versus token normalization.
- Use `train()` for training and `eval()` with `no_grad()` or `inference_mode()` for evaluation. Evaluation mode alone does not disable autograd. Avoid `.data` mutations and unintended graph retention.

A complete CPU shape/gradient check, with no dataset download:

```python
import torch
from torch import nn

model = nn.Linear(4, 2)
x = torch.randn(3, 4)
y = torch.tensor([0, 1, 0])
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3)
optimizer.zero_grad(set_to_none=True)
loss = nn.functional.cross_entropy(model(x), y)
assert loss.ndim == 0 and torch.isfinite(loss)
loss.backward()
optimizer.step()
```

## Training and scaling

- Define where accumulation windows start/end, how losses are normalized, and when optimizer, scheduler, and gradient clipping run. Handle a final partial window. Clip after unscaling when using a scaler.
- Select AMP dtype from device support and numerical requirements. Use the installed `torch.amp`/`autocast` API; scaling is typically needed for float16, not universally for bfloat16. Do not silently enable AMP or alter precision.
- Prefer the project's distributed strategy; for ordinary multi-process data parallel training use DDP rather than recommending `DataParallel` by default. Check sampler sharding, rank-specific writes, synchronized metrics, and unused parameters.
- Tune loaders, pinned memory, checkpointing, compilation, and kernels only after measuring the bottleneck. Benchmark flags and determinism can conflict; document the chosen tradeoff.

## Persistence and verification

Save model state plus the optimizer, scheduler, scaler, step, configuration, and RNG state needed for the promised resume behavior. Load with explicit device mapping and inspect missing/unexpected keys. Use the version's safe weight-loading facilities; full pickle deserialization requires a trusted source.

Check one forward/backward step and relevant shape/gradient assertions before a long run. For resume or distributed changes, verify that specific behavior on a small run. Report observed loss, finite gradients, and test scope without claiming convergence from a smoke test.

Use [PyTorch documentation](https://docs.pytorch.org/docs/stable/) for version-specific AMP, checkpoint, compile, and export APIs. Choose an export backend to match the deployment target rather than prescribing TorchScript universally.
