# ZotPilot troubleshooting

Diagnose the failing layer before changing configuration. Discover the actual
connected tool/CLI version; examples in older tool guides may use different names.

| Symptom | Targeted response |
| --- | --- |
| CLI unavailable | Use an existing connector or configure PATH; install only when requested with wrapper `--install`. |
| Missing configuration/library | Inspect setup help and the selected Zotero library/data path; preserve other profiles. |
| Empty search | Check query, collection/library scope and indexing coverage; do not equate an empty index with an empty Zotero library. |
| Provider credential/rate failure | Check actual error and provider settings; respect retry guidance, avoid exposing keys or switching providers without authorization. |
| Local model missing | A first download can require network access; an installed local model can then run without a cloud embedding API. |
| Read succeeds but write fails | Check API permission/library identity and network reachability separately; do not rotate credentials solely because DNS failed. |
| Newly registered tools unavailable | Reload the affected connection when required, then inspect tool discovery. |
| Partial indexing/write failures | Report affected item keys; retry only failed items after resolving the cause. |
| Index lock | Identify the owning process and its state; do not stop unrelated sessions or delete database locks blindly. |

For setup, use [install-steps.md](install-steps.md). Confirm current command flags
with installed help. Provider pricing, quotas and model quality are not fixed facts
of this skill; check primary documentation only when that choice matters.

Compare live Zotero items with index contents before duplicate cleanup. DOI and
attachment hashes can support identity; a similar title/embedding is a review lead,
not authorization to merge/delete. Preserve annotations and attachment ownership.

A reset is a last-resort, explicitly scoped repair. Identify exact config/index paths,
retain a recoverable copy when needed, and determine whether targeted repair/reindex
can solve the issue. Never apply a generic `rm -rf` recipe to the user's library.
