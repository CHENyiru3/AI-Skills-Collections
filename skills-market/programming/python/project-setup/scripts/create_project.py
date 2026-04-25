#!/usr/bin/env python3
"""Scaffold a small Python library with modern defaults."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from textwrap import dedent


def slug_to_package(name: str) -> str:
    normalized = re.sub(r"[^a-zA-Z0-9]+", "_", name).strip("_").lower()
    if not normalized:
        raise ValueError("project name must contain at least one letter or number")
    return normalized


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def scaffold(project_root: Path, package_name: str, author: str) -> None:
    project_name = project_root.name

    write_file(
        project_root / "pyproject.toml",
        dedent(
            f"""
            [build-system]
            requires = ["setuptools>=69", "wheel"]
            build-backend = "setuptools.build_meta"

            [project]
            name = "{project_name}"
            version = "0.1.0"
            description = "Short project description."
            readme = "README.md"
            requires-python = ">=3.10"
            license = {{text = "MIT"}}
            authors = [{{name = "{author}"}}]
            dependencies = []

            [project.optional-dependencies]
            dev = [
                "mypy>=1.8",
                "pytest>=8.0",
                "ruff>=0.4",
            ]

            [tool.pytest.ini_options]
            testpaths = ["tests"]

            [tool.ruff]
            line-length = 88
            target-version = "py310"

            [tool.ruff.lint]
            select = ["E", "W", "F", "I", "B", "UP"]

            [tool.mypy]
            python_version = "3.10"
            disallow_untyped_defs = true
            warn_return_any = true

            [tool.setuptools.packages.find]
            where = ["src"]
            """
        ),
    )

    write_file(
        project_root / "README.md",
        dedent(
            f"""
            # {project_name}

            Short description of what `{project_name}` does.

            ## Installation

            ```bash
            pip install -e ".[dev]"
            ```

            ## Quick Start

            ```python
            from {package_name} import __version__

            print(__version__)
            ```
            """
        ),
    )

    write_file(project_root / "CHANGELOG.md", "# Changelog\n\n## [Unreleased]\n")
    write_file(project_root / "LICENSE", "MIT License\n")
    write_file(project_root / ".gitignore", ".venv/\n__pycache__/\n.pytest_cache/\n.mypy_cache/\ndist/\nbuild/\n")
    write_file(
        project_root / "Makefile",
        dedent(
            """
            .PHONY: lint format test typecheck

            lint:
            \truff check src tests

            format:
            \truff format src tests

            test:
            \tpytest

            typecheck:
            \tmypy src
            """
        ),
    )
    write_file(
        project_root / ".pre-commit-config.yaml",
        dedent(
            """
            repos:
              - repo: https://github.com/astral-sh/ruff-pre-commit
                rev: v0.4.8
                hooks:
                  - id: ruff
                  - id: ruff-format
            """
        ),
    )
    write_file(
        project_root / ".github/workflows/ci.yml",
        dedent(
            """
            name: ci

            on:
              push:
              pull_request:

            jobs:
              test:
                runs-on: ubuntu-latest
                steps:
                  - uses: actions/checkout@v4
                  - uses: actions/setup-python@v5
                    with:
                      python-version: "3.11"
                  - run: python -m pip install -U pip
                  - run: pip install -e ".[dev]"
                  - run: ruff check src tests
                  - run: ruff format --check src tests
                  - run: mypy src
                  - run: pytest
            """
        ),
    )
    write_file(project_root / "tests/test_smoke.py", f"from {package_name} import __version__\n\n\ndef test_version_present() -> None:\n    assert __version__\n")
    write_file(
        project_root / f"src/{package_name}/__init__.py",
        '__all__ = ["__version__"]\n__version__ = "0.1.0"\n',
    )
    write_file(project_root / f"src/{package_name}/py.typed", "")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("name", help="Project directory name, for example my-library")
    parser.add_argument("--author", default="Your Name", help="Author name for pyproject metadata")
    parser.add_argument(
        "--directory",
        default=".",
        help="Parent directory in which to create the project",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    project_root = Path(args.directory).resolve() / args.name
    package_name = slug_to_package(args.name)

    if project_root.exists():
        raise SystemExit(f"Refusing to overwrite existing path: {project_root}")

    scaffold(project_root, package_name, args.author)
    print(f"Created {project_root}")
    print("Next steps:")
    print(f"  cd {project_root}")
    print('  python -m pip install -e ".[dev]"')
    print("  pre-commit install")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
