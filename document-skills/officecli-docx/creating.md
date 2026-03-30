# Creating `.docx` Files

Use this path when no template exists.

## Minimal Recipe

```bash
officecli create report.docx
officecli set report.docx / --prop title="Q4 Report" --prop author="Team"
officecli set report.docx / --prop defaultFont=Calibri
officecli add report.docx /body --type paragraph --prop text="Q4 Report" --prop style=Heading1
officecli add report.docx /body --type paragraph --prop text="Executive Summary" --prop style=Heading2
officecli add report.docx /body --type paragraph --prop text="Revenue increased by 25% year-over-year." --prop size=11pt --prop lineSpacing=1.15x
officecli validate report.docx
```

## Common Building Blocks

```bash
officecli add doc.docx /body --type paragraph --prop text="Hello world"
officecli add doc.docx /body --type table --prop rows=4 --prop cols=3 --prop width="100%"
officecli add doc.docx / --type header --prop text="Company" --prop type=default
officecli add doc.docx / --type footer --prop text="Page " --prop type=default
officecli add doc.docx "/footer[1]" --type field --prop fieldType=page
officecli add doc.docx /body --type picture --prop path=figure.png --prop width=12cm --prop height=8cm --prop alt="Figure"
officecli add doc.docx /body --type chart --prop chartType=column --prop categories="Q1,Q2,Q3,Q4" --prop series1="Revenue:42,58,65,78"
```

## Guidance

- Define heading styles before relying on `Heading1`/`Heading2` in blank docs.
- Use hanging indents for references instead of manual spaces.
- Add page numbers in headers or footers for professional output.
- After generation, run `view outline`, `view issues`, and `validate`.
