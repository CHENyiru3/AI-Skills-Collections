---
name: skill-seekers
domain: core
description: Use this skill when the user wants to use Skill Seekers to turn documentation sites, GitHub repositories, local codebases, PDFs, videos, notebooks, wikis, or other knowledge sources into AI-ready outputs such as Claude skills, OpenAI/Gemini assets, RAG documents, vector database payloads, or IDE rule files. Also use when the user explicitly mentions Skill Seekers, `skill-seekers`, or asks how to package one knowledge source for multiple AI platforms.
---

# Skill Seekers

Skill Seekers is a CLI and MCP-oriented workflow for converting source material into structured AI knowledge assets. Use this skill to keep the interaction focused on source selection, packaging target, and the smallest command sequence that gets the user to a usable output.

## Language Selection

- Default to [references/english.md](./references/english.md).
- If the user asks in Chinese or wants Chinese instructions, use [references/chinese.md](./references/chinese.md).
- Do not load both reference files unless translation or comparison is part of the task.

## Core Workflow

1. Identify the source type.
2. Identify the target output.
3. Recommend the shortest viable Skill Seekers flow.
4. Expand into config, enhancement, or multi-source workflows only if the user needs them.

Keep the first answer concrete. Prefer commands over long explanations.

## Source Types To Recognize

- Documentation sites
- GitHub repositories
- Local projects
- PDF, Word, EPUB, PowerPoint, and HTML files
- Jupyter notebooks
- OpenAPI specs
- RSS or Atom feeds
- Videos
- Confluence, Notion, Slack, or Discord exports

## Common Targets

- Claude skill packages
- Gemini skill packages
- OpenAI or Custom GPT packages
- LangChain or LlamaIndex documents
- Haystack documents
- Markdown for vector databases
- IDE context or rule files for tools such as Cursor, Windsurf, Continue, or Cline

## Response Pattern

When helping the user:

- State the assumed source and output target.
- Give the minimum install and command sequence first.
- Mention optional enhancement or packaging presets only when they materially help.
- If the task is broad or underspecified, ask for the source, target platform, and whether they want quick commands or a reusable config.

## Quick-Start Bias

Start with the direct flow:

```bash
pip install skill-seekers
skill-seekers create <source>
skill-seekers package output/<name> --target <platform>
```

Only move to config-heavy or multi-source guidance after the simple path is clear.

## When To Read The References

- Load [references/english.md](./references/english.md) for command patterns, supported source families, packaging targets, and common workflows.
- Load [references/chinese.md](./references/chinese.md) when the user wants the same guidance in Chinese.

## Output Expectations

Prefer:

- Short install steps
- Ready-to-run commands
- A note about the produced artifact
- A small set of next options such as enhancement, batching, or packaging for more targets
