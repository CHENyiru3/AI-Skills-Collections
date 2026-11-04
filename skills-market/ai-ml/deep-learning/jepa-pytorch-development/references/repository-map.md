# Repository evidence map

Reviewed **2026-11-04**. Five public repositories were pinned before reading their actual Python/configuration source through the connected GitHub tools. “Observed” below describes those source snapshots. “Recommendation” identifies engineering synthesis for new development; it does not claim that upstream already implements or validates it.

## Snapshots and source scope

| Repository | Full commit SHA | Source inspected |
|---|---|---|
| [I-JEPA](https://github.com/facebookresearch/ijepa/tree/52c1ae95d05f743e000e8f10a1f3a79b10cff048) | `52c1ae95d05f743e000e8f10a1f3a79b10cff048` | Training, helper/optimizer, image encoder/predictor, multiblock masks, tensor/distributed utilities, released ViT-H configuration |
| [V-JEPA](https://github.com/facebookresearch/jepa/tree/51c59d518fc63c08464af6de585f78ac0c7ed4d5) | `51c59d518fc63c08464af6de585f78ac0c7ed4d5` | Training/optimizer, video encoder/predictor, multimask wrappers, patch embedding, 3D masks, ViT-L configuration, frozen video classification |
| [V-JEPA 2 / 2.1 / 2-AC](https://github.com/facebookresearch/vjepa2/tree/204698b45b3712590f06245fbfba32d3be539812) | `204698b45b3712590f06245fbfba32d3be539812` | Baseline and 2.1 training, encoders/predictors/wrappers, masks, positional rotations, resume loading, AC/DROID training and causal predictor, corresponding configurations |
| [LeJEPA](https://github.com/galilai-group/lejepa/tree/c293d291ca87cd4fddee9d3fffe4e914c7272052) | `c293d291ca87cd4fddee9d3fffe4e914c7272052` | Executable minimal example, slicing and Epps–Pulley modules, DDP demonstration, README and launcher |
| [EB-JEPA](https://github.com/facebookresearch/eb_jepa/tree/966e61e9285b3a876f49b9774e9720d9a99a7925) | `966e61e9285b3a876f49b9774e9720d9a99a7925` | JEPA composition/rollout, architectures, losses, image/video/AC loops, planning, output-contract and loss-equivalence tests |

The selection spans foundational masked prediction, recent dense/deep supervision, frozen-encoder action prediction, and explicit teacher-free regularization. It is representative rather than exhaustive; it does not establish a ranking or cover every modality.

## Observed: I-JEPA

The teacher encodes the full augmented image under no-grad; its features are layer-normalized over the feature dimension before target selection. The online encoder sees context tokens; the predictor estimates the selected teacher features. The actual objective is smooth L1. EMA follows the optimizer step. [Training contract](https://github.com/facebookresearch/ijepa/blob/52c1ae95d05f743e000e8f10a1f3a79b10cff048/src/train.py#L295-L336).

The encoder adds positional embeddings and gathers context **before transformer blocks**. Full-image encoding followed by output gathering therefore changes the information available to context features. The predictor projects context to its own feature width, appends learned mask tokens with target positions, and returns target outputs in encoder width. [Encoder](https://github.com/facebookresearch/ijepa/blob/52c1ae95d05f743e000e8f10a1f3a79b10cff048/src/models/vision_transformer.py#L401-L423), [predictor](https://github.com/facebookresearch/ijepa/blob/52c1ae95d05f743e000e8f10a1f3a79b10cff048/src/models/vision_transformer.py#L285-L326).

Mask tensors contain indices to **keep**, not boolean removal flags. Multiple target/context masks use Cartesian replication: target mask, then context mask, then original sample. Repetition operates on complete batch chunks, so ordinary sample-wise `repeat_interleave` is not equivalent. [Gather and repetition](https://github.com/facebookresearch/ijepa/blob/52c1ae95d05f743e000e8f10a1f3a79b10cff048/src/utils/tensors.py#L55-L71).

The multiblock sampler truncates masks to common batch lengths. Its retry path progressively relaxes acceptable regions, so `allow_overlap: false` alone does not prove unconditional disjointness for every configuration. [Retry behavior](https://github.com/facebookresearch/ijepa/blob/52c1ae95d05f743e000e8f10a1f3a79b10cff048/src/masks/multiblock.py#L76-L104), [collation](https://github.com/facebookresearch/ijepa/blob/52c1ae95d05f743e000e8f10a1f3a79b10cff048/src/masks/multiblock.py#L137-L170).

## Observed: V-JEPA

V-JEPA uses full-clip teacher features and masked-context online features. Its objective is `mean(abs(pred-target)**p)/p`, equally averaged across configured mask pairs. The released ViT-L example uses `p=1` and zero predictor-variance regularization coefficient; the existence of regularization code does not establish that the recipe enables it. [Loss](https://github.com/facebookresearch/jepa/blob/51c59d518fc63c08464af6de585f78ac0c7ed4d5/app/vjepa/train.py#L419-L459), [configuration](https://github.com/facebookresearch/jepa/blob/51c59d518fc63c08464af6de585f78ac0c7ed4d5/configs/pretrain/vitl16.yaml#L35-L37).

Its wrappers evaluate context/target strategies in lists and zip them **1:1**, unlike I-JEPA's Cartesian contract. The underlying predictor explicitly relies on this pairing. [Wrappers](https://github.com/facebookresearch/jepa/blob/51c59d518fc63c08464af6de585f78ac0c7ed4d5/src/models/utils/multimask.py#L11-L48), [predictor constraint](https://github.com/facebookresearch/jepa/blob/51c59d518fc63c08464af6de585f78ac0c7ed4d5/src/models/predictor.py#L219-L237).

Video input is `[B,C,T,H,W]`; strided Conv3d and flattening produce width-fastest `(time,height,width)` tokens. For grid dimensions `(Tt,Ht,Wt)`, the index is `((t*Ht)+h)*Wt+w`. Mask and positional layouts must agree. [Patch embedding](https://github.com/facebookresearch/jepa/blob/51c59d518fc63c08464af6de585f78ac0c7ed4d5/src/models/utils/patch_embed.py#L31-L57).

The predictor supports a diffusion-corrupted target-input branch as well as learned mask tokens. The released ViT-L configuration selects mask tokens. Accordingly, clean-target leakage checks should apply to the chosen masked recipe without incorrectly prohibiting an intentional denoising variant. [Branches](https://github.com/facebookresearch/jepa/blob/51c59d518fc63c08464af6de585f78ac0c7ed4d5/src/models/predictor.py#L154-L217), [selected configuration](https://github.com/facebookresearch/jepa/blob/51c59d518fc63c08464af6de585f78ac0c7ed4d5/configs/pretrain/vitl16.yaml#L70-L76).

## Observed: V-JEPA 2 baseline

The baseline retains full-teacher / masked-online encoding and feature-axis target normalization. Nested groups preserve clip lengths and masking configurations. Equal averaging of per-group losses is not a global token-count-weighted mean. EMA follows the attempted optimizer step without guarding against a GradScaler-skipped update. [Objective](https://github.com/facebookresearch/vjepa2/blob/204698b45b3712590f06245fbfba32d3be539812/app/vjepa/train.py#L424-L456), [update](https://github.com/facebookresearch/vjepa2/blob/204698b45b3712590f06245fbfba32d3be539812/app/vjepa/train.py#L458-L480).

The multisequence mask generator supports truncation, optional reconstructed complements and inverted context/target roles. Inspect the actual gather contract rather than inferring semantics from “mask.” [Mask implementation](https://github.com/facebookresearch/vjepa2/blob/204698b45b3712590f06245fbfba32d3be539812/src/masks/multiseq_multiblock3d.py#L173-L269).

Baseline RoPE source documents duplicated frequencies retained for checkpoint compatibility. Silently correcting positional rotations can invalidate released-weight compatibility even if the replacement seems mathematically preferable. [Compatibility comment and implementation](https://github.com/facebookresearch/vjepa2/blob/204698b45b3712590f06245fbfba32d3be539812/src/models/utils/modules.py#L26-L55).

## Observed: V-JEPA 2.1

Dense prediction supervises **both context and target positions**, using separate predictor heads. The training loss adds target loss to a weighted context loss; context weights may depend on distance to the target. Dense supervision does not mean giving the online encoder the full clip. [Heads](https://github.com/facebookresearch/vjepa2/blob/204698b45b3712590f06245fbfba32d3be539812/app/vjepa_2_1/models/predictor.py#L171-L187), [loss](https://github.com/facebookresearch/vjepa2/blob/204698b45b3712590f06245fbfba32d3be539812/app/vjepa_2_1/train.py#L648-L703).

Deep supervision selects multiple intermediate encoder levels and concatenates them along feature channels. Targets are normalized **per level**; a single normalization across the concatenation changes the recipe. [Level selection](https://github.com/facebookresearch/vjepa2/blob/204698b45b3712590f06245fbfba32d3be539812/app/vjepa_2_1/models/vision_transformer.py#L147-L178), [target normalization](https://github.com/facebookresearch/vjepa2/blob/204698b45b3712590f06245fbfba32d3be539812/app/vjepa_2_1/train.py#L591-L627).

Image/video branches can use different temporal patch embeddings and learned modality embeddings. The inspected ViT-L recipe has equal EMA endpoints (`0.99925`), so increasing EMA momentum is not universal. [Tokenizers](https://github.com/facebookresearch/vjepa2/blob/204698b45b3712590f06245fbfba32d3be539812/app/vjepa_2_1/models/vision_transformer.py#L79-L109), [configuration](https://github.com/facebookresearch/vjepa2/blob/204698b45b3712590f06245fbfba32d3be539812/configs/train_2_1/vitl16/pretrain-256px-16f.yaml#L107-L149).

## Observed: V-JEPA 2-AC

Action-conditioned post-training uses fixed target features, with no gradient-bearing online-encoder forward and no EMA update in the AC training loop. Each frame is duplicated into a two-frame tokenizer input and encoded independently, avoiding future-frame information in a state's latent representation. [Framewise targets](https://github.com/facebookresearch/vjepa2/blob/204698b45b3712590f06245fbfba32d3be539812/app/vjepa_droid/train.py#L408-L415), [update](https://github.com/facebookresearch/vjepa2/blob/204698b45b3712590f06245fbfba32d3be539812/app/vjepa_droid/train.py#L443-L470).

The predictor interleaves action, state and image tokens and uses **frame-block causal attention**: tokens within one timestep can attend to each other and earlier timesteps. This differs from strict token-triangular attention. [Conditioning layout](https://github.com/facebookresearch/vjepa2/blob/204698b45b3712590f06245fbfba32d3be539812/src/models/ac_predictor.py#L136-L188), [causal mask](https://github.com/facebookresearch/vjepa2/blob/204698b45b3712590f06245fbfba32d3be539812/src/models/utils/modules.py#L12-L23).

Training combines teacher-forced next-step and differentiable autoregressive rollout losses. Targets are shifted by a frame's token count; rollout predictions feed subsequent steps without detach in this loop. Test action/time alignment separately from shape correctness. [Rollout and targets](https://github.com/facebookresearch/vjepa2/blob/204698b45b3712590f06245fbfba32d3be539812/app/vjepa_droid/train.py#L417-L449).

## Observed: LeJEPA

The minimal path uses one trainable encoder/projector on multiple views, with invariance around their mean plus SIGReg. Gradients pass through all views and the view mean; there is no teacher, EMA, detached target or explicit predictor in that path. A probe consumes detached backbone features. [Encoding](https://github.com/galilai-group/lejepa/blob/c293d291ca87cd4fddee9d3fffe4e914c7272052/MINIMAL.md#L78-L93), [loss/probe](https://github.com/galilai-group/lejepa/blob/c293d291ca87cd4fddee9d3fffe4e914c7272052/MINIMAL.md#L164-L183).

SIGReg uses normalized random projection directions and an Epps–Pulley statistic comparing empirical characteristic functions to a standard normal target. In the minimal `[V,N,D]` layout, statistics are computed over `N` separately for each view. Pooling view/sample axes changes the objective. [Minimal statistic](https://github.com/galilai-group/lejepa/blob/c293d291ca87cd4fddee9d3fffe4e914c7272052/MINIMAL.md#L56-L75).

The library registers a projection-step buffer and synchronizes projection seeds across ranks. Its Epps–Pulley implementation uses functional distributed reductions and sample-count scaling; averaging rank means implicitly assumes equal local counts. The DDP demonstration is not a proof of complete gradient equivalence. [Slicing](https://github.com/galilai-group/lejepa/blob/c293d291ca87cd4fddee9d3fffe4e914c7272052/lejepa/multivariate/slicing.py#L91-L153), [statistic](https://github.com/galilai-group/lejepa/blob/c293d291ca87cd4fddee9d3fffe4e914c7272052/lejepa/univariate/epps_pulley.py#L62-L99).

Check signatures against documentation: the inspected constructor uses `n_points`, although README's quick start uses `num_points`. [Constructor](https://github.com/galilai-group/lejepa/blob/c293d291ca87cd4fddee9d3fffe4e914c7272052/lejepa/univariate/epps_pulley.py#L62-L78), [README example](https://github.com/galilai-group/lejepa/blob/c293d291ca87cd4fddee9d3fffe4e914c7272052/README.md#L101-L118).

The minimal example also uses LR scheduling despite broader simplification claims. These are reasons to verify executable behavior rather than inherit slogans as requirements. [Optimizer and schedule](https://github.com/galilai-group/lejepa/blob/c293d291ca87cd4fddee9d3fffe4e914c7272052/MINIMAL.md#L144-L183).

## Observed: EB-JEPA

Its reusable model separates encoder, action encoder, predictor, regularizer and prediction cost. Encoded targets participate in gradients; explicit distribution regularization replaces the EMA-teacher recipe in these examples. Do not transfer this gradient topology to masked-teacher models accidentally. [Composition](https://github.com/facebookresearch/eb_jepa/blob/966e61e9285b3a876f49b9774e9720d9a99a7925/eb_jepa/jepa.py#L9-L42), [state gradients and regularizer](https://github.com/facebookresearch/eb_jepa/blob/966e61e9285b3a876f49b9774e9720d9a99a7925/eb_jepa/jepa.py#L122-L139).

Parallel teacher-forced and autoregressive paths explicitly manage context, next-state alignment and action slices. Architectures have different context requirements: the state-only video wrapper combines two frames, while the GRU predictor takes a state/action pair. [Rollouts](https://github.com/facebookresearch/eb_jepa/blob/966e61e9285b3a876f49b9774e9720d9a99a7925/eb_jepa/jepa.py#L141-L205), [two-frame wrapper](https://github.com/facebookresearch/eb_jepa/blob/966e61e9285b3a876f49b9774e9720d9a99a7925/eb_jepa/architectures.py#L107-L128).

VC treats spatial/temporal positions as samples; composite regularizers expose other axis choices. BCS and LeJEPA SIGReg differ in invariance reduction, weighting, quadrature and sample-count scaling, so their coefficients are not numerically interchangeable. EB-JEPA's BCS helper uses an ordinary Python step counter and raw in-place distributed reduction. [VC](https://github.com/facebookresearch/eb_jepa/blob/966e61e9285b3a876f49b9774e9720d9a99a7925/eb_jepa/losses.py#L16-L111), [BCS](https://github.com/facebookresearch/eb_jepa/blob/966e61e9285b3a876f49b9774e9720d9a99a7925/eb_jepa/losses.py#L349-L401).

Its upstream tests provide useful examples of loss equivalence and rollout/action-bound contracts. Pixel decoders in examples are probes, not a requirement that JEPA pretraining reconstruct pixels. [Loss tests](https://github.com/facebookresearch/eb_jepa/blob/966e61e9285b3a876f49b9774e9720d9a99a7925/tests/test_loss_equivalences.py#L121-L160), [rollout tests](https://github.com/facebookresearch/eb_jepa/blob/966e61e9285b3a876f49b9774e9720d9a99a7925/tests/test_jepa_output_formats.py#L352-L487).

## Observed: lifecycle and evaluation details

I-JEPA and V-JEPA use AdamW with bias/one-dimensional no-decay groups, warmup-cosine LR, cosine WD and linear EMA schedules between configured endpoints. These are source recipe choices, not requirements for all families. [I-JEPA optimizer](https://github.com/facebookresearch/ijepa/blob/52c1ae95d05f743e000e8f10a1f3a79b10cff048/src/helper.py#L121-L156), [EMA schedule](https://github.com/facebookresearch/ijepa/blob/52c1ae95d05f743e000e8f10a1f3a79b10cff048/src/train.py#L227-L229).

Pretraining checkpoints contain online/predictor/teacher, optimizer, scaler and epoch metadata; schedules/mask counters are replayed from epoch times iterations. These files do not establish bit-exact mid-epoch replay. I-JEPA catches load failures and resets epoch; 2.1 can tolerate missing/incompatible weights or optimizer groups. Such behavior is suitable only when an explicitly chosen warm-start policy permits it. [I-JEPA resume/save](https://github.com/facebookresearch/ijepa/blob/52c1ae95d05f743e000e8f10a1f3a79b10cff048/src/train.py#L231-L264), [2.1 adaptation loader](https://github.com/facebookresearch/vjepa2/blob/204698b45b3712590f06245fbfba32d3be539812/app/vjepa_2_1/utils.py#L125-L169).

Frozen V-JEPA evaluation sets the encoder to eval, disables its parameter gradients and uses no-grad forward while training an attentive classifier. Evaluation defaults to teacher weights, with an explicit encoder fallback. [Freeze](https://github.com/facebookresearch/jepa/blob/51c59d518fc63c08464af6de585f78ac0c7ed4d5/evals/video_classification_frozen/eval.py#L177-L187), [checkpoint selection](https://github.com/facebookresearch/jepa/blob/51c59d518fc63c08464af6de585f78ac0c7ed4d5/evals/video_classification_frozen/eval.py#L414-L438).

## Recommendations distilled into the skill

The following are development recommendations informed by those contrasts; they are not uniform upstream behavior.

| Skill decision | Evidence motivating it |
|---|---|
| Choose the JEPA family before drawing the gradient graph. | Masked EMA targets, fixed AC targets, LeJEPA all-view gradients and EB-JEPA target gradients differ. |
| Make token/view/sample/time/mask axes explicit; test with index-coded data. | Cartesian and paired wrappers can have compatible shapes but different sample alignment. |
| Preserve target normalization and exact reductions when reproducing. | Smooth L1, L1/power losses, per-group means, per-level normalization and sample-scaled regularizers differ. |
| State the anti-collapse mechanism and monitor it independently of prediction error. | EMA/predictor asymmetry and explicit distribution regularization are distinct designs; small matching loss alone proves neither quality nor non-collapse. |
| For a new trainer, define the update clock and EMA/buffer policy. | Upstream loops can advance EMA despite a skipped optimizer step; no-grad does not itself freeze BatchNorm/dropout behavior. |
| Validate global regularizers against a concatenated-batch reference. | Shared random directions, sample counts, autograd collectives and DDP gradient averaging all affect results. |
| Separate strict resume from warm-start. | Epoch replay and permissive shape adaptation cannot silently satisfy an exact-continuation promise. |
| Test causal behavior by perturbing future inputs and evaluate open-loop horizons. | Fixed framewise AC encodings, frame-block attention and autoregressive feedback create separate leakage/alignment risks. |
| Record encoder/checkpoint, pooling, preprocessing and probe protocol. | A frozen teacher-feature probe is a different experiment from fine-tuning online representations. |

For new implementations, use current PyTorch APIs appropriate to the installed environment. Prefer input-derived devices and registered statistic buffers; unscale AMP gradients before clipping. Preserve historical operations when released-weight reproduction requires them, and document changes.

For exact continuation where supported, save global update count, configuration and code revision, schedule states, regularizer/mask counters, relevant RNG states and sampler position. Verify next-step behavior after restoring rather than claiming exactness from checkpoint field names.

For action-conditioned augmentation, transform actions/states consistently with the image coordinate change. The supplied AC configuration disables horizontal flipping; the broader coordinate-consistency rule is engineering inference.

The resulting validation priorities depend on the selected path:

- Masked teacher models: verify information visibility, gather alignment, target gradients and EMA arithmetic.
- Dense/deep models: additionally verify context/target heads, per-level channels and normalization.
- Teacher-free regularized models: verify sample/view axes, distribution statistics and global-batch gradients.
- Action-conditioned models: additionally verify transition/action shifts, causal influence and open-loop horizons.

## Limits and reuse

- This review read source; it did not run upstream training, upstream suites, CUDA/DDP experiments, checkpoint downloads or benchmark reproduction.
- The skill's standalone smoke test is newly written engineering code. **No upstream source code was copied into it.** Passing it checks its stated synthetic contracts; it does not validate these repositories or reproduce their results.
- Code licenses vary, and source, checkpoints and datasets can have different terms. I-JEPA's inspected source license is noncommercial. Check the selected repository revision and artifact terms before copying implementation or distributing weights.
- The immutable links preserve reviewed behavior; future branches and APIs may differ. Re-check signatures and configurations when adapting a newer revision.
- No recommendation here establishes theoretical collapse prevention, planning safety, causal correctness or downstream accuracy. Those need evidence from the actual model, data and evaluation protocol.
