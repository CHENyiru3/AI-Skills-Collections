---
name: jepa-pytorch-development
description: Design, implement, adapt, or debug JEPA representation learners and latent world models in PyTorch. Use for masked EMA-teacher JEPA, V-JEPA dense/deep supervision, teacher-free LeJEPA/SIGReg, or action-conditioned latent prediction, including token and mask contracts, gradient flow, collapse diagnostics, distributed losses, and checkpointing.
---

# JEPA development in PyTorch

Build around an explicit prediction task and information boundary. Choose a coherent recipe before borrowing components. A JEPA name alone does not specify masking, an EMA teacher, a predictor, or the collapse-prevention mechanism.

## Select the recipe

Inspect the user's code, configuration, pretrained checkpoint, compute budget, and downstream task. Infer routine choices; ask only when an unresolved choice changes the model's meaning. Distinguish reproduction, a deliberate variant, debugging, and transfer to a new modality.

| Task | Starting family | Read when needed |
|---|---|---|
| Predict missing image/video features | I-JEPA / V-JEPA / V-JEPA 2: visible-token encoder, positional predictor, stopped EMA targets | [Masked EMA](references/recipes.md#masked-ema-teacher) |
| Learn dense video features at multiple depths | V-JEPA 2.1: visible/masked prediction with aligned intermediate targets | [Dense/deep supervision](references/recipes.md#dense-and-deep-supervision) |
| Learn view-invariant representations without a teacher | LeJEPA: shared encoder/projector, invariance plus SIGReg | [Teacher-free learning](references/recipes.md#teacher-free-regularized-learning) |
| Predict future states conditioned on actions | Frozen-encoder V-JEPA 2-AC, or explicitly regularized joint training | [World models](references/recipes.md#action-conditioned-world-models) |

For attribution or faithful reproduction, consult the commit-pinned [repository map](references/repository-map.md). It distinguishes observed source behavior from engineering recommendations. Do not claim benchmark reproduction from a toy smoke test.

## Define the contracts before implementing the loss

Write these in the project's existing config/design conventions:

- Input units/layout, tokenizer geometry, flattening order, padding and validity. For a standard video grid, `N = T_tokens * H_tokens * W_tokens`; assert actual tokenizer output agrees.
- Context/target indices in original coordinates, with batch, view, mask, time, and layer axes named. Specify paired versus Cartesian multi-mask expansion and prediction-target alignment.
- Allowed online/predictor inputs, permitted overlap, target normalization, prediction dimensions, reduction denominators, and component weights.
- Gradient ownership: optimized, frozen, or EMA-updated modules; teacher train/eval behavior and mutable-buffer policy.
- Augmentations and split units. Preserve correspondence within a masked-prediction pair; use the chosen view policy for invariance. Split trajectories by episode/entity where appropriate.

Keep encoder/tokenizer, predictor, target construction, mask sampler, objective, and trainer boundaries clear. Reuse the project structure; an upstream directory layout is not a JEPA requirement.

## Preserve the learning signal

**Masked EMA branch.** Remove hidden tokens before online operations that mix token content. Gathering after full self-attention leaks targets. Full-input tokenization is compatible only if receptive fields and normalization respect the hidden boundary. Keep original positional coordinates after gathering. In the standard mask-token recipe the predictor receives encoded context plus target coordinates/queries, never clean target features. An explicitly chosen denoising predictor is a different contract; preserve its corruption process and document it. The teacher may encode the full augmented input under `no_grad`; normalize and gather in recipe order. Exclude teacher parameters from the optimizer.

**Regularized branch.** Gradients normally flow through all views of the shared encoder/projector. Keep invariance and anti-collapse regularization distinct. Do not add a teacher or detach the view mean by analogy with I-JEPA. Match the regularizer's statistical axes and distributed implementation.

**Action-conditioned branch.** Express `state_t + action_t -> state_(t+1)`, including timestamps and action units. Separate observed context, future supervision, and open-loop rollout. Frozen encoders, jointly trained encoders, and EMA targets are different choices.

Treat replacing LayerNorm targets with L2-normalized vectors, Smooth L1 with MSE, or a weighted stream mean with a global mean as an experiment. Record the change and compare with the coherent baseline.

## Implement optimizer time and distributed statistics deliberately

Read [training-and-validation.md](references/training-and-validation.md) when building a trainer, changing precision/DDP, or debugging resume.

- Use float32 for sensitive normalization, reductions, and regularizer statistics unless another path is established safe.
- Reduce over the intended unit: example, valid token, mask stream, head, layer, or horizon. Padding contributes neither loss nor count. Equal stream and equal token weights differ for unequal lengths.
- For EMA, copy the initial encoder, freeze teacher gradients, match parameter names/shapes, handle buffers separately, and specify the momentum schedule's clock.
- For a new trainer, advance update-based EMA/LR/WD schedules after successful optimizer updates, respecting AMP skips and accumulation. For reproduction, preserve and report upstream timing.
- DDP gradient synchronization does not implement global feature statistics. Keep regularizer communication differentiable and verify parameter-gradient scaling. Accumulation does not automatically enlarge a nonlinear regularizer's statistical batch.
- Save model/predictor/teacher where used, optimizer, scaler, schedule counters, resolved config, and relevant RNG/sampler/mask state. Define and test the supported resume boundary.

## Verify before scaling

Select checks relevant to the change. For a new model/trainer establish:

1. **Identity and alignment:** token values encode sample/view/time/token IDs; verify actual multi-mask pairing, not just shape. Reject invalid IDs, empty selections, unintended duplicates, and prohibited overlap. Bound mask sampling retries and report infeasible configurations.
2. **Information boundary:** hold stochastic state fixed, perturb hidden inputs, and confirm online context/predictions stay unchanged. For causal dynamics perturb future observations/actions and check earlier predictions. Test the actual tokenizer and attention path.
3. **Gradient ownership:** intended modules get finite nonzero gradients; frozen/EMA targets get none and have no optimizer membership. In teacher-free learning check all intended views and the regularizer independently.
4. **Update/resume:** check EMA arithmetic, skipped-step timing, and the next supported resumed update against uninterrupted training.
5. **Learning quality:** overfit a tiny fixed batch to detect wiring errors, then track cross-sample variability, covariance/effective rank or comparable collapse signals, and a held-out frozen probe or rollout metric. Falling prediction loss alone does not establish useful representations.

The optional [CPU contract smoke test](scripts/smoke_masked_jepa.py) demonstrates a tiny masked EMA branch, original-position gathering, leakage checking, gradient isolation, EMA, and deterministic in-memory resume:

```bash
python scripts/smoke_masked_jepa.py
```

It requires PyTorch and no datasets/checkpoints/network. It is original educational code, not an upstream model, collapse test, distributed test, or substitute for checks on the user's implementation.

## Adapt or debug one controlled change at a time

For a new modality choose the prediction unit, coordinates/topology, valid augmentations, missing regions or future horizons, target representation, and collapse mechanism before copying a vision sampler. Unordered sets, molecular graphs, and irregular spatial samples do not inherit raster positions or temporal causality automatically.

When debugging inspect a concrete batch and IDs, ownership, target variance, component losses, and counters first. Use [failure triage](references/training-and-validation.md#failure-triage) to narrow causes. Add scaling optimizations after semantic checks pass; compare numerics and gradients with the reference path.

Deliver the requested implementation or diagnosis, selected recipe/deviations, checks actually run, and evidence limits. Separate a plausible adaptation from a demonstrated scientific improvement.
