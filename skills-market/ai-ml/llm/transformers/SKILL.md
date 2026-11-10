---
name: transformers
domain: ai-ml
description: Implement or debug Hugging Face Transformers model/tokenizer loading, task heads, generation, feature extraction, or Trainer fine-tuning. Use in a Transformers codebase or when that library is requested.
license: Apache-2.0 license
metadata:
  version: "1.0.1"
  skill-author: Eric Yiru
---

# Transformers

Identify the task, model architecture, checkpoint/revision, tokenizer or processor, installed library version, hardware, and intended training or inference path. Preserve existing task and data contracts.

## Model and inputs

- Select the correct head: `AutoModel` exposes representations; sequence classification, causal LM, seq2seq LM, and masked LM use different task classes. Call generation on the model actually loaded for generation, not a previously defined encoder.
- Match tokenizer/processor and model revisions. Inspect padding side, special tokens, chat template, maximum context, and truncation policy. Resizing embeddings is required when adding vocabulary entries to a compatible model.
- Treat model-card claims and executable remote code separately. Use a known revision and inspect required custom code before enabling it; do not enable `trust_remote_code` merely to suppress an error.
- Place inputs according to the model's actual device dispatch. Avoid calling `.to(...)` on an already dispatched/offloaded model indiscriminately.

## Task-specific behavior

- Generation: distinguish prompt length from `max_new_tokens`; choose sampling or deterministic decoding deliberately. Use the model's chat template once and inspect actual tokenized input. Decoder-only batched generation needs a valid padding policy and attention mask. Explain whether outputs include the prompt.
- Classification: align label IDs, problem type, head dimension, and metric. A newly initialized classification head is not a trained predictor.
- Token tasks: align labels to subword tokens and mask ignored positions. For question answering, track overflow windows and offsets.
- Embeddings: use the pooling method the checkpoint was trained for. Exclude padding from mean pooling using the attention mask; neither an arbitrary CLS vector nor an unmasked mean is a universal sentence embedding.
- Long inputs: measure truncation or chunk explicitly. Do not claim the model processed omitted content.

## Fine-tuning and delivery

1. Inspect real examples and split membership before tokenization; keep subjects/documents/groups from leaking across evaluation boundaries.
2. Choose a collator and labels matching the loss. Causal-LM, seq2seq, and classification batches are not interchangeable; padding labels generally need an ignored-loss value rather than a vocabulary target.
3. Check installed `TrainingArguments` and `Trainer` signatures. Align evaluation and save schedules when selecting a best checkpoint. Do not turn on fp16 on unsupported hardware or add a second distributed wrapper around Trainer.
4. Run a small batch through forward/backward and inspect finite loss, shapes, masking, and trainable parameters. Evaluate on held-out task-relevant data.
5. Save model or adapters with tokenizer/processor, revision, label mapping, and generation/configuration details. Reload through the intended deployment path and distinguish weight-only loading from training resume.

Use [official Transformers documentation](https://huggingface.co/docs/transformers/) and the checkpoint's model card for version-specific loading, pipeline availability, Trainer parameters, and generation behavior. Avoid copying a catalog of unrelated models into the answer.
