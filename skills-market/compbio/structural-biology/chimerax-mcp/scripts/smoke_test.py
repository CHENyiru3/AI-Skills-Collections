#!/usr/bin/env python3
"""Verify the local ChimeraX MCP bridge with an offline molecule and PNG export.

Run with the Python environment that contains chimerax-mcp. A new dedicated GUI
session is started and left open; existing working sessions are not targeted.
"""

from __future__ import annotations

import argparse
import asyncio
from datetime import timedelta
import json
import os
from pathlib import Path
import re
import struct
import sys
import tempfile
from typing import Any


PDB = """HEADER    OFFLINE MCP INSTALLATION SMOKE TEST
ATOM      1  N   GLY A   1      -1.200   0.000   0.000  1.00 20.00           N
ATOM      2  CA  GLY A   1       0.000   0.000   0.000  1.00 20.00           C
ATOM      3  C   GLY A   1       1.250   0.850   0.000  1.00 20.00           C
ATOM      4  O   GLY A   1       2.250   0.350   0.000  1.00 20.00           O
TER
END
"""
REQUIRED_TOOLS = {
    "start_new_chimerax_session", "open_structure", "list_models",
    "run_command", "save_image",
}


def output_directory(requested: Path | None) -> Path:
    """Use a fresh directory so verification cannot overwrite user artifacts."""
    if requested is None:
        return Path(tempfile.mkdtemp(prefix="chimerax-mcp-smoke-"))
    output = requested.expanduser().resolve()
    output.mkdir(parents=True, exist_ok=True)
    if any(output.iterdir()):
        raise ValueError(f"Output directory must be empty: {output}")
    return output


async def verify(args: argparse.Namespace) -> None:
    try:
        from mcp import ClientSession, StdioServerParameters
        from mcp.client.stdio import stdio_client
    except ImportError as exc:
        raise RuntimeError("Run this helper with the bridge virtual environment's Python.") from exc

    output = output_directory(args.output)
    pdb_path, image_path = output / "smoke-glycine.pdb", output / "smoke-glycine.png"
    pdb_path.write_text(PDB, encoding="ascii")
    transcript: list[dict[str, Any]] = []
    print(f"Output: {output}", flush=True)

    async def call(session: Any, name: str, arguments: dict[str, Any]) -> str:
        result = await session.call_tool(name, arguments=arguments)
        content = "\n".join(item.text for item in result.content if item.type == "text")
        transcript.append({"tool": name, "arguments": arguments,
                           "isError": result.isError, "content": content})
        (output / "transcript.json").write_text(json.dumps(transcript, indent=2) + "\n")
        print(f"{name}: {content}", flush=True)
        if result.isError:
            raise RuntimeError(f"{name} failed: {content}")
        return content

    environment = {name: os.environ[name] for name in (
        "CHIMERAX_PATH", "CHIMERAX_PORT", "CHIMERAX_TIMEOUT", "CHIMERAX_DEBUG",
    ) if name in os.environ}
    if args.chimerax:
        environment["CHIMERAX_PATH"] = str(args.chimerax.expanduser().resolve())
    bridge_default = int(environment.get("CHIMERAX_PORT", "8080"))
    if args.port == bridge_default:
        raise ValueError("Choose a test --port different from the bridge default port.")
    parameters = StdioServerParameters(
        command=sys.executable,
        args=["-m", "chimerax_mcp", "serve", "--profile", args.profile],
        env=environment,
    )
    async with stdio_client(parameters) as (read, write):
        async with ClientSession(
            read, write, read_timeout_seconds=timedelta(seconds=args.timeout),
        ) as session:
            initialized = await session.initialize()
            print(f"Initialized {initialized.serverInfo.name}", flush=True)
            tools, cursor = [], None
            while True:
                page = await session.list_tools(cursor=cursor)
                tools.extend(page.tools)
                cursor = page.nextCursor
                if not cursor:
                    break
            (output / "tools.json").write_text(json.dumps(
                [tool.model_dump(mode="json") for tool in tools], indent=2,
            ) + "\n")
            missing = REQUIRED_TOOLS - {tool.name for tool in tools}
            if missing:
                raise RuntimeError(f"Required tools missing: {', '.join(sorted(missing))}")
            print(f"Listed {len(tools)} tools ({args.profile} profile)", flush=True)

            started = await call(session, "start_new_chimerax_session", {
                "session_name": "MCP installation smoke test", "port": args.port,
            })
            match = re.search(r"started successfully.*? on port (\d+)\.", started)
            if not match:
                raise RuntimeError("Dedicated session startup failed; inspect ChimeraX before retrying.")
            port = int(match.group(1))
            if port == bridge_default:
                raise RuntimeError(
                    "The new session uses the bridge default port; stop before modifying models. "
                    "Choose a different --port to prevent default-session recovery from "
                    "redirecting a later command to a working window."
                )
            await call(session, "open_structure", {
                "identifier": str(pdb_path), "format": "pdb", "session_id": port,
            })
            models = await call(session, "list_models", {"session_id": port})
            if "Models loaded: 1" not in models or "4 atoms" not in models:
                raise RuntimeError(f"Unexpected offline test model: {models}")
            await call(session, "run_command", {
                "command": "style #1 sphere; view #1; set bgColor white",
                "session_id": port,
            })
            await call(session, "save_image", {
                "filename": str(image_path), "width": 800, "height": 600,
                "supersample": 1, "session_id": port,
            })
            png = image_path.read_bytes()
            if len(png) < 24 or png[:8] != b"\x89PNG\r\n\x1a\n":
                raise RuntimeError("Export is not a PNG image.")
            if struct.unpack(">II", png[16:24]) != (800, 600):
                raise RuntimeError("Export has unexpected image dimensions.")
            summary = {"passed": True, "profile": args.profile,
                       "tool_count": len(tools), "session_id": port,
                       "image": str(image_path), "output": str(output)}
            (output / "result.json").write_text(json.dumps(summary, indent=2) + "\n")
            print(f"PASS: offline molecule and 800x600 PNG; GUI port {port} remains open.", flush=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--chimerax", type=Path, help="ChimeraX executable; otherwise use bridge discovery")
    parser.add_argument("--output", type=Path, help="New or empty output directory; default: fresh temp directory")
    parser.add_argument("--port", type=int, default=58180, help="Preferred non-default port for a NEW session (default: 58180)")
    parser.add_argument("--profile", choices=("full", "core"), default="full")
    parser.add_argument("--timeout", type=float, default=90, help="Per-request timeout in seconds (default: 90)")
    args = parser.parse_args()
    if not 1 <= args.port <= 65535:
        parser.error("--port must be between 1 and 65535")
    if args.timeout <= 0:
        parser.error("--timeout must be positive")
    try:
        asyncio.run(verify(args))
    except (RuntimeError, ValueError, OSError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
