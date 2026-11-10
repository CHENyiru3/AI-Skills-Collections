---
name: mcp-builder
domain: agents
description: Build or change an MCP server that exposes a specific service or workflow through tools, resources or prompts. Use for MCP server implementation and protocol troubleshooting; not for ordinary use of an existing connected tool.
license: Complete terms in LICENSE.txt
metadata:
  version: "1.0.1"
---

# MCP Server Development

Start with the user workflows, service API and client environment. Implement the
smallest useful surface; comprehensive endpoint coverage is not the default.
Choose the repository's language/SDK and supported protocol revision. Check the
installed SDK and [official specification](https://modelcontextprotocol.io/specification/latest)
before reusing version-sensitive examples.

## Preserve the interface contract

- Give tools action-oriented names, narrow descriptions and validated input schemas.
  State identifiers, units, defaults and mutation effects where ambiguity matters.
- Return bounded, focused results with pagination/cursors where the service needs
  them. Preserve machine-readable data and explain truncation or partial results.
- Make errors actionable without leaking credentials or private upstream payloads.
  Distinguish invalid input, denied access, rate limits and upstream failure.
- Set annotations truthfully; hints such as read-only/destructive/idempotent describe
  behavior and do not replace authorization checks.
- Keep secrets out of arguments/logs when the service offers a protected mechanism.
  Respect tenant/user identity, least-required scopes and upstream access rules.
- For stdio, reserve stdout for protocol traffic and send diagnostics to stderr.
  For remote transport, implement the supported auth/session/origin requirements;
  do not treat a local stdio example as a secure public HTTP deployment.

## Implement and verify the requested slice

Share authentication, HTTP timeout/retry and response-formatting code where it
actually removes repeated behavior. Read only the relevant implementation guide:

- [Python guide](reference/python_mcp_server.md) for Python SDK patterns.
- [TypeScript guide](reference/node_mcp_server.md) for Node SDK patterns.
- [Design notes](reference/mcp_best_practices.md) for a specific interface question.

Bundled examples may target a different SDK revision; verify imports and signatures
against the installed version before copying them. Use stdio for a local process or
a supported HTTP transport for a remote service according to the client contract.

Build/type-check as appropriate and exercise initialization, tool discovery and a
representative call. Check validation errors and a relevant permission/error path.
Use an Inspector or a small client when available; syntax alone does not establish
protocol compatibility. Avoid exercising a destructive live API just to test wiring.

For a requested usability benchmark, read [evaluation guidance](reference/evaluation.md)
and inspect `scripts/evaluation.py --help`. Select representative cases with known
answers and explicit data provenance. Ten complex questions and a full benchmark
are not prerequisites to shipping a small valid server.

Report the supported transport/version, tools implemented, checks and deployment
limits. Stop when the requested server behavior works; new endpoints, evaluation
infrastructure and production deployment are separate scope decisions.
