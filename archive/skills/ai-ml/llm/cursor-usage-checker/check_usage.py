#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def resolve_shared_script() -> Path:
    here = Path(__file__).resolve()
    candidates = [
        here.parents[1] / "utility" / "provider-usage-checker" / "scripts" / "check_usage.py",
        here.parents[2] / "utility" / "provider-usage-checker" / "scripts" / "check_usage.py",
        here.parents[1] / "provider-usage-checker" / "scripts" / "check_usage.py",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    raise FileNotFoundError("Shared provider usage checker not found.")


def main() -> int:
    shared_script = resolve_shared_script()
    result = subprocess.run(
        [sys.executable, str(shared_script), "--provider", "cursor", *sys.argv[1:]],
        check=False,
    )
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
