# Skill Seekers Reference

Adapted from the upstream `yusufkaraaslan/Skill_Seekers` project for use inside this skill repository.

## What It Does

Skill Seekers turns source material into structured knowledge assets that can be packaged for multiple AI systems. The common pattern is:

```bash
pip install skill-seekers
skill-seekers create <source>
skill-seekers package output/<name> --target <platform>
```

## Typical Inputs

- Documentation sites
- GitHub repositories such as `facebook/react`
- Local folders such as `./my-project`
- PDF, DOCX, EPUB, PPTX, HTML, and OpenAPI files
- Jupyter notebooks
- RSS or Atom feeds
- Videos
- Confluence, Notion, Slack, or Discord exports

## Typical Outputs

- `--target claude` for Claude-oriented skill packages
- `--target gemini` for Gemini skill packages
- `--target openai` for OpenAI or Custom GPT packaging
- `--target langchain` for LangChain documents
- `--target llama-index` for LlamaIndex nodes
- `--target haystack` for Haystack documents
- Markdown or vector-database-ready content for downstream indexing

## Minimal Examples

### Documentation website

```bash
skill-seekers create https://docs.react.dev/
skill-seekers package output/react --target claude
```

### GitHub repository

```bash
skill-seekers create facebook/react
skill-seekers package output/react --target openai
```

### Local project

```bash
skill-seekers create ./my-project
skill-seekers package output/my-project --target langchain
```

### PDF

```bash
skill-seekers create manual.pdf
skill-seekers package output/manual --target claude
```

## How To Frame Recommendations

When answering users:

- Ask for the source if it is unclear.
- Ask for the target platform if they have not picked one.
- Start with a two-command or three-command path.
- Mention enhancement presets, reusable config files, or multi-source ingestion only after the basic flow is working.

## Useful Positioning

Skill Seekers is best described as a data-preparation layer for AI systems:

- One ingestion pass
- One structured output directory
- Multiple packaging targets from the same prepared asset

## Good Follow-Up Options

After the quick path, relevant next steps include:

- Packaging for multiple targets from the same output
- Creating a reusable config for repeatable ingestion
- Combining several source types into one asset
- Adding enhancement passes for richer `SKILL.md` output

## Upstream Pointers

- Repository: `https://github.com/yusufkaraaslan/Skill_Seekers`
- Website and documentation: `https://skillseekersweb.com/`
