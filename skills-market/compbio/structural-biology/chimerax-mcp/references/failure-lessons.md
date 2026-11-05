# Failure review and local MCP improvements

Reviewed from the 2PQK installation and visualization session on 2026-11-05. This is a record of operational lessons, not a claim that interface interactions have all been measured.

| Evidence | Cause or uncertainty | Reusable response |
|---|---|---|
| The quick installer selected Python 3.9 despite an available Python 3.11. | `install.sh` invokes `python3`, not the newest installed interpreter. | Choose a verified Python 3.11+ executable and an isolated virtual environment. |
| Codex configuration existed, but this conversation exposed no ChimeraX MCP tools. | Configuration alone did not establish availability in the active tool catalog. | Discover tools first; use the installed STDIO bridge through its client API when necessary. |
| A running GUI did not answer on the checked REST ports. | A GUI window and a REST-enabled session are distinct. | Inspect available endpoints. Use MCP/CLI/API only; an isolated headless calculation is suitable for file-based measurements. Do not use Computer Use to attach the window. |
| UI actions repeatedly reported stale state; accessibility reads produced Qt invalid-object messages; screenshot capture intermittently failed with SCStreamError −3811. | GUI automation was unreliable in this session. These are not evidence of a CIF or molecular-model error. | Retire the GUI automation fallback. Do not retry accessibility/mouse/keyboard actions in this skill. |
| A later observation showed an empty window with different recent-file history after the complex had been visible. | The exact cause was not established: another instance, a reset, or user action could explain it. | Re-identify the session before mutation. Automatically reopening the CIF/replaying commands was not a reliable identity check. |
| After `split #1 chains`, chain A disappeared until its surface was regenerated; the camera framed only the visible peptide. | New atomic models and IDs replaced the original structure; derived surface/visibility state was not preserved. | Split before final styling when possible. Inspect actual new IDs, restore requested representations, reapply ESP coloring, then fit the complete complex. |
| Static review found explicit-port connection failure could enter the launch/recovery path and reuse another running session. | The default-port branch inside `start_chimerax` could discover an alternate even for an explicit request. This failure path was traced in code, not observed modifying a user's molecule. | The local patch makes a failed explicit target raise without launch or redirection; regression tests cover both default and non-default explicit ports. |
| One test failed because its fixed port 49200 was already in use. | Test-fixture collision, not application failure. | Bind a kernel-selected ephemeral port in the fixture. |

## Local MCP changes

The accompanying [patch](../assets/chimerax-mcp-0.4.0-local-fixes.patch) targets upstream commit `10cac22aec078ac1d07a3435a7a68358ce3c4cd5` (bridge 0.4.0). It changes:

- Full and core MCP initialization instructions: CLI/API-only operation, no-export scope, four interaction categories, session identity, and split recovery.
- `find_hbonds`: a second-selection restriction, salt-only analysis, sibling-submodel control, and count-only/detailed-log options. `inter_model=False` now explicitly excludes cross-model H-bonds instead of silently relying on the native default.
- `split_model`: return current model IDs after splitting and a recovery warning. A failed post-split inspection reports that the mutation already completed, so callers do not blindly repeat it.
- Explicit session failure: no alternate discovery or automatic launch. Implicit discovery/launch remains available when no port was specified.
- `set_scene`: use the documented native `graphics silhouettes` command. The legacy spelling was a compatibility concern identified from documentation; it was not recorded as a failed command in the live session.
- Focused regression tests for these behaviors and the ephemeral-port test fix.

To apply the authored patch to a matching checkout, first inspect it and run:

```bash
git apply --check /absolute/path/to/skill/assets/chimerax-mcp-0.4.0-local-fixes.patch
git apply /absolute/path/to/skill/assets/chimerax-mcp-0.4.0-local-fixes.patch
```

Do not apply it blindly to a newer or already-patched checkout. Reinstall the local package into its existing environment after code changes, verify an MCP initialization handshake, and start a new MCP connection to receive updated instructions and schemas. The patch is local feedback prepared for review; it has not been submitted to the upstream project.
