# Project Management Documents

Read this reference when creating or updating `project_index.md` or `last_recap.md`.

## Merge Rules

Inspect the existing document before editing it. Preserve researcher-written notes, decisions, warnings, and useful project-specific sections. Add missing information narrowly; do not regenerate a mature document solely to match these templates.

Use relative Markdown links where links help navigation. The default convention is English project documents and a Chinese `last_recap.md`; preserve explicit user choices and established project languages when different. Do not claim that an output is canonical, complete, validated, or scientifically meaningful unless the workspace or researcher establishes that fact.

## `project_index.md`

This file is the durable map of the project. English is the default language.

Recommended starting structure:

```markdown
# Project Index

## Overview

- Research objective: TBD
- Current phase: TBD
- Project lead: TBD

## Directories and Key Files

| Path | Purpose | Status or Notes |
| --- | --- | --- |
| `data/` | Analysis or training data | TBD |
| `scripts/` | Analysis and utility scripts | TBD |
| `outputs/` | Generated results and run artifacts | TBD |
| `log/` | Execution logs and handoff records | TBD |

## Main Entry Points and Environment

- Main entry point: TBD
- Environment or dependency files: TBD
- How to run: TBD

## Data and Outputs

- Main inputs: TBD
- Main outputs: TBD
- Data restrictions or privacy requirements: TBD

## Confirmed Conventions and Decisions

- TBD

## Project-Specific Skills

- TBD
```

Omit sections that do not help the actual project. Update this file when stable facts change, not after every run.

## `last_recap.md`

This file is the latest concise handoff from the agent to the researcher. The default is Chinese prose with code identifiers, commands, and filenames unchanged; adapt to the project’s chosen language.

Recommended structure:

```markdown
# 最新工作回顾

- 更新时间：YYYY-MM-DD HH:MM（时区）
- 本次目标：...
- 当前状态：已完成 / 部分完成 / 阻塞

## 已完成

- ...

## 变更与产物

- 修改文件：...
- 输出位置：...
- 运行命令或检查：...

## 关键结果与限制

- 已观察到的结果：...
- 尚未验证或需要谨慎解释的内容：...

## 问题与待确认事项

- ...

## 下一步

1. ...
```

Use `无` when a retained section has no entries. Keep the status honest: use `部分完成` when required work remains, and `阻塞` only when progress actually depends on missing researcher input or an unavailable external condition.

`last_recap.md` is a current-state document, not a full transcript. Summarize commands and checks rather than pasting terminal output. If the project already archives handoffs under `log/`, follow that convention before updating the latest recap; otherwise do not introduce an archive automatically.
