# Testing CI

Use CI to prove the package still works in a clean environment.

## Minimal GitHub Actions Workflow

```yaml
name: tests

on:
  push:
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.10", "3.11", "3.12"]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - run: python -m pip install -U pip
      - run: pip install -e ".[dev]"
      - run: pytest --cov=my_library
```

## CI Rules

- Keep unit tests fast enough to run on every pull request.
- Reserve slow integration suites for separate jobs or schedules.
- Fail the build when tests fail or coverage drops below the agreed threshold.
