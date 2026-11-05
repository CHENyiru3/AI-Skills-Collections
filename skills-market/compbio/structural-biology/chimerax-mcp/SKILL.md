---
name: chimerax-mcp
description: Install, configure, troubleshoot, and use dovas-net/chimeraX-mcp through MCP or CLI/API access. Use for ChimeraX molecular visualization, hydrogen bonds, salt bridges, van der Waals contacts, electrostatic surfaces, sessions, and requested figure export.
---

# ChimeraX MCP

Use the [dovas-net/chimeraX-mcp bridge](https://github.com/dovas-net/chimeraX-mcp) to operate a local UCSF ChimeraX application. The client launches a Python MCP server over STDIO; the server sends commands to ChimeraX over localhost HTTP. Installing this skill supplies instructions and a verification helper; the bridge and ChimeraX are separate installations.

**Use MCP tools or documented CLI/API access only. Do not use Computer Use, mouse/keyboard automation, or accessibility-tree control.** If a GUI has no REST endpoint, report the missing connection; use an isolated headless CLI process for calculations that do not require changing that GUI. Do not silently open a replacement window. An on-screen styling request does not imply export; honor an explicit no-export instruction for images, sessions, and reports.

## Setup and troubleshooting

For installation, configuration, missing tools, or connection failures, read [references/setup.md](references/setup.md). Use an existing working installation when the task only requires operating ChimeraX.

The setup reference covers Python selection, Codex configuration, existing-window attachment, and [scripts/smoke_test.py](scripts/smoke_test.py). That helper requires `--allow-export`: it starts a dedicated GUI session through the bridge and verifies PNG export. Use API/headless checks instead for no-export work.

## Choose the session

1. Discover the available tools and their current argument schemas. Use `list_chimerax_instances` and `check_chimerax_status` to identify responsive sessions.
2. Inspect the intended session with `list_models` or `get_session_info` before changing it. Use its returned model IDs and chain names in later calls.
3. Pass `session_id` explicitly when multiple instances exist or when working in a dedicated session. A session ID is the ChimeraX REST **port**, not a model ID or OS process ID.
4. If the intended GUI is open without REST, attach it as described in the setup reference. An automatic launch can otherwise create a different window.

For an independent task, `start_new_chimerax_session` creates a new instance. Read the actual port from its response; a busy requested port can be replaced with another port. After a startup timeout, inspect the running instances before retrying so a late launch does not produce duplicate windows.

After a connection failure, re-check the intended session before resuming changes. Unpatched bridge 0.4.0 can auto-launch or rediscover another instance even after an explicit-port failure; the bundled local fix makes explicit-port requests fail without redirection. An empty/different window is a reason to inspect session identity, not to reload the input or replay earlier commands automatically.

## Work on structures

- Prefer the specialized tools for opening structures, styling, selecting, measuring, and saving. Use `run_command` for commands that lack a suitable wrapper; consult `get_command_documentation` for the installed ChimeraX version.
- Use `get_atomspec_guide` when constructing unfamiliar selections. Model, chain, residue, and atom identifiers are distinct: for example, `#1/A:42@CA` selects the CA atom of residue 42 in chain A of model 1. Confirm that those identifiers exist in the target structure.
- Inspect tool responses for command errors even if the MCP call itself succeeds. Verify the resulting models or visibility after structural or display changes.
- Keep the original session or structure available when a requested edit needs comparison with the starting state. A new task does not imply permission to close unrelated models or windows.
- Report measurements with their returned units and selection identities. Distinguish operations on experimental coordinates from modeling or prediction results.

## Binding-interface interactions

When asked to analyze an interface, consider **hydrogen bonds, salt bridges, van der Waals contacts, and electrostatic interactions**. Distinguish their evidence and overlap rather than treating them as independent interaction counts or energies. A visualization-only request does not require running every analysis.

Read [references/interface-analysis.md](references/interface-analysis.md) for chain-restricted counting commands, the count-only MCP call, electrostatic coloring, and scientific interpretation limits. Use the current model IDs: after splitting the example complex, chain A was `#1.1/A` and chain B was `#1.2/B`; these are examples, not permanent identifiers.

For separate chain controls in the Models panel, use `split_model(..., by="chains")`, inspect the returned model list, and rename the resulting atomic models. Splitting can remove surfaces and leave a chain invisible. Restore the requested surface/cartoon and electrostatic coloring using the new IDs, then fit the complex in view. Keep the coordinates together unless spatial separation is requested.

Read [references/failure-lessons.md](references/failure-lessons.md) when recovering from missing models, split-display changes, or a transport failure. It records observed failures separately from inferred causes and links the portable local MCP fixes.

## Prepare views and requested exports

Set the requested representation, colors, camera, background, and image dimensions. Use `get_shown` to inspect visibility and clear selection highlights with `run_command("~select", session_id=...)` when they should not appear in the figure.

Export only when requested. Call `save_image` with an explicit output path, width, height, supersampling, and the intended session ID. Check that the file exists and visually inspect it before reporting completion. Save a `.cxs` session when the user requests an editable result. For view-only work, verify display state through the API; do not export a preview merely to inspect it.

## Capability boundaries

- The bridge exposes ChimeraX commands; it does not install prediction engines or grant access to external services. Boltz requires its own installation, Modeller requires a license key, and some prediction workflows involve remote or interactive services.
- The `core` profile reduces the number of tools but retains `run_command`; it is not a command-access restriction.
- Keep the REST bridge local. This repository supplies a local STDIO MCP server, not a hosted remote MCP endpoint.

## Sources

- [Bridge README and current installation instructions](https://github.com/dovas-net/chimeraX-mcp)
- [ChimeraX command documentation](https://www.cgl.ucsf.edu/chimerax/docs/user/commands/index.html)
- [Official OpenAI MCP configuration documentation](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)
