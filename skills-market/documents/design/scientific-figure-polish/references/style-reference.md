# Compact scientific figure style

These conventions distill the author's FEAST manuscript figure reviews. Apply them as user preferences, not journal regulations. Preserve a different explicit style when the user requests it.

## Visual character

The desired figure is dense enough to read as one organized scientific composition. Use clear panel groups, aligned data regions, a restrained sans-serif hierarchy, neutral headings, and existing scientific color palettes. Related maps and plots form regular rows and columns. Whitespace separates groups without spreading them apart.

The author explicitly rejected a roomier Figure 6 and requested the tightness of the original. A revision that only looks clean after adding a much taller canvas misses this preference. Prefer:

- Short, repeatable title-to-data gaps.
- Consistent, compact spacing between rows of the same family.
- Shared coordinate explanations, axis captions, and legends.
- Aligned condition captions across corresponding groups.
- Single-line region labels when they fit, rather than fragmented words.

The final Figure 6 revision was about 19% shorter than the rejected revision. This records the direction of the correction; it is not a target percentage for future figures.

## Typography examples

The following were used at roughly 595 pt artwork width. Choose actual sizes for the intended printed width and surrounding figures. Do not rescale an entire group and accidentally create a different effective font size.

| Level | Example | Reference treatment |
|---|---|---|
| Main panel tag | a, b, c | Existing 12 pt retained; bold, lowercase |
| Gene/subplot header | Slc17a7, Gad2, Reln | 7.5 pt bold, shared across comparable panels |
| Condition title | Reference sample or transfer condition | Around 7 pt bold |
| Secondary sample ID | GSM accession | Around 6.25 pt regular |
| Region/legend label | DorsalVZ, Septum | Around 6.25–6.5 pt regular |
| Ticks and small plot annotations | Axis values, section coordinate | Around 5.5 pt at that artwork scale |

These values are examples, not a minimum-size policy. Some earlier embedded anatomical callouts remained constrained by their source raster. Do not copy that limitation into new editable artwork. Keep equivalent tiers consistent and inspect at the final manuscript size.

## Color examples

- Figure 3 benchmark headings were changed from deep blue to deep gray, approximately `#333333`.
- Its red ARI annotations were changed to black while retaining the numerical results.
- This preference concerns neutral explanatory text. It does not authorize changing a red/blue data palette, region colors, cluster colors, or a meaningful highlighted condition.

## What counts as an equal unit

| Unit family | Match | Preserve |
|---|---|---|
| Line plots or boxplots | Inner axes width/height, column starts, title gaps | Data values, axis limits, tick calibration |
| The same slice across methods/genes | Viewport size, centers, common tissue scale | Aspect, anatomy, background/overlay registration |
| Different anatomical stages | Equal outer cells and alignment | Scientifically meaningful differences in tissue size |
| Plane previews and 3D composites | Complete viewport, repeated physical size, centers | All corners, projected geometry, annotations |
| Heatmaps | Data-frame size, cell order, title baseline | Cell values, palette/calibration, row/column identities |
| Network diagrams | Complete unit canvas, node centers, caption alignment | Edges, directions, loops, weights, node colors |

Tissue ink bounds are not viewports. Sparse maps and age-dependent shapes naturally occupy different fractions of equal cells. Do not normalize them by stretching their content.

## Specific annotation precedents

- Figure 4 used one shared mean/variance/zero-proportion coordinate key and reduced repeated alpha explanations. Distinct parameter values remained visible.
- The author's complaint about Figure 4b/c concerned unequal actual line-plot frames. Matching the outside panel boxes alone would not resolve it.
- Figure 6e/f used matching condition captions only after the author confirmed their correspondence. Preserve evidence-based identity mapping in future figures.
- Upper-row heatmap x tick names were shared with the bottom row to make the compact Figure 6 readable without excessive row height.

These are design precedents. Do not transfer project-specific scores, gene sets, condition orders, or old geometry numbers into another figure.
