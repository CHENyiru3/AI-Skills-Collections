---
name: accelerate
domain: ai-ml
description: Configure or debug Hugging Face Accelerate launchers, Accelerator training loops, mixed precision, accumulation, distributed metrics, and checkpoint resume. Use when the project uses Accelerate.
license: Apache-2.0 license
metadata:
  version: "1.0.1"
  skill-author: Eric Yiru
---

# Accelerate

Inspect the installed Accelerate version, launcher, device topology, existing training framework, and effective batch definition. Avoid wrapping a Trainer-managed loop in an unrelated second `Accelerator`.

## Launch and preparation

Use launcher configuration through `accelerate launch --config_file <path> train.py` or supported launch flags. Process count and distributed backend are launch concerns; do not pass `config_file`, `distributed_type`, or `num_processes` as invented `Accelerator` constructor arguments.

Create the model, optimizer, loaders, and any supported scheduler, then prepare the relevant objects once with `accelerator.prepare`. Use prepared objects for the loop and inspect actual batch/device placement.

## Accumulation and precision

```python
# Assumes accelerator was configured with gradient_accumulation_steps,
# and model, optimizer, loader were prepared together.
for inputs, targets in loader:
    with accelerator.accumulate(model):
        loss = criterion(model(inputs), targets)
        accelerator.backward(loss)
        optimizer.step()
        optimizer.zero_grad()
```

`accelerator.backward` handles the configured accumulation scaling; do not divide the same loss by that factor again. Distinguish batch-mean accumulation from exact normalization with unequal numbers of valid tokens or examples. Check final partial windows and distributed sample accounting.

Use supported precision settings and hardware. Use Accelerate's clipping interface at synchronization boundaries when clipping is needed. Check scheduler-step ownership and skipped optimizer steps; do not automatically multiply learning rate by process count.

## Metrics and persistence

- Gather metrics through the supported metric-aware interface, accounting for duplicated/padded end batches and unequal sample counts. Compute on the correct device; do not reduce rank-local CPU tensors with an incompatible backend.
- Run collective operations on all required ranks. Restrict ordinary file/log side effects to the appropriate main process, but do not restrict sharded checkpoint collectives to rank zero blindly.
- Use `save_state`/`load_state` for supported training-state resume, including registered stateful objects. Weight export is a separate operation using supported model save/unwrapping/state-dict APIs.
- `accelerator.save` needs an object and destination; do not invent `accelerator.load` or `get_states` for gradient inspection. Inspect parameter gradients directly and distinguish synchronization triggers from diagnostics.

Check one process first, then a short launched run for changes involving distribution or resume. Report topology, effective batch, observed metrics, and whether reload was exercised.

Consult [Accelerator reference](https://huggingface.co/docs/accelerate/package_reference/accelerator), [launch CLI](https://huggingface.co/docs/accelerate/package_reference/cli), and version-matched integration guides.
