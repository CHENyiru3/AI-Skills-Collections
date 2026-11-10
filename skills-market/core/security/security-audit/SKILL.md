---
name: auditing-python-security
domain: core
description: Audit Python source, dependency vulnerabilities or secret exposure, or implement requested security checks. Use for an explicit Python security review or hardening task; ordinary code edits do not require a full audit.
metadata:
  version: "1.0.1"
---

# Python Security Audit

Establish the source/dependency scope and whether the request is inspection,
remediation or CI integration. Start with static evidence; executing unfamiliar
project code and installing dependencies require an appropriate isolated context.
Do not turn a read-only audit into dependency upgrades or CI changes.

## Collect and interpret evidence

Use existing tooling where available. For example:

```bash
bandit -r src/ -ll      # medium severity and above; -lll means high only
pip-audit -r requirements.txt
```

A tool finding is a lead, not proof of exploitability. Record location, affected
version, input/control flow and practical impact. Distinguish false positives,
unavailable checks and accepted risks. Redact secrets rather than reproducing
values in output; an exposed credential needs revocation/rotation, not just deletion.

Keep these distinctions explicit:

- B608 concerns SQL query construction; bind values instead of interpolating them.
- B602 flags shell use; assess input control and shell semantics before proposing
  an argv replacement. An argv list still needs care with option injection.
- B108 concerns hardcoded temporary paths, not path traversal. For traversal,
  resolve the candidate relative to the allowed root and check containment;
  consider symlink/race behavior if the filesystem can change concurrently.
- Untrusted pickle/YAML deserialization can execute code. Select a non-executing
  format/loader appropriate to the actual data contract.
- Password hashing, encryption and non-security checksums have different needs;
  do not replace password hashing with a fast SHA digest.

Use [VULNERABILITIES.md](VULNERABILITIES.md) for a relevant vulnerability pattern,
checking its examples against the current API and threat model. These are examples,
not a universal checklist.

## Remediate only within the requested scope

Separate an advisory dependency finding from a package change. Inspect proposed
updates and compatibility before using automated fixes such as `pip-audit --fix`;
verify the affected path or dependency lock afterwards. Avoid blanket exclusions
that suppress production findings just to obtain a clean scan.

For requested CI integration, consult [CI_SECURITY.md](CI_SECURITY.md) and adapt
paths, dependency setup and permissions to the repository. Scan cadence and a
particular tool stack are recommendations, not audit completion conditions.

Deliver scoped findings, evidence, fixes made and relevant verification. Stop
when the requested assessment or repair is complete; do not require zero findings,
new infrastructure or a weekly scanning rollout for an inspection request.

CLI references: [Bandit](https://bandit.readthedocs.io/en/latest/man/bandit.html),
[B108](https://bandit.readthedocs.io/en/latest/plugins/b108_hardcoded_tmp_directory.html).
