---
name: bitsandbytes
domain: ai-ml
description: Configure or debug bitsandbytes 4-bit/8-bit model loading, quantization settings, supported hardware, and PEFT/QLoRA preparation. Use for an actual bitsandbytes integration rather than generic model optimization.
license: MIT license
metadata:
  version: "1.0.1"
  skill-author: Eric Yiru
---

# bitsandbytes quantization

Check the installed bitsandbytes, Transformers, Accelerate, PEFT, PyTorch, and hardware/backend compatibility together. Record model revision, intended inference/training use, precision, and memory budget.

## Select the quantization path

- For Transformers integration import `BitsAndBytesConfig` from `transformers`, not `bitsandbytes`.
- Choose one loading mode: `load_in_8bit=True` or `load_in_4bit=True`. For 4-bit loading, valid configuration includes `bnb_4bit_quant_type`, `bnb_4bit_compute_dtype`, and `bnb_4bit_use_double_quant`; do not invent `bnb_4bit_bits`.
- NF4 is commonly used for QLoRA; select compute dtype from supported hardware. Quantized storage, compute dtype, and non-quantized module dtype are separate choices.
- Use `device_map="auto"` for supported inference dispatch. Do not copy it into a distributed training recipe. Training placement must match the launcher and parallelism strategy.
- CPU offloading has its own dtype and memory cost. Check the actual device map and input embedding device instead of sending every input to a hardcoded CUDA device.

## Fine-tuning

For a supported quantized base, prepare it using PEFT's `prepare_model_for_kbit_training`, then apply an adapter configuration whose task type and target modules match the model. Inspect trainable parameters. In the usual 4-/8-bit Transformers fine-tuning path, train added parameters rather than assuming all quantized base weights are trainable. This workflow is not a generic quantization-aware-training implementation.

Check label masking, a finite loss, nonzero adapter gradients, and a small optimizer step before a long run. Preserve tokenizer, base revision, adapter configuration, and quantization metadata in the output.

## Verify the tradeoff

Measure peak memory, throughput, and task quality on a representative workload. Weight-storage estimates omit optimizer states, activations, KV cache, temporary buffers, and offloaded weights; do not promise model fit from parameter count alone. Quantization does not guarantee faster inference or identical outputs.

Test save/reload through APIs supported by the installed versions. Do not merge or dequantize adapters implicitly, and do not claim a quantized checkpoint is portable across unsupported backends.

Use the [official Transformers bitsandbytes guide](https://huggingface.co/docs/transformers/quantization/bitsandbytes) and [bitsandbytes documentation](https://huggingface.co/docs/bitsandbytes/) for supported parameters and hardware.
