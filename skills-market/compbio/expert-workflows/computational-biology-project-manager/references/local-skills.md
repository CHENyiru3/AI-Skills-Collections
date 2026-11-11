# Project-local skill distillation

Use when the user requests a local skill or has authorized ongoing distillation.
Choose a demonstrated recurring workflow with stable inputs, outputs, or a
non-obvious project contract. A speculative one-off command is insufficient.

1. Inspect existing local skills and their ownership before adding a duplicate.
2. Preserve approved scientific choices; do not turn an inference into policy.
3. Write a specific trigger and the smallest instructions that change decisions.
4. Put substantial conditional details in linked references and reusable
   deterministic operations in scripts only when they serve the workflow.
5. Follow the target agent's documented project-local discovery convention.
   For projects using `.agents/skills`, place one named folder at
   `<project-root>/.agents/skills/<skill-name>/SKILL.md`. Resolve the repository
   root rather than using an arbitrary nested working directory.
6. Check frontmatter, referenced resources, and relevant helper behavior. Confirm
   discovery using the target agent's available skill listing.
7. Record the location and purpose in existing project continuity documents.

Do not write to user-global skill directories without that requested scope.
Include the complete required resources; use a symlink only when its target
will remain available to intended consumers. If the source workflow is still
ambiguous, record a candidate rather than encoding an unapproved rule.
