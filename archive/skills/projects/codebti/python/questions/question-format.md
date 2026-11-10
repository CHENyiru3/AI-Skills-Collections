# Question Card Format

Use this format for fixed and adaptive CodeBTI questions.

````md
## QN. Placeholder Title

Dimension:
The primary CodeBTI dimension this question probes.

User-facing scenario:
One or two plain sentences shown to the user.

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:
```python
# Optional. Keep this short and focused.
```

Choices:
- A. A practical maintainable option.
- B. A different practical maintainable option.
- C. Another practical maintainable option.

Agent scoring:
- A: Hidden style-axis interpretation.
- B: Hidden style-axis interpretation.
- C: Hidden style-axis interpretation.

Pattern signals:
- A: Optional pattern tendency or anti-pattern signal.
- B: Optional pattern tendency or anti-pattern signal.
- C: Optional pattern tendency or anti-pattern signal.

CodeStyle output implications:
How the answer should affect generated project guidance.
````

## Code Example Rules

- Use Python in the initial version.
- Keep snippets small enough to compare quickly.
- Show the same problem solved in different styles when possible.
- Prefer real project situations: configuration, data loading, validation, services, commands, plugins, tests, and error handling.
- Avoid examples that require external libraries unless the question is about dependency tolerance.
- Do not make one choice obviously wrong.
- Do not ask users to identify a named design pattern.

## Choice Rules

- Use 2-4 choices.
- Make every choice plausible for some project.
- Describe what the user would maintain, not what is academically "correct".
- Keep labels neutral and concrete.
- Avoid jargon-only labels such as "Strategy" or "Factory" in user-facing choices.
- Avoid labels that imply skill level, such as "advanced", "strict", "simple", or "quick and dirty".
- Keep scoring hidden unless the user asks to inspect how CodeBTI works.

## Scoring Rules

Score answers on style dimensions before pattern names. Useful dimensions include:

- abstraction depth,
- typing posture,
- data modeling preference,
- construction style,
- dependency boundary strictness,
- error-handling style,
- extension mechanism,
- workflow orchestration,
- state management,
- testing and documentation expectations.

Pattern signals should remain secondary evidence. A generated `CodeStyle.md` should say what to do in code, not only name patterns.
