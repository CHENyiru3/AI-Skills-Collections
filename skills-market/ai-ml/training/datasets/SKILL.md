---
name: datasets
domain: ai-ml
description: Load, transform, split, stream, cache, or export data with Hugging Face Datasets. Use for Dataset/DatasetDict/IterableDataset workflows and their schema, batching, or reproducibility issues.
license: Apache-2.0 license
metadata:
  version: "1.0.1"
  skill-author: Eric Yiru
---

# Hugging Face Datasets

Inspect source files or Hub dataset/config/revision, real columns/features, row unit, split policy, size, and installed Datasets version before selecting an operation.

## Load the intended object

`load_dataset(..., split="train")` returns a split dataset; omitting `split` commonly returns a `DatasetDict`. Streaming returns iterable variants. Inspect the object type before indexing with a split name or using random-access methods.

```python
from datasets import Dataset

rows = Dataset.from_dict({"text": ["a", "b"], "label": [0, 1]})
upper = rows.map(lambda batch: {"text": [s.upper() for s in batch["text"]]},
                 batched=True)
assert upper[0]["text"] == "A"
```

Use explicit `data_files`, configuration, split, and revision where relevant. Preserve stable identifiers and feature types; do not assume downloaded label names or row counts match a tutorial.

## Transform and split

- Design the evaluation boundary before shuffling. Split by the required subject, document, conversation, source, or time unit; random row splitting can leak related records. Persist split membership and seed when randomized.
- `Dataset.train_test_split` applies to a split dataset, not an entire dictionary blindly. Stratification has feature/type constraints; check them instead of assuming any label column is accepted.
- For batched `map`, return equal-length columns. If a transform changes row count, remove or replace incompatible original columns. Preserve provenance through tokenization/chunking and inspect nulls, types, and sample rows.
- Select needed columns before passing to a framework. Choose a collator matching dynamic padding and the task's label shape; do not feed a raw string/metadata column into the model accidentally.
- Parallel processing can change memory use and ordering assumptions. Benchmark on a subset and keep nondeterministic transforms or external dependencies explicit.

## Large data and persistence

Memory-mapped datasets, in-memory objects, and streaming iterables have different access/shuffle/persistence semantics. Streaming avoids eagerly materializing the entire dataset but is not a blanket guarantee of zero local cache or network traffic. Bound buffers, downloads, and worker sharding for the actual source.

Do not call random-access selection, `num_proc`, length-dependent code, or save methods on an iterable without checking support. Verify iteration/restart and distributed sharding if training depends on them.

Use `save_to_disk`/`load_from_disk` for supported dataset persistence or explicit CSV/JSON/Parquet export as required. Record revision, schema, transformations, fingerprints/configuration, and split IDs. Inspect row counts and schema after reload, especially where an export format loses feature metadata.

Use [official Datasets documentation](https://huggingface.co/docs/datasets/) for version-specific loading, streaming, caching, and feature APIs. Validate only the transformations and downstream batch contract relevant to the task.
