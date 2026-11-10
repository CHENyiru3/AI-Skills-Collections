#!/usr/bin/env python3
"""Delegate to an installed ZotPilot CLI; installation requires --install.

Usage by AI agent (via SKILL.md):
    python scripts/run.py status --json
    python scripts/run.py setup --non-interactive --provider local
    python scripts/run.py index --limit 10
    python scripts/run.py register [--platform <name>] [--gemini-key <k>] ...

Windows note: use 'python' instead of 'python3' if python3 is not in PATH.
"""
from __future__ import annotations
import argparse
import shutil
import subprocess
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent  # repo root


def _uv_args(uv: str) -> list[str]:
    """Return uv invocation as a list (handles 'python -m uv' form)."""
    if uv.startswith(sys.executable):
        return [sys.executable, "-m", "uv"]
    return [uv]


def _ensure_uv() -> str:
    """Return path/invocation for uv, or exit with helpful message."""
    uv = shutil.which("uv")
    if uv:
        return uv
    # Fallback: uv installed via pip but not in PATH (common on Windows)
    try:
        subprocess.run(
            [sys.executable, "-m", "uv", "--version"],
            capture_output=True, check=True,
        )
        return f"{sys.executable} -m uv"  # sentinel for _uv_args()
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass
    print(
        "ERROR: uv is not installed.\n"
        "Install it:\n"
        "  Linux/macOS: curl -LsSf https://astral.sh/uv/install.sh | sh\n"
        "  Windows:     powershell -ExecutionPolicy ByPass -c "
        '"irm https://astral.sh/uv/install.ps1 | iex"\n'
        "  Any platform: pip install uv",
        file=sys.stderr,
    )
    sys.exit(1)


def _find_zotpilot_after_pip() -> list[str] | None:
    """Try to locate the zotpilot binary after a pip install.

    Returns a ready-to-use command list, or None if not found.
    """
    # PATH may have been updated by the install
    zp = shutil.which("zotpilot")
    if zp:
        return [zp]
    # Linux/macOS pip --user installs to ~/.local/bin/
    user_bin = Path.home() / ".local" / "bin" / "zotpilot"
    if user_bin.exists():
        return [str(user_bin)]
    # Windows pip --user installs to %APPDATA%\Python\PythonXYY\Scripts\
    import os as _os, platform as _plt
    if _plt.system() == "Windows":
        appdata = _os.environ.get("APPDATA", "")
        if appdata:
            py_ver = f"Python{sys.version_info.major}{sys.version_info.minor}"
            win_scripts = Path(appdata) / "Python" / py_ver / "Scripts"
            for name in ("zotpilot.exe", "zotpilot"):
                candidate = win_scripts / name
                if candidate.exists():
                    return [str(candidate)]
    return None


def _is_uv_tool_installed(uv: str) -> bool:
    """Check if zotpilot binary exists in uv's tool bin directory."""
    try:
        r = subprocess.run(
            _uv_args(uv) + ["tool", "dir", "--bin"],
            capture_output=True, text=True,
        )
        if r.returncode == 0 and r.stdout.strip():
            bin_dir = Path(r.stdout.strip())
            return (bin_dir / "zotpilot").exists() or (bin_dir / "zotpilot.exe").exists()
    except (FileNotFoundError, OSError):
        pass
    return False


def _ensure_zotpilot(uv: str) -> list[str] | None:
    """Install zotpilot CLI if needed.

    Returns an override command list when pip-installed (binary outside uv),
    or None when uv tool run should be used (the normal case).

    Resolution order:
    1. shutil.which() — binary on PATH
    2. _find_zotpilot_after_pip() — pip-installed binary (Windows %APPDATA%, ~/.local/bin)
    3. _is_uv_tool_installed() — uv's tool bin dir (not on PATH but uv tool run works)
    4. Fresh install via uv tool install
    5. pip fallback if uv fails
    Installation is called only with explicit --install; no automatic upgrade.
    """
    # 1. Check PATH
    if shutil.which("zotpilot"):
        return None

    # 2. Check pip-installed locations (binary outside uv)
    pip_cmd = _find_zotpilot_after_pip()
    if pip_cmd:
        return pip_cmd

    # 3. Check uv tool bin dir (installed but not on PATH — common on Windows)
    if _is_uv_tool_installed(uv):
        return None  # uv tool run still works

    # 4. Not installed anywhere — install now
    print("ZotPilot CLI not found. Installing...", file=sys.stderr)
    uv_cmd = _uv_args(uv)
    result = subprocess.run(
        uv_cmd + ["tool", "install", str(SKILL_DIR)],
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        print("ZotPilot CLI installed successfully.", file=sys.stderr)
        return None  # uv tool run works

    print(f"uv tool install failed; no pip fallback was attempted:\n{result.stderr}", file=sys.stderr)
    sys.exit(1)


def _handle_register(argv: list[str]) -> int:
    """Handle the 'register' subcommand for cross-platform MCP registration."""
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "platforms", Path(__file__).resolve().parent / "platforms.py"
    )
    if spec is None or spec.loader is None:
        print("ERROR: platforms.py not found in scripts/", file=sys.stderr)
        return 1
    platforms_mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(platforms_mod)
    register = platforms_mod.register
    PLATFORMS = platforms_mod.PLATFORMS

    parser = argparse.ArgumentParser(
        prog="run.py register",
        description="Register ZotPilot MCP server on AI agent platforms.",
    )
    parser.add_argument(
        "--platform", action="append", dest="platforms",
        required=True,
        choices=list(PLATFORMS.keys()),
        help="Explicit platform to register on (repeatable); no automatic multi-client writes.",
    )
    parser.add_argument("--gemini-key", help="Gemini API key for embeddings")
    parser.add_argument("--dashscope-key", help="DashScope API key for embeddings")
    parser.add_argument("--zotero-api-key", help="Zotero Web API key (for write ops)")
    parser.add_argument("--zotero-user-id", help="Zotero numeric user ID (for write ops)")
    args = parser.parse_args(argv)

    results = register(
        platforms=args.platforms,
        gemini_key=args.gemini_key,
        dashscope_key=args.dashscope_key,
        zotero_api_key=args.zotero_api_key,
        zotero_user_id=args.zotero_user_id,
    )
    return 0 if results and all(results.values()) else 1


def main():
    args = sys.argv[1:]
    install = bool(args and args[0] == "--install")
    if install:
        args = args[1:]
    if not args or args == ["--help"] or args == ["-h"]:
        print("Usage: run.py [--install] <zotpilot-command> [args]\nInstallation is opt-in; status/help never install or upgrade the CLI.\nRegistration requires register --platform <name>.")
        return

    # Intercept 'register' before uv check — register only edits JSON config files,
    # it does not need uv or the zotpilot CLI to be installed.
    if args and args[0] == "register":
        sys.exit(_handle_register(args[1:]))

    command = _find_zotpilot_after_pip()
    if command is None and not install:
        print("ZotPilot CLI is not on PATH or in a known user bin. No installation or upgrade was performed. Use an existing connector, configure PATH, or explicitly request --install.", file=sys.stderr)
        sys.exit(1)
    if command is None:
        uv = _ensure_uv()
        command = _ensure_zotpilot(uv)
        if command is None:
            result = subprocess.run(_uv_args(uv) + ["tool", "dir", "--bin"], capture_output=True, text=True, check=True)
            binary = Path(result.stdout.strip()) / ("zotpilot.exe" if sys.platform == "win32" else "zotpilot")
            command = [str(binary)]
    sys.exit(subprocess.run(command + args).returncode)


if __name__ == "__main__":
    main()
