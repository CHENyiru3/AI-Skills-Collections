# Editing Existing `.pptx` Files

Use this path when the presentation already exists.

## Inspect First

```bash
officecli view slides.pptx issues
officecli view slides.pptx outline
officecli get slides.pptx /slide[1] --depth 1
```

## Safe Editing Order

1. Structural changes first: add/remove/move slides or shapes
2. Re-query slide contents after structural or z-order changes
3. Update text, charts, tables, notes, or images
4. Re-run visual QA and validation

## Examples

```bash
officecli set slides.pptx "/slide[1]/shape[1]" --prop text="Updated Title"
officecli set slides.pptx "/slide[1]/chart[1]" --prop title="Updated Revenue Trend"
officecli remove slides.pptx "/slide[2]/shape[4]"
officecli move slides.pptx "/slide[3]" --to / --index 1
officecli set slides.pptx "/slide[1]/shape[5]" --prop zorder=back
```

## Pitfalls

- Shape indices can change after z-order operations.
- Delete and recreate charts if you need to change series count.
- Blank-layout slides may still trigger title warnings in `view issues`; check whether that warning is expected.
- Always preview after edits; validation alone is not enough for slide quality.
