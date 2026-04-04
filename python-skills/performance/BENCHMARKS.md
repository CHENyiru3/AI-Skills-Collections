# Benchmark Regression Testing

Use benchmarks to preserve performance after you already know which paths matter.

## Principles

- Benchmark stable, representative workloads.
- Separate performance tests from unit tests if runtime becomes high.
- Keep hardware and interpreter version as consistent as possible.

## pytest-benchmark Pattern

```python
def test_parse_benchmark(benchmark):
    benchmark(parse_payload, SAMPLE_INPUT)
```

## CI Guidance

- Run smoke benchmarks on pull requests only if they are stable.
- Run larger comparison suites on a schedule or dedicated runners.
- Treat big regressions as review blockers only when the benchmark is trusted.
