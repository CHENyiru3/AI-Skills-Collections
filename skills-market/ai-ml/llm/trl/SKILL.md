---
name: trl
domain: ai-ml
description: Implement or debug TRL supervised fine-tuning, preference optimization, reward modeling, or reinforcement-learning trainers, including their dataset schemas and evaluation. Use for a specific TRL workflow.
license: Apache-2.0 license
metadata:
  version: "1.0.1"
  skill-author: Eric Yiru
---

# TRL training

Record TRL, Transformers, PEFT, and backend versions. Choose the actual objective before selecting a trainer; SFT, DPO, reward modeling, and online RL have different data, model, and sampling contracts.

## Establish the supported path

- Read the installed trainer/config signatures and matching official example. Configuration fields move between trainer constructors and config classes across releases; do not mix legacy `tokenizer`/length arguments with current APIs blindly.
- Use a trainer that exists in that release. Do not invent a universal `RLHFTrainer`/`RLHFConfig`, `get_train_batch`, sampler, or `loss_type="custom"` implementation.
- Fix model and tokenizer revisions, task-appropriate head, chat template, pad/EOS behavior, precision, and distributed strategy. Match PEFT/quantized training to supported integrations.

## Validate the data contract

- **SFT:** select language-model text/messages or prompt-completion records supported by the trainer. Decide whether loss covers all tokens, completions, or assistant messages; inspect actual masks after templating/truncation/packing.
- **Preference training:** inspect real rows before mapping fields. Use supported chosen/rejected formats with an explicit prompt where applicable, or an accepted implicit-prompt format. Do not assume a source such as HH-RLHF has a `prompt` column. Extract shared context correctly if conversion is required.
- **Reward modeling:** compare compatible chosen/rejected continuations for the same context; validate scalar scoring head, padding, truncation, and pair ordering.
- **Online RL:** supply the required prompt dataset, rollout mechanism, reward function/model, reference policy, and any value model for that algorithm/version. Validate reward shape, range, generation boundaries, EOS handling, and reference freezing.

Keep related prompts/conversations/subjects together across splits. Inspect duplicates, preference direction, length bias, and any data transformations that could remove the distinguishing answer tokens.

## Run and evaluate

1. Materialize a tiny batch and inspect rendered text, token IDs, masks, and target structure.
2. Run one short supported training path; check finite losses, gradients, effective batch/accumulation accounting, and trainable parameters.
3. For preference/RL objectives, monitor reference divergence, reward distribution, completion length and diversity, and degeneracy. A toy length reward is not evidence of alignment quality.
4. Evaluate held-out prompts and task behavior independently of training reward. Do not claim that a rising reward proves better answers.
5. Save the actual model/adapter, tokenizer/template, configuration, data revision, and resume state needed by the chosen trainer. Verify reload and describe precisely what was tested.

Use [TRL trainer documentation](https://huggingface.co/docs/trl/) and [dataset formats](https://huggingface.co/docs/trl/dataset_formats); select versioned pages when reproducing an older run.
