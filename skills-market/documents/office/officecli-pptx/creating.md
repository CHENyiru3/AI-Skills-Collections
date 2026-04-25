# Creating `.pptx` Files

Use this path when building a presentation from scratch.

## Minimal Recipe

```bash
officecli create deck.pptx
officecli add deck.pptx / --type slide --prop layout=blank --prop background=1A1A2E
officecli add deck.pptx /slide[1] --type shape --prop text="Q4 Report" --prop x=2cm --prop y=2cm --prop width=20cm --prop height=3cm --prop font=Georgia --prop size=32 --prop bold=true --prop color=FFFFFF
officecli add deck.pptx /slide[1] --type shape --prop text="Revenue grew 25%" --prop x=2cm --prop y=6cm --prop width=20cm --prop height=2cm --prop font=Calibri --prop size=20 --prop color=CADCFC
officecli validate deck.pptx
```

## Common Building Blocks

```bash
officecli add slides.pptx / --type slide --prop layout=blank --prop background=FFFFFF
officecli add slides.pptx /slide[1] --type picture --prop path=chart.png --prop x=18cm --prop y=4cm --prop width=12cm --prop height=8cm --prop alt="Chart"
officecli add slides.pptx /slide[1] --type chart --prop chartType=column --prop categories="Q1,Q2,Q3,Q4" --prop series1="Revenue:42,58,65,78"
officecli add slides.pptx /slide[1] --type table --prop rows=4 --prop cols=3 --prop x=2cm --prop y=8cm --prop width=20cm --prop height=6cm
officecli add slides.pptx /slide[1] --type notes --prop text="Speaker notes"
```

## Guidance

- Avoid text-only decks. Use charts, images, or shapes on every slide.
- Keep a small palette with one dominant color and one accent.
- Vary layouts across slides instead of repeating the same structure.
- Run `view outline`, `view issues`, `view html --browser`, and `validate`.
