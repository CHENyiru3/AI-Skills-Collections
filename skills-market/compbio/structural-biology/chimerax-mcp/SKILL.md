---
name: chimerax-mcp
description: Install, configure, troubleshoot, and use dovas-net/chimeraX-mcp to control local UCSF ChimeraX from Codex or another local MCP client. Use for ChimeraX MCP setup, molecular visualization, structural measurements, sessions, and figure export.
---

# ChimeraX MCP

Use the [dovas-net/chimeraX-mcp bridge](https://github.com/dovas-net/chimeraX-mcp) to operate a local UCSF ChimeraX application. The client launches a Python MCP server over STDIO; the server sends commands to ChimeraX over localhost HTTP. Installing this skill supplies instructions and a verification helper; the bridge and ChimeraX are separate installations.

## Setup and troubleshooting

For installation, configuration, missing tools, or connection failures, read [references/setup.md](references/setup.md). Use an existing working installation when the task only requires operating ChimeraX.

The setup reference covers Python selection, Codex configuration, existing-window attachment, and [scripts/smoke_test.py](scripts/smoke_test.py). The helper starts a dedicated GUI session, opens an offline test molecule, and verifies PNG export without targeting the user's working session.

## Choose the session

1. Discover the available tools and their current argument schemas. Use `list_chimerax_instances` and `check_chimerax_status` to identify responsive sessions.
2. Inspect the intended session with `list_models` or `get_session_info` before changing it. Use its returned model IDs and chain names in later calls.
3. Pass `session_id` explicitly when multiple instances exist or when working in a dedicated session. A session ID is the ChimeraX REST **port**, not a model ID or OS process ID.
4. If the intended GUI is open without REST, attach it as described in the setup reference. An automatic launch can otherwise create a different window.

For an independent task, `start_new_chimerax_session` creates a new instance. Read the actual port from its response; a busy requested port can be replaced with another port. After a startup timeout, inspect the running instances before retrying so a late launch does not produce duplicate windows.

After a connection failure, re-check the intended session before resuming changes. Bridge recovery can launch a new instance or, when targeting its default port, rediscover another running instance.

## Work on structures

- Prefer the specialized tools for opening structures, styling, selecting, measuring, and saving. Use `run_command` for commands that lack a suitable wrapper; consult `get_command_documentation` for the installed ChimeraX version.
- Use `get_atomspec_guide` when constructing unfamiliar selections. Model, chain, residue, and atom identifiers are distinct: for example, `#1/A:42@CA` selects the CA atom of residue 42 in chain A of model 1. Confirm that those identifiers exist in the target structure.
- Inspect tool responses for command errors even if the MCP call itself succeeds. Verify the resulting models or visibility after structural or display changes.
- Keep the original session or structure available when a requested edit needs comparison with the starting state. A new task does not imply permission to close unrelated models or windows.
- Report measurements with their returned units and selection identities. Distinguish operations on experimental coordinates from modeling or prediction results.

## Export figures

Set the requested representation, colors, camera, background, and image dimensions. Use `get_shown` to inspect visibility and clear selection highlights with `run_command("~select", session_id=...)` when they should not appear in the figure.

Call `save_image` with an explicit output path, width, height, supersampling, and the intended session ID. Check that the file exists and visually inspect it before reporting completion. Save a `.cxs` session as well when the user requests an editable result.

## Capability boundaries

- The bridge exposes ChimeraX commands; it does not install prediction engines or grant access to external services. Boltz requires its own installation, Modeller requires a license key, and some prediction workflows involve remote or interactive services.
- The `core` profile reduces the number of tools but retains `run_command`; it is not a command-access restriction.
- Keep the REST bridge local. This repository supplies a local STDIO MCP server, not a hosted remote MCP endpoint.

## Sources

- [Bridge README and current installation instructions](https://github.com/dovas-net/chimeraX-mcp)
- [ChimeraX command documentation](https://www.cgl.ucsf.edu/chimerax/docs/user/commands/index.html)
- [Official OpenAI MCP configuration documentation](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)
