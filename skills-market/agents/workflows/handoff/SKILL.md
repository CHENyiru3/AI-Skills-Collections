---
name: handoff
description: Write a compact temporary conversation handoff for another agent. Use when the user explicitly requests session transfer; not automatic project logging or continuation of the underlying task.
metadata:
  version: "1.0.0"
  argument-hint: What will the next session be used for?
  disable-model-invocation: true
---

# Handoff

Use any supplied next-session focus to prioritize the context. Save a uniquely
named `handoff-*.md` file in the operating system's reported temporary directory;
return its absolute path. Do not overwrite a file or place the handoff in the
workspace unless the user explicitly chooses another destination.

Capture the objective, verified current state, completed outcomes, remaining
work, constraints, authorization, unresolved decisions, and concrete next steps.
Separate assumptions and proposals from verified facts. Include exact commands
only when they matter to continuation; link durable specs, reports, commits,
and artifacts instead of repeating them.

Include a `Suggested skills` section naming only relevant skills actually
available to the next agent. Tell it to load them using its supported skill
mechanism; do not assume a tool literally named `Skill`. If none apply, say so.

Redact secrets and unnecessary personal/private identifiers. Preserve only
operational identifiers needed to resume. Verify the handoff exists, report its
path, and stop; creating a handoff does not authorize additional project work.
