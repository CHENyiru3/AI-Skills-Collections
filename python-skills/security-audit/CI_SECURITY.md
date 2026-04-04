# CI Security Workflow

```yaml
name: security

on:
  pull_request:
  schedule:
    - cron: "0 6 * * 1"

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: python -m pip install -U pip
      - run: pip install bandit pip-audit detect-secrets
      - run: bandit -r src -ll
      - run: pip-audit
      - run: detect-secrets scan --all-files
```

## Notes

- Keep scheduled dependency scanning separate from fast pull request checks if runtime is high.
- Fail pull requests on high-confidence security findings, not noisy style-only issues.
