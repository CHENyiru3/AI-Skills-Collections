# Library Review Checklist

## Structure

- `pyproject.toml` present and modern
- `src/` layout used where appropriate
- Public API exports are intentional
- `py.typed` included if typing is supported

## Quality

- Ruff and mypy configured
- Public functions typed
- Exceptions and error messages are coherent

## Testing

- Tests exist for public API
- Edge cases covered
- CI runs tests on pull requests

## Distribution

- Build succeeds
- Wheel metadata is sane
- Install path works in a clean environment

## Docs and Operations

- README covers installation and quick start
- Changelog exists
- License exists
- Security scanning or at least dependency auditing exists
