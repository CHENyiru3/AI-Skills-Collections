# Conda Packaging Guide

Most Python libraries should publish to PyPI first. Add Conda packaging only if your users actually install with Conda.

## When Conda Helps

- Scientific users already rely on Conda environments.
- Native dependencies make wheel distribution harder.
- The package is commonly used in Jupyter or research workflows.

## Practical Recommendation

- Prefer `conda-forge` over maintaining a private recipe unless there is a strong reason not to.
- Keep PyPI metadata clean first; Conda recipes are easier once packaging is already correct.
- Document whether Conda is official or community-maintained.
