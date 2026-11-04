# JEPA recipe decisions

These are engineering deductions from the pinned sources in [repository-map.md](repository-map.md). Numbers, loss forms, axes, and schedules observed in one configuration are not universal defaults. Follow the requested checkpoint/config when reproducing; label deliberate deviations.

## Masked EMA teacher

Applies to the standard learned-mask-token paths in I-JEPA, V-JEPA, and V-JEPA 2.

The online encoder sees visible token content. A predictor combines context representations with target positions and predicts full-input teacher features at withheld positions. The teacher starts as an encoder copy, receives no optimizer gradients, and follows parameter EMA:

`teacher_next = momentum * teacher_current + (1 - momentum) * online_after_step`.

The teacher and predictor serve different purposes: the teacher constructs stable targets; the predictor solves the conditional prediction task. Their presence alone does not prove non-collapse.

### Axes, masks, and positions

- For `tokens[B,N,D]`, an upstream integer mask `[B,K]` usually contains **indices to keep**. Check the gather implementation rather than the variable name or docstring. Boolean attention masks have a separate meaning.
- In the examined Conv3d tokenizer, input `[B,C,T,H,W]` becomes `[B,N,D]` with `id = ((t * H_tokens) + h) * W_tokens + w`. Non-square grids and more than one temporal slice make useful alignment fixtures.
- I-JEPA expands context and target masks into Cartesian combinations, ordered by target mask, context mask, then original batch. V-JEPA wrappers pair lists 1:1. Never substitute a per-element `repeat_interleave` for repetition of complete batch chunks without an identity test.
- Preserve original positions. Renumbering gathered context `0..K-1` changes positional meaning. Track special tokens separately from patch IDs. Check sorting and inverse-sorting at the predictor output.
- Structured spatial/temporal block sizes determine prediction difficulty. A pixel dropout pattern or arbitrary mask percentage is not automatically a faithful substitute. Upstream samplers truncate selected lengths for batching; a padded implementation needs explicit validity and loss-count handling.
- Enforce the intended visibility rule. I-JEPA's retry fallback can relax overlap constraints; do not turn that artifact into a desired behavior of a new sampler. Bound retries and reject impossible requests.

### Target construction and objective

The teacher encodes the full, geometrically matching augmented input under `torch.no_grad()`. Feature-axis LayerNorm precedes target gather in the baseline paths. L2 normalization changes target geometry.

| Inspected baseline | Actual objective |
|---|---|
| I-JEPA | Smooth L1 between predicted and teacher feature tokens |
| V-JEPA / V-JEPA 2 | `mean(abs(pred-target)**p) / p`, then equal mean over configured groups; released examples use `p=1` |
| V-JEPA optional variance penalty | Implemented, but disabled with coefficient zero in the examined released ViT-L config |

Expose target normalization, loss exponent/Huber parameter, per-group weighting, and validity semantics explicitly. Avoid accidentally increasing loss magnitude when adding masks or longer clips. Equal group means intentionally give a short and long stream equal weight; preserve this when reproducing.

V-JEPA also has an explicit diffusion-corrupted target-feature branch when learned mask tokens are disabled. That is a denoising task, not permission to pass clean targets into the standard mask-token predictor. Test the selected forward path rather than assuming every available path is used by a released config.

### Teacher lifecycle

Freeze teacher parameters and omit them from optimizer groups. `no_grad` prevents graph creation; `eval` controls stochastic/stateful module behavior. Neither substitutes for the other. The teacher's mode and buffer-update rule must be chosen for the actual backbone. ViT examples with no running BatchNorm statistics do not settle that choice for CNNs.

Match EMA parameters by name and shape after unwrapping wrappers. Decide whether floating buffers are copied, averaged, or independently updated; integer counters are not averaged. Use a recipe-specific momentum curve: inspected I/V baselines use a linear interpolation, while a supplied 2.1 recipe uses constant endpoints. Do not assume cosine or a fixed value.

## Dense and deep supervision

V-JEPA 2.1 modifies the masked EMA branch; it does not remove the online information boundary.

- Predict teacher features at both withheld and visible positions. The examined predictor uses separate masked/context output projections and reorders tokens back to their respective IDs.
- Keep masked and context losses separate: `loss = target_loss + lambda(step) * context_loss`. The source additionally supports distance weights for context. Preserve the exact weight normalization and averaging axes; weights affect effective learning rate as well as emphasis.
- Select intermediate layers explicitly. In the examined implementation, multiple representations are individually normalized and concatenated along channels; the predictor maps from/to `levels * encoder_dim`. Teacher target normalization is **per level**, not one LayerNorm across the concatenation.
- Assert teacher/online layer ordering and channel slices. Check each head/level's finite loss and gradients, and ensure a layer with a small feature scale is not accidentally underweighted.
- Check image and video streams independently. The source supports distinct image/video tokenizers, different temporal tubelet sizes, modality embeddings, and nested groups for different sequence lengths. Reusing video-grid masks on the image grid is unsafe without validation.
- Match the exact RoPE/position implementation of pretrained weights. The V-JEPA 2 source retains a documented frequency-duplication bug for checkpoint compatibility; a silent correction changes the model being loaded.

Adopt these components when dense downstream features are needed, or when reproducing this family. Adding every head and supervision depth to a small baseline without an ablation needlessly changes the research question.

## Teacher-free regularized learning

### LeJEPA

The inspected minimal path uses a shared encoder and projector over views, `z[V,B,D]`, with:

`invariance = mean((z - mean(z, dim=view))**2)`

`loss = (1 - lambda) * invariance + lambda * SIGReg(z)`.

There is no explicit masked predictor, teacher, or target detach in that path. Gradients flow through all views and their mean. Keep backbone embeddings separate from projector outputs; frozen probes consume detached backbone features.

Nuance for debugging: detaching the exact view mean in this unweighted squared-deviation expression leaves its first-order gradients unchanged, because residuals sum to zero over views. Preserve the source graph, but do not diagnose that detach alone as a demonstrated gradient bug; weighting, asymmetric targets, or other losses require separate analysis.

SIGReg applies a univariate distribution test to random unit-direction projections. The Epps–Pulley statistic compares empirical sine/cosine characteristic-function averages to a standard normal characteristic function, using numerical quadrature. Preserve the following:

- The sample axis is B, separately for each view in the minimal implementation. Pooling views and samples changes the test.
- Projection directions, count, quadrature nodes/weights, sample-count factor, and loss reductions define the scale. Record them with the regularization weight.
- The reusable library generates projections on the input device and registers a step counter; do not copy the minimal example's hardcoded CUDA assumptions.
- Global statistics require the same projection directions on all ranks, differentiable reductions, and count-correct means. The inspected library averages local means and uses `B * world_size`; this presumes equal local counts.
- Read real constructor signatures. At the pinned revision, the README's `num_points` example disagrees with the implementation's `n_points` argument.

Do not assume “teacher-free” eliminates all scheduling; the minimal example still schedules optimizer learning rate. Test distribution regularization independently of invariance, including finite gradients for valid small batches and sensitivity to collapsed versus varied inputs. At exact symmetry some penalties can have zero gradients; this check does not establish a universal guarantee against collapse.

### EB-JEPA

The library decomposes encoder, action encoder, predictor, regularizer, and prediction cost. Its predictive paths train encoded targets as part of a joint gradient graph, with explicit regularization instead of EMA. Preserve this choice rather than importing stopped targets from I-JEPA.

VC regularization reshapes feature maps into samples/channels; choices such as pooling temporal/spatial positions, first-step-only statistics, temporal penalties, and inverse dynamics alter the task. Correlated positions are not automatically independent examples.

Its BCS image objective differs numerically from LeJEPA's minimal SIGReg objective: pairwise MSE versus variance around a view mean, different weighting/quadrature, and no matching sample-count multiplier. Trade-off weights are not portable. The inspected raw in-place distributed reduction is not sufficient evidence of correct backward semantics; validate against a concatenated-batch reference before adopting it for global training.

## Action-conditioned world models

Choose between a frozen representation space and jointly trained representations with explicit anti-collapse regularization. V-JEPA 2-AC uses a frozen pretrained target encoder and optimizes the predictor, with no EMA update in its AC loop. EB-JEPA offers jointly trainable predictive examples. Neither choice applies automatically to every world model.

For V-JEPA 2-AC:

- The training code encodes each frame independently, duplicating it to satisfy the pretrained video tokenizer. Encoding a whole bidirectional clip could leak future observations into an apparently current latent, even with a causal predictor.
- Actions, robot states, optional extrinsics, and visual patches are interleaved by timestep. Attention is frame-block causal, allowing within-timestep interactions and previous frames; a plain token-level triangle is a different model.
- Teacher-forced next-step loss and autoregressive rollout loss are separate components. The source feeds predictions back differentiably for its short rollout. Detaching them changes optimization.

For all sequence predictors define context length C, prediction horizon H, latent token stride, action indices, and target shift. EB-JEPA's state-only video example uses two-frame context; do not force it into a single-state interface. Define whether re-fed left context is observed or predicted.

If fixing a leaked encoding protocol, preserve the pretrained encoder weights but invalidate/recompute latent caches and retrain or adapt the predictor to the corrected features. Future measured proprioceptive states, extrinsics, and derived conditioning can leak too: rollout must use only information available at that step, candidate actions, and an explicit state-transition rule. Holding out future camera frames alone is insufficient.

Augment robot images and actions/states consistently. A horizontal flip can change the coordinate interpretation; resizing, cropping, and camera transformations may require geometry-aware handling. Use the project's coordinate system rather than generic image-SSL assumptions.

Evaluate teacher-forced error, open-loop drift by horizon, action sensitivity, and task-relevant planning outcomes separately. Causal counterfactual checks should perturb future frames, future actions, and future state independently, while an allowed current action should influence its intended next-state prediction. A planner must receive only available context and candidate actions.
