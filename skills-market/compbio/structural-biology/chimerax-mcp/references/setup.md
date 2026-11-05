# Local ChimeraX MCP setup

## Prerequisites

- UCSF ChimeraX installed on the computer that runs the MCP server, with a working desktop session for GUI rendering.
- Python 3.11 or newer. Check the chosen executable's version: a Mac can have a suitable `python3.11` while `python3` still points to Apple's Python 3.9.
- A local MCP client such as Codex, Claude Code, Claude Desktop, or Cursor. A hosted remote connector cannot directly launch this local command.

The workflow below was verified on macOS arm64 with ChimeraX 1.12, Python 3.11, bridge 0.4.0 (upstream commit `10cac22aec078ac1d07a3435a7a68358ce3c4cd5`), and MCP SDK 1.30.0. It is a verification baseline, not a requirement to downgrade newer installations. Inspect current upstream packaging when updating; bridge 0.4.0 requires `mcp[cli]>=1.2.0,<2`.

## Install the bridge

Choose a persistent install directory outside the skill collection. Check for an existing clone or environment before creating a second installation. These POSIX commands use Python 3.11 explicitly; substitute another verified Python 3.11+ executable when appropriate:

```bash
git clone https://github.com/dovas-net/chimeraX-mcp.git "${HOME}/.local/share/chimerax-mcp"
cd "${HOME}/.local/share/chimerax-mcp"
python3.11 -m venv .venv
.venv/bin/python -m pip install .
.venv/bin/python -m pip check
.venv/bin/chimerax-mcp print-config codex
```

The upstream `install.sh` uses `python3` specifically. Use the manual path when that executable is too old. There is no need to change the system-wide Python default.

On Windows, use Python 3.11+ with `.venv\Scripts\python.exe` and `.venv\Scripts\chimerax-mcp.exe`; the Bash installer does not run in PowerShell. The macOS workflow above is the tested baseline.

## Register with Codex

Inspect and back up the existing `~/.codex/config.toml`, retaining its permissions. Review any existing `chimerax` entry before changing it: the setup helper replaces that server's section, including custom options in that section. Preserve unrelated settings and server entries.

From the bridge directory:

```bash
.venv/bin/chimerax-mcp setup codex
.venv/bin/chimerax-mcp doctor
codex mcp get chimerax --json
```

The resulting entry uses the absolute path to the **bridge virtual environment's Python**, rather than a shell activation command. For example, replace `/absolute/install/path` with the real directory before using this configuration:

```toml
[mcp_servers.chimerax]
command = "/absolute/install/path/.venv/bin/python"
args = ["-m", "chimerax_mcp", "serve"]
enabled = true
tool_timeout_sec = 600
```

Codex's default per-tool timeout is shorter than the upstream recommendation for long-running tools. The setup helper supplies 600 seconds. The bridge also has its own command timeouts; increasing the client timeout does not provision prediction services or guarantee completion of arbitrary jobs.

The desktop app, CLI, and IDE extension on the same Codex host share MCP configuration. Fully quit and reopen the desktop app, start a new CLI session, or restart the IDE extension to load the changed configuration. Do not close the user's active client automatically.

For another supported local client, use `print-config CLIENT` followed by `setup CLIENT`; check upstream for that client's name and config destination. This skill does not contain a hosted remote service.

## Executable discovery and options

On macOS, discovery includes versioned `/Applications/ChimeraX*.app` and `~/Applications/ChimeraX*.app` installations. For an unusual installation or to select a particular version, configure the executable explicitly:

```toml
[mcp_servers.chimerax.env]
CHIMERAX_PATH = "/Applications/ChimeraX-1.12.app/Contents/MacOS/ChimeraX"
```

The path must name the executable, not the `.app` directory. Update it if that version is removed. Other bridge environment variables are `CHIMERAX_PORT` (default `8080`), `CHIMERAX_TIMEOUT` (default `60` seconds), and `CHIMERAX_DEBUG`.

For the lighter profile, use `args = ["-m", "chimerax_mcp", "serve", "--profile", "core"]`. Bridge 0.4.0 exposes 119 full-profile tools and 45 core-profile tools; discover the current catalog instead of assuming these counts for future versions.

## Attach an existing ChimeraX window

If no REST server is available in the intended window, ask the **user** to enter this command there once, or use a documented existing CLI/API attachment facility. Do not use Computer Use or keyboard/mouse automation to enter it:

```text
remotecontrol rest start port 8080 json true log true
```

Use the resulting port as the MCP tools' `session_id`. Existing GUI windows without REST are not usable by the bridge; an ordinary tool call may auto-launch a separate instance instead. A failed REST discovery does not mean the GUI is absent.

Discovery scans common ports and ports known to the current bridge process; it is not an exhaustive search. For a custom port, pass `session_id` explicitly, or configure `CHIMERAX_PORT` for a preferred default. An in-memory session name or default selection may be lost when the MCP process restarts.

## Verify the complete connection

`doctor` checks executable discovery and REST reachability. In bridge 0.4.0, finding the executable alone can produce exit code zero; it does not prove a tool can open a model or export an image.

For API-only verification, initialize the STDIO MCP server, list tools, check the intended session status and inspect its models. An isolated headless CLI calculation is another option; see [interface-analysis.md](interface-analysis.md#headless-cli-calculation). Neither requires an exported image or GUI automation.

The bundled GUI/rendering helper is **opt-in installation verification**: it launches a dedicated application instance through the bridge and exports a PNG. Do not use it for no-export or view-only tasks. When rendering/export verification is authorized, run it with the bridge environment's Python and the explicit `--allow-export` flag. Replace `/absolute/path/to/skill` with the installed skill directory:

```bash
.venv/bin/python /absolute/path/to/skill/scripts/smoke_test.py --help
.venv/bin/python /absolute/path/to/skill/scripts/smoke_test.py --allow-export
```

The helper initializes the actual STDIO server, checks the required tool names, creates a **new** ChimeraX session, opens a generated four-atom glycine PDB, lists its model, and exports an 800 × 600 PNG. It prints the actual port and output directory, records the tool catalog and transcript, and leaves its dedicated test window open for inspection. Read the PNG to verify the rendered content. Test files go to a fresh temporary directory by default. `--output` accepts a new or empty directory; `--chimerax` selects a specific executable.

The preferred test port is `58180`. The helper rejects a test port equal to the bridge default (`CHIMERAX_PORT`, normally `8080`), including a replacement port returned at launch. In bridge 0.4.0, recovery from a failed connection to the default port can select another existing session; a separate test port avoids that recovery path.

If launch times out, inspect the GUI and recorded responses before retrying. A delayed startup can otherwise leave multiple test windows. Network or sandbox restrictions can prevent localhost access or desktop launching; distinguish that from a missing Python dependency.

## Advanced features

Installing the MCP bridge does not install every engine called by its tools:

- [Boltz](https://www.cgl.ucsf.edu/chimerax/docs/user/commands/boltz.html) has a separate installation and model-weight download.
- [Modeller](https://www.cgl.ucsf.edu/chimerax/docs/user/commands/modeller.html) requires a license key and an appropriate service or local installation.
- [AlphaFold](https://www.cgl.ucsf.edu/chimerax/docs/user/commands/alphafold.html) prediction can involve an interactive external workflow.

Check the installed ChimeraX command documentation and the actual response before claiming an advanced workflow is available or complete.

## Authoritative references

- [Upstream bridge source and README](https://github.com/dovas-net/chimeraX-mcp)
- [Upstream client configuration writer](https://github.com/dovas-net/chimeraX-mcp/blob/main/src/chimerax_mcp/client_setup.py)
- [Official OpenAI documentation: MCP](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)
- [ChimeraX REST server command](https://www.cgl.ucsf.edu/chimerax/docs/user/commands/remotecontrol.html)
