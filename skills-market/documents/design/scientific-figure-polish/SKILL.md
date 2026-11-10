---
name: scientific-figure-polish
description: Review and refine multi-panel scientific manuscript figures in the user's compact publication style. Use for consistent font hierarchy, equal comparable plot frames and map viewports, aligned subpanels, clearer legends, and shared annotations. Applies to existing PDF/vector artwork and plotting sources; excludes manuscript prose editing and scientific recomputation.
metadata:
  version: "1.0.1"
---

# Scientific Figure Polish

Apply the user's FEAST-derived figure style: compact, organized, readable, and scientifically faithful. Current user instructions override these defaults. Read [style-reference.md](references/style-reference.md) for visual conventions and examples. For direct PDF edits, also read [pdf-editing.md](references/pdf-editing.md) and use the available PDF skill for its format-specific requirements.

## Priorities

1. Preserve scientific meaning and the author's current edits.
2. Retain the original figure's compact density and organize the content on a clear grid.
3. Match the size and alignment of comparable units.
4. Make equivalent text levels consistent and readable.

Tighten internal gaps before extending the artwork; cropping outside margins alone does not fix a loose composition. Preserve compactness jointly with readability.

Compactness and readability are joint constraints. If larger text does not fit, first share repeated annotations, repair wrapping, reduce gaps, or rebalance groups. Do not force the old footprint with unreadable text or overlaps. Use the smallest necessary geometry adjustment and explain a material expansion; changing scientific content requires separate justification.

## Establish the current baseline

- Inspect the actual current artwork before editing. The author also modifies files manually. When replacing shared or manually edited artwork, retain a recoverable baseline and check for intervening author edits; hashes can help identify the exact source. A read-only review does not need a backup workflow.
- Treat the latest author-approved artwork as authoritative. Plotting sources or retained component figures may predate manual changes. Rebuild only when their scientific content and author adjustments can be preserved.
- For density comparisons, “original” defaults to the current supplied figure before this edit. If the author identifies an earlier version as the compactness reference, use that version's organization while preserving the current scientific content and manual edits.
- Review every unit in the requested scope. An all-figure scan includes main and supplementary figures; a named-figure request stays within that scope.
- Render the whole figure and inspect dense details. Identify panel roles, comparable families, annotation levels, and the original density before changing geometry.
- Optionally use [scripts/figure_inventory.py](scripts/figure_inventory.py) for a read-only PDF inventory and review previews. Its measurements support inspection; they do not prove correct alignment or scientific fidelity.

## Build a compact grid

- Define comparison groups by their scientific role and comparison context. Two support plots, or the same slice across methods, form a family; every tissue image or every line chart in the manuscript does not automatically share one global size.
- Align panel-tag edges, heading baselines, plot boundaries, map-column centers, and legend entries. Use repeatable row/column pitches and small, consistent gutters.
- Reduce oversized title-to-data gaps, excessive row spacing, and isolated empty areas. Use shared captions and concise wrapping to gain space before shrinking scientific content or extending the page.
- Compare the revised internal spacing and total artwork footprint with the original. A visibly taller or looser arrangement needs a reason grounded in the user's request.
- Use the same **inner plotting-frame width and height** for the same family of charts, including charts in different main panels. Equal outer boxes can hide unequal axes. Tick-label widths and legend margins should not determine the data-frame size.
- Set identical target geometry within each group and measure it in page units. Distinguish harmless source/serialization rounding from visible drift; report measured variation when claiming exact matching.
- Use equal viewports and fixed centers for comparable tissue maps, embeddings, slice views, and complete 3D composites. Do not stretch tissue ink to fill each viewport. Preserve aspect ratio, anatomical proportions, and meaningful differences in physical scale.
- Keep registered layers together, including a map's background and expression overlay. Translate or scale the complete unit with one transform; do not independently recenter its rasters.
- A chart's frame aspect can be adjusted when its data-to-axis mapping remains correct and comparable charts stay matched. Spatial geometry requires an aspect-preserving transform.

## Apply a text hierarchy

- Use lowercase main panel tags, `a`, `b`, `c`, retaining their existing point size. This rule applies to panel tags only. Preserve gene names, acronyms, sample IDs, scientific notation, and condition codes.
- Enlarge undersized subplot titles, tick labels, legends, and annotations. Unify equivalent levels across the figure rather than choosing a different size for every imported component.
- Preserve the established typeface where practical; the reference style uses Arial/Helvetica-like sans serif, bold headings, and regular labels. Distinguish hierarchy with a few font levels and restrained emphasis.
- Judge readability at the intended manuscript width. Reference point sizes are examples at a particular artwork scale, not universal journal defaults.
- When restyling neutral section/benchmark headings or metric annotations, prefer deep gray headings and black numbers. Preserve other existing figure-specific colors unless recoloring is requested; a neutral-text preference does not authorize unrelated color changes.

## Simplify annotations without losing meaning

- Share repeated x/y captions, coordinate keys, legends, and parameter explanations within a clearly defined comparison group. For example, one shared `x: log mean | y: log variance | z: zero proportion` key can serve a parameter-grid group.
- Keep condition-specific values, stage labels, units, and sample identifiers. A shared alpha caption does not remove different alpha values.
- Consider keeping repeated tick names only on the bottom row or left column when the common axes are unmistakable. Preserve numerical calibration and enough labels to read every unit unambiguously.
- Position legends close to the plots they explain. Align swatches, labels, and baselines; repair awkward word breaks such as `Septu` / `m`.
- Corresponding units should use the same condition order and matching captions when that mapping is supported. Do not infer or silently correct scientific identities, metrics, or conditions from layout or visual similarity alone.

## Verify the result

- Render the latest revision and inspect both the whole composition and critical details. Check crowding, complete cube/network outlines, colorbar endpoints, tick placement, superscripts, and shared-label coverage.
- Measure comparable frames and viewports in page coordinates. Check centers, pitches, and baselines, not just a contact sheet's apparent similarity.
- Preserve numerical values, plotted curves, heatmap cell colors, network directions/weights, tissue proportions, and layer registration. Do not rerun experiments to solve a layout problem.
- For reused artwork, compare image/mask hashes or drawing operations where useful. Recheck axis calibration after a chart-frame change. These checks complement visual review.
- Validate PDF structure with a parser as well as rendering: a PDF can display in Poppler while its resources remain malformed.
- Make routine, reversible layout decisions within the request. Ask only when scientific meaning or the requested scope is genuinely ambiguous. Report the concrete changes concisely and identify any unresolved scientific label issue separately.
