---
name: reviewing-python-libraries
domain: programming
description: Assess a Python package for adoption, maintenance or release readiness and report evidence-backed engineering risks. Use for a requested library audit; not a demand to run arbitrary tests or redesign a package during inspection.
metadata:
  version: "1.0.1"
---

# Python Library Review

Establish the package revision, intended use and requested review depth. Inspect
metadata, source, tests, CI and existing result artifacts before running code.
Dependency installation, test collection and build hooks can execute repository
code; use an appropriate isolated environment for unfamiliar sources and do not
assume an audit authorizes global installation.

Prioritize findings that affect the user's intended use:

- Packaging/importability and declared Python/dependency compatibility.
- Evidence that tests cover consequential behavior, with limits of available
  coverage reports; a fixed percentage alone is not a quality verdict.
- Public API stability, exception/data contracts and migration support.
- Vulnerabilities or secret exposure with a specific affected path/version.
- Documentation and license evidence needed for the intended adoption.
- Maintenance/release history as context, not proof that an old stable library is
  defective or a frequently changed one is dependable.

Distinguish confirmed defects, plausible risks and missing evidence. Do not treat
src layout, strict types, py.typed, a particular build backend or CI platform as
universal requirements. Avoid contradictory 70/80/85 percent gates and star scores
that hide the evidence.

Use [CHECKLIST.md](CHECKLIST.md) as optional review lenses and
[REPORT_TEMPLATE.md](REPORT_TEMPLATE.md) as a report aid, adapting both to scope.
Do not inherit their thresholds as acceptance policy. Report location/evidence,
practical effect and a proportionate recommendation for each material finding.

If execution is useful, run the smallest relevant checks and label what was not
tested. Stop when the scoped assessment and unresolved gaps are clear; remediation,
new CI and dependency updates are separate requested work.
