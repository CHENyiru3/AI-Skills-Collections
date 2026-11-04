# PyTorch trainer and validation contracts

The following are development recommendations. The upstream implementation evidence is in [repository-map.md](repository-map.md); these recommendations are not claims that every reviewed repository implements them.

## Precision and optimizer updates

Start semantic checks in eager float32. Add autocast for the supported device/dtype after confirming target normalization and objective agreement. Evaluate characteristic-function/covariance statistics in float32 if lower precision distorts them. Do not hardcode CUDA in reusable modules; register constant quadrature/position tensors as buffers where appropriate.

With gradient scaling, accumulate a complete update, unscale before clipping, step/update the scaler, and identify whether the optimizer actually updated. A normal optimizer often returns `None` even on success; the return value of `scaler.step` is not a reliable success flag. Implement and test an explicit update signal appropriate to the selected PyTorch/scaler/optimizer. For the common single-optimizer dynamic scaler, scale decrease can indicate overflow; do not generalize that heuristic to multiple optimizers or custom scale policies. [PyTorch AMP examples](https://docs.pytorch.org/docs/2.15/notes/amp_examples.html).

Keep clocks separate: attempted batch, accumulation microbatch, successful optimizer update, epoch, and examples/tokens processed. In a new trainer use successful updates for update-based EMA and schedules. Do not update EMA on every microbatch. For faithful reproduction retain the source's attempted-step behavior and document it: reviewed V-JEPA loops can advance EMA even when an optimizer step is skipped.

For equal microbatches of a mean loss, divide by the accumulation count. Unequal valid-token counts need the objective's count weighting instead. Nonlinear regularizers computed on each microbatch are not equivalent to statistics on their union.

If the union objective is required, retain graph-bearing embeddings and concatenate on the example axis before one statistic/backward, or use a validated gradient-cache/recomputation method. Share one random projection matrix across that union. Retaining graphs costs activation memory; detached feature caching alone loses encoder gradients. An already averaged union loss needs no extra division by the microbatch count. Matching the objective over these outputs still does not make several BatchNorm/stochastic forwards identical to one large forward; characterize that distinction before claiming training-step equivalence.

## Objective reductions and DDP

DDP synchronizes parameter gradients; it does not automatically produce a global mean/covariance/characteristic function of features. Keep logging reductions detached from the differentiable objective. Avoid adding a second loss all-reduce merely because DDP is enabled. [PyTorch DDP design](https://docs.pytorch.org/docs/2.15/notes/ddp.html).

For a separable global token mean with standard DDP gradient averaging and unequal local counts, let rank r have differentiable sum S_r, global count C, and world size W. The local backward objective `W * S_r / C` yields the intended global mean gradient after DDP averaging. Reduce counts separately. This formula does not implement a nonlinear global regularizer; its sufficient statistics need correctly differentiated communication.

For SIGReg/covariance objectives:

1. Fix shared random projections/quadrature and use the same effective examples.
2. Compare one-process concatenated-batch loss to the distributed forward.
3. Compare full encoder/projector parameter gradients, and preferably one optimizer update. Matching scalar losses alone misses collective-backward/DDP scaling errors.
4. Check equal local counts first; either enforce that invariant or add and validate count weighting. Test unequal counts when supported.
5. Resume projection counters/RNG and repeat the comparison if changing collectives or gradient accumulation.

One useful scaling derivation: if every rank evaluates the same global regularizer from an autograd-aware SUM with SUM backward, each local feature gradient acquires a factor W from collective backward. Standard DDP's parameter-gradient averaging cancels that factor. In that specific construction, use the regularizer directly on each rank, without a further division by W. AVG collectives, gather backward conventions, or custom DDP hooks can differ. This is a derived contract to check numerically, not a substitute for the comparison above or a universal loss-scaling rule.

Do not claim multi-rank validation from the bundled single-process smoke test.

## Masks and causality

Separate three concepts: gather IDs, token validity masks, and attention permissions. A function named `apply_masks` may gather kept tokens. For PyTorch SDPA, boolean `True` permits attention; MultiheadAttention's padding-mask convention differs. SDPA dropout must receive zero explicitly at evaluation. Check the installed API and actual backend. [PyTorch SDPA](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.scaled_dot_product_attention.html).

Use ID-coded tensors to test original coordinates, sample identity, mask expansion, special tokens, and predictor reorderings. Include unequal axes and more than one example. A test using one batch element and square grids can miss transpose/order bugs.

Leakage checks hold RNG/mode constant and compare predictions before/after perturbing only forbidden content. A hidden patch can leak through overlapping convolution receptive fields, global preprocessing/normalization, or temporal tokenization before attention; test the complete input path. A causal predictor cannot repair a future-contaminated encoder state. Training targets may use future observations for supervision; those observations must not enter the prediction input.

## Teacher and frozen probes

Freeze parameters, optimizer ownership, mode, and buffers deliberately. `eval()` changes dropout/BatchNorm behavior; it does not disable autograd. `no_grad()` does not prevent running-statistic mutations. Calling `.train()` on a parent can also switch a frozen child back to training mode. [PyTorch module modes](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.eval).

Validate EMA initialization, a known weighted update, unchanged weights on a skipped update under the chosen policy, and the buffer rule. Under sharding, use framework-supported full/sharded EMA mechanisms; a naive named-parameter loop assumes compatible complete tensors.

For a frozen probe, detach/no-grad backbone features, keep the backbone mode fixed, optimize only the probe, and confirm backbone parameters and relevant buffers do not change. Record online versus teacher checkpoint key, feature layer, pooling/token selection, preprocessing, clip stride/resolution, and split identity.

## Checkpoint and resume

Distinguish strict resume from a warm-start adaptation. Strict loading should expose missing/incompatible tensors and optimizer groups, not silently replace them. Save the selected architecture, tokenizer/position convention, and source revision with the weights. Match RoPE implementation and feature-level ordering to pretrained checkpoints.

A practical checkpoint includes online encoder, predictor/projector, teacher where used, regularizer buffers/counters, optimizer, scaler, LR/WD/EMA schedule state or sufficient counters, resolved config, and RNG state for relevant libraries/devices. Include sampler epoch/cursor and collator/mask state if the promised boundary needs them. Worker prefetching can make exact mid-epoch replay difficult: prefer a stated supported boundary over a false bit-exact promise. Save atomically at completed update boundaries where possible.

Compare the next resumed batch IDs/masks, loss, learning rate, EMA momentum, and updated weights against an uninterrupted run. The bundled script checks an in-memory CPU state restore and randomized batch/mask continuation; it does not validate serialized disk checkpoints or multi-worker dataloaders.

## Failure triage

| Symptom | First discriminating checks |
|---|---|
| Loss nearly zero immediately | Context-target identity leakage; target variance across samples; accidental target reuse; trivial masks |
| Correct shapes, poor learning | ID-coded mask/sample ordering; target normalization; wrong head/depth slices; disabled regularizer |
| NaN/Inf loss or gradients | Empty masks/counts; covariance sample minimum; precision-sensitive stats; AMP unscale and component loss values |
| Collapse with teacher-free training | Regularizer axis/gradient; effective sample count; loss scaling; projection synchronization; feature covariance |
| Low one-step error, bad rollouts | Teacher forcing versus open loop; action/target shift; future leakage; rollout feedback/detach policy |
| Single GPU works, DDP differs | Scalar and parameter-gradient equivalence; nonlinear global statistics; unequal counts; collective ordering |
| Resume has a loss/EMA jump | Teacher restore; optimizer/scaler; counters; RNG/masks/data order; accidental warm start |
| Probe unexpectedly strong or unstable | Split leakage; trainable backbone; mode/buffer drift; checkpoint/preprocessing mismatch |

Prediction loss, feature variance, and probe/rollout performance answer different questions. Use all relevant signals. Per-token variability inside one example does not rule out identical representations across examples. Do not set a universal effective-rank threshold without task-specific evidence.
