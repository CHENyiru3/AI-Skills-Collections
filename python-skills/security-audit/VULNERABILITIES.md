# Vulnerability Patterns

## Injection

- Use parameterized SQL queries.
- Avoid `shell=True` unless there is no alternative and inputs are fully controlled.
- Validate filenames, paths, and untrusted user input before use.

## Deserialization

- Do not load untrusted pickle data.
- Prefer JSON or explicit schema validation for external payloads.

## Secrets

- Never commit tokens or passwords.
- Use environment variables or secret stores.
- Scan history as well as current files if a leak is suspected.

## Temporary Files and Permissions

- Use secure temp file APIs from the standard library.
- Avoid writing secrets to world-readable paths.

## Dependency Risk

- Remove unused packages.
- Review transitive dependencies for abandoned or risky projects.
