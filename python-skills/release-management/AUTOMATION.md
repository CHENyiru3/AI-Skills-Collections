# Release Automation

Release automation should reduce mistakes, not hide the release process.

## Good Workflow

1. Merge the release-ready changes.
2. Update version and changelog.
3. Build and test artifacts in CI.
4. Tag the commit.
5. Publish to GitHub Releases and PyPI from CI.

## Version Bump Script Rules

- Accept the new version explicitly unless your project already has strong conventions.
- Update a single source of truth when possible.
- Fail fast if the working tree is dirty or tests fail.

## Safety Checks

- Verify the tag matches the package version.
- Run `python -m build` and `twine check`.
- Publish from CI rather than a maintainer laptop where possible.
