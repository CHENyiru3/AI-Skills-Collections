---
name: peft
domain: ai-ml
description: Configure, train, load, switch, merge, or debug Hugging Face PEFT adapters such as LoRA, QLoRA, prompt tuning, and prefix tuning. Use when an actual PEFT adapter workflow is requested.
license: Apache-2.0 license
metadata:
  version: "1.0.1"
  skill-author: Eric Yiru
---

# PEFT adapters

Inspect the base model/revision, PEFT/Transformers versions, task head, quantization, target modules, and intended training or inference workflow.

## Configure the adapter

- Select a method actually supported by the installed PEFT release. Do not substitute a generic `AdapterConfig` from a different adapter library.
- Match `TaskType` to the objective: sequence-classification labels are not causal-LM token targets. Inspect the architecture's module names rather than assuming every model has `q_proj`/`v_proj`.
- Choose rank, alpha/scaling variant, dropout, bias policy, and optional trainable task head from the task and budget. Treat example values as experiments, not universal settings.
- Use `get_peft_model` to wrap a supported base model. Inspect named trainable parameters and the fraction trained; do not assert a fixed parameter count.
- For QLoRA, use a supported quantization configuration and `prepare_model_for_kbit_training` before adapter injection. Match device placement to training strategy; inference `device_map="auto"` is not a distributed training recipe.

## Train and verify

1. Validate data formatting, padding, attention masks, and loss labels. Language-model training requires appropriate token labels/collation; an IMDb classification dataset does not become causal-LM training data simply by tokenizing its text.
2. Construct the optimizer after selecting trainable parameters. Clear gradients at the intended accumulation boundary, backpropagate, and step; do not silently accumulate forever.
3. Check finite loss and adapter gradients with a small batch. Confirm the intended base parameters remain frozen and any task-specific head is saved.
4. Evaluate held-out task quality and peak memory. Lower trainable-parameter count does not imply a fixed total VRAM requirement.

## Save, load, and switch

Save the adapter configuration/weights, tokenizer changes, base identifier and revision, and required extra modules. An adapter checkpoint alone is not a standalone full model or complete optimizer resume state.

Load on a compatible base, set trainability explicitly for resume versus inference, and verify active adapter names. Methods such as `add_adapter` can mutate the object in place: check the installed signature/return value rather than assigning its result to `model` blindly. Adding, loading, and activating an adapter are distinct operations.

Merge only when the method, quantization/backend, and delivery target support it and the requested output needs merged weights. Keep the original adapter; test merged/reloaded behavior rather than making merging a universal export prerequisite.

Consult [PEFT documentation](https://huggingface.co/docs/peft/) and [PeftModel reference](https://huggingface.co/docs/peft/package_reference/peft_model) for supported methods and exact signatures.
