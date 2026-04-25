# API Evolution

Use this file when changing a public Python API without surprising downstream users.

## Deprecation Sequence

1. Introduce the replacement API.
2. Emit a `DeprecationWarning` from the old API.
3. Document the migration path in the changelog and docs.
4. Keep the warning in at least one minor release before removal unless there is a security or correctness reason.
5. Remove in the next planned breaking release.

## Warning Template

```python
warnings.warn(
    "`old_name()` is deprecated; use `new_name()` instead.",
    DeprecationWarning,
    stacklevel=2,
)
```

## Migration Notes

- Show before and after examples.
- State whether behavior changed or only names changed.
- Mention fallback compatibility shims if they exist.
- Call out data migrations or config changes explicitly.

## Versioning Rules

- Bug fix with compatible behavior: patch.
- New API without breakage: minor.
- Removed or incompatible behavior: major.
