---
name: optimizing-python-performance
domain: programming
description: Profile and improve Python CPU, memory or throughput behavior using representative measurements. Use for an explicit performance investigation or optimization; not mandatory benchmarking for an unrelated edit.
metadata:
  version: "1.0.1"
---

# Python Performance Work

Define the workload, environment, measured problem and correctness contract.
Capture a representative baseline before changing code; distinguish startup,
I/O, compute, allocation and retained memory rather than guessing from syntax.
Profiling executes code, so select a suitable environment for unfamiliar inputs.

Choose the needed lens: CPU sampling/cProfile for hot paths, tracemalloc for Python
allocations, or a native-aware profiler when Python-only evidence is insufficient.
Read [PROFILING.md](PROFILING.md) for a relevant tool and verify its installed CLI.
Do not install a profiling stack globally as an automatic first step.

Compare like with like: inputs, warmup, caches, threads, device synchronization and
measurement units. Report repetitions/variability when they affect the conclusion.
Distinguish list indexing from value lookup; hash lookup is expected/amortized, not
a universal constant-time guarantee. Consider memory and ordering/duplicate semantics
before replacing a list with a set or caching a computation.

Optimize a measured bottleneck, then check that outputs, precision, side effects
and relevant resource bounds remain valid. Speed claims must name the workload
and baseline; do not extrapolate a microbenchmark to all users.

Read [BENCHMARKS.md](BENCHMARKS.md) for requested sustained regression tracking.
Adding a permanent benchmark suite or CI threshold is optional unless needed for
the agreed outcome. Stop when the requested measurement or improvement is verified,
and report remaining bottlenecks without expanding into unrelated tuning.
