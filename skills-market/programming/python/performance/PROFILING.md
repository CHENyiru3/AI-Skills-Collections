# Profiling Guide

Profile before you optimize. The goal is to find the real bottleneck, not the most suspicious-looking code.

## Recommended Order

1. Reproduce the slow path.
2. Measure baseline runtime and memory.
3. Use a profiler to locate hotspots.
4. Change one thing at a time.
5. Re-measure and keep the simpler version if gains are negligible.

## Tool Choice

- `pyinstrument`: best first pass for wall-clock hotspots.
- `cProfile`: useful for detailed call counts.
- `tracemalloc`: built-in memory allocation tracing.
- `memray`: deeper memory analysis for hard cases.

## Common Mistakes

- Benchmarking debug builds or cold-start paths only.
- Comparing numbers from different environments.
- Optimizing microseconds in code dominated by network or disk latency.
