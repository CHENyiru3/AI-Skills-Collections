---
name: testing-python-libraries
domain: programming
description: Design or repair meaningful pytest tests for a Python package, including fixtures, parametrization or property checks. Use for a requested test strategy or regression case; not mandatory coverage infrastructure for every reversible edit.
metadata:
  version: "1.0.1"
---

# Python Testing Strategy

Identify the observable contract and the failure the test should distinguish.
Use the repository's existing test runner/configuration and supported environments.
Prefer a focused regression over assertions that mirror implementation details or
merely match generated wording.

- Cover consequential valid, boundary and failure behavior, selecting cases from
  actual risks rather than a universal public-API/coverage checklist.
- Use temporary paths and isolated state; create valid input fixtures explicitly.
  Restore environment, working directories and patched dependencies after a test.
- Mock at the boundary where a dependency is looked up. The `mocker` fixture needs
  pytest-mock; use existing tooling or pytest's monkeypatch instead of assuming it.
- Keep unit tests independent of live credentials/services. Add an integration
  test only when its environment and side effects are intentional and controlled.
- For randomized/property tests, state the invariant and relevant domain; preserve
  failing examples/seeds. Avoid arbitrary output snapshots that conceal semantics.

Read [FIXTURES.md](FIXTURES.md) for complex fixture scopes,
[HYPOTHESIS.md](HYPOTHESIS.md) for property testing, and [CI.md](CI.md) only for
requested CI work. Verify current plugin APIs before copying examples.

Run the smallest test set that can detect the changed behavior; broaden on a real
failure or unresolved dependency concern. Coverage reports reveal unexercised code,
not correctness, and 85 percent or sub-100ms limits are not universal acceptance
criteria. Report what ran, failed or was unavailable, then stop when the requested
behavior has relevant evidence.
