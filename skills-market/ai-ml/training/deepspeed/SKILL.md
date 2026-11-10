---
name: deepspeed
domain: ai-ml
description: Configure or debug DeepSpeed engines, ZeRO stages, offloading, mixed precision, checkpointing, or a supported Transformers/Accelerate integration. Use for an actual DeepSpeed workload.
license: MIT license
metadata:
  version: "1.0.1"
  skill-author: Eric Yiru
---

# DeepSpeed

Identify the installed DeepSpeed/PyTorch versions, launcher, host framework, model/loss contract, hardware, and memory bottleneck. Choose native engine or framework integration deliberately.

## Engine and batch contract

- Native `deepspeed.initialize` returns an engine and associated objects. Feed model inputs to the engine, compute a differentiable scalar task loss, then use `engine.backward(loss)` and `engine.step()`. A linear layer's batch-by-output prediction is not itself a scalar training loss.
- Reconcile global train batch with microbatch per data-parallel rank, gradient accumulation, and data-parallel world size. Tensor/pipeline parallel ranks do not all represent independent data-parallel samples.
- With Transformers or Accelerate, let that integration own initialization, precision, optimization, accumulation, and checkpointing. Do not initialize a second independent engine around it.

## Configure from the actual workload

| ZeRO stage | Partitioned state |
| --- | --- |
| 1 | Optimizer state |
| 2 | Optimizer state and gradients |
| 3 | Optimizer state, gradients, and parameters |

Choose the smallest sufficient strategy after measuring actual memory and communication. There is no fixed 4x/8x saving across workloads. Activations, temporary buffers, communication buckets, and caches remain relevant.

Use stage-appropriate, supported keys and numeric types from the installed configuration reference. Integration-specific `"auto"` values must be resolved by that integration before reaching native DeepSpeed; they are not a universal native configuration feature. Do not enable incompatible fp16 and bf16 modes together.

Offload optimizer/parameters only where supported. Account for CPU RAM, pinned memory, NVMe capacity and bandwidth, and throughput cost. Verify compiler/kernel compatibility before enabling optional operations. Quantized PEFT plus ZeRO needs a supported recipe, not an arbitrary combination of examples.

## Checkpoints, inference, and verification

- Distinguish a partitioned training checkpoint from consolidated model weights. Save/load using the engine or host integration's documented collective semantics and exact stage/version. Keep configuration and optimizer/scheduler state when promising resume.
- Do not assume a single rank's shard is a complete model. Consolidate through supported tools when required and verify reloaded outputs.
- Training ZeRO, inference tensor parallelism, and pipeline parallelism have different APIs. A list of layer names in an invented JSON block does not build a pipeline model; follow the actual supported module/engine contract.
- Run a short launch with the chosen topology; inspect scalar finite loss, gradients, effective batch, per-rank peak memory, and checkpoint round-trip. Profile before tuning communication buckets or offload settings.

Consult [DeepSpeed configuration](https://www.deepspeed.ai/docs/config-json/), [training API](https://deepspeed.readthedocs.io/en/latest/training.html), and the host framework's versioned integration guide.
