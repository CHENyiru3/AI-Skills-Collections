---
name: pytorch-lightning
domain: ai-ml
description: Implement, migrate, or debug LightningModule, LightningDataModule, Trainer configuration, callbacks, logging, checkpoint resume, and distributed training in a PyTorch Lightning project.
license: Apache-2.0 license
metadata:
  version: "1.0.1"
  skill-author: Eric Yiru
---

# PyTorch Lightning

Read the installed Lightning version and project imports first. Keep one consistent namespace (`lightning.pytorch` or the project's supported `pytorch_lightning` package) and consult matching documentation before migrating APIs.

## Model and data contracts

- Call `super().__init__()` in modules and data modules. Keep `forward` for the model computation; implement `training_step` and `configure_optimizers` for training.
- Under automatic optimization return a differentiable scalar loss or a supported dictionary containing `loss`. Use `self.log` for metrics; returning legacy `log` dictionaries does not replace metric logging.
- Implement validation when using a validation-monitored callback. Log the exact monitor key, such as `val_loss`, with an appropriate epoch reduction and batch size. Use distributed synchronization when the metric requires it; do not average unequal batches incorrectly.
- Separate download/preparation from per-process setup. Preserve independent train/validation/test groups and deterministic split membership. Avoid re-splitting each time `setup` is called.

## Trainer choices

1. Select accelerator, device count, strategy, precision, accumulation, and checkpoint directory for the actual hardware and package version.
2. Use `seed_everything` before creating randomized data/model state; seeding is not a `Trainer(seed=...)` argument. Deterministic execution is a separate, potentially costly setting.
3. Use supported precision names such as `16-mixed` or `bf16-mixed` when available. Remove legacy `amp_backend`/Apex examples rather than combining generations of Trainer options.
4. Choose automatic or manual optimization deliberately. In manual optimization, explicitly manage backward, optimizer steps, accumulation, clipping, and schedulers through the supported Lightning APIs.
5. Configure early stopping/checkpointing only after the monitored metric is produced. Fail clearly on a missing monitor instead of suppressing the error.

## Check and resume

Use a small `fast_dev_run` for data/model wiring, then a short real run to verify logging and checkpoint callbacks: fast-dev mode does not exercise all normal callback behavior. Resume the complete training state through the version's `Trainer.fit(..., ckpt_path=...)` interface; loading a module's weights alone is not equivalent.

Verify metric names, finite losses, device placement, sample accounting across ranks, and the actual saved checkpoint. Do not hide incompatible state with `strict=False` without inspecting the mismatches.

Consult [Trainer documentation](https://lightning.ai/docs/pytorch/stable/common/trainer.html) and [LightningModule](https://lightning.ai/docs/pytorch/stable/common/lightning_module.html) for current signatures, hooks, and distributed metric behavior.
