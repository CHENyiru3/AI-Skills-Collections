---
name: zotpilot
domain: writing
description: Search or organize a Zotero library through existing ZotPilot/Zotero tools, or configure ZotPilot when explicitly requested. Use for library-specific access; not every paper, citation or literature-writing task, and not automatic installation/indexing.
metadata:
  version: "1.0.1"
---

# ZotPilot and Zotero Library Work

Discover the available Zotero/ZotPilot connector and its actual tool schemas before
running a setup wrapper. Reuse working access. A local Zotero desktop/database is
not a prerequisite to every connected or Web API operation, and a citation-format
edit does not need whole-library indexing.

## Library operations

Select the actual library/collection and item identity. Use precise metadata search
for a known paper and semantic search only when its index/provider is available.
Distinguish live library contents, local index coverage and stale cached results.
Read passages with sufficient context; cite title/authors/year and available page
or section locators. Bibliographic correctness and support for a scientific claim
are different checks. Do not invent quotations, DOI metadata or experimental facts.

For organization, match by DOI or verified identifiers first; title/embedding
similarity alone is a review lead. Preview affected item keys/collection scope and
perform only the requested tag/collection changes. Batch operations can partially
fail: report and retry only failed items rather than assuming atomic rollback.
Do not merge/delete duplicate items or attachments as a default cleanup.

For folder intake, match existing items before imports. Keep separate statuses for
already present, existing item assigned to collection, new item created, attachment
pending and unresolved. Confirm local/Web library sync before claiming a local
index sees newly imported records. Do not rename source PDFs merely to query them.

## Optional setup or repair

Use [install-steps.md](references/install-steps.md) only for a requested installation
or configuration, and [troubleshooting.md](references/troubleshooting.md) for a
specific failure. Ordinary `scripts/run.py status --json`/help no longer installs
or upgrades anything; `--install` is an explicit opt-in. Registration requires a
named `--platform` and must preserve unrelated clients/configuration.

Agree on embedding provider and item scope before indexing private content. Cloud
embeddings transmit library-derived material; local models can require an initial
download. Indexing a missing item or rebuilding an index is not automatically
necessary for basic metadata/read operations. Do not print or pass API keys in
chat/command arguments; use configured protected credentials and appropriate
library-specific write scopes.

Tool names/parameters depend on the connected version. Read
[tool-guide.md](references/tool-guide.md) only for a matching bundled backend and
verify its schema before a call. Diagnose credentials, network, provider and stale
index separately rather than resetting configuration for every error.

Stop when the requested library result/change or scoped setup works. No whole-library
rebuild, additional client registration or remote write is implied by a search.
