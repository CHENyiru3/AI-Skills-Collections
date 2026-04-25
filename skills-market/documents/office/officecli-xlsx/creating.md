# Creating `.xlsx` Files

Use this path when the workbook does not exist yet.

## Minimal Recipe

```bash
officecli create budget.xlsx
officecli set budget.xlsx / --prop title="Budget" --prop author="Finance"
officecli set budget.xlsx "/Sheet1/A1" --prop value="Category" --prop bold=true
officecli set budget.xlsx "/Sheet1/B1" --prop value="Amount" --prop bold=true
officecli set budget.xlsx "/Sheet1/A2" --prop value="Revenue"
officecli set budget.xlsx "/Sheet1/B2" --prop formula="SUM(B3:B10)" --prop numFmt='$#,##0'
officecli validate budget.xlsx
```

## Common Building Blocks

```bash
officecli add data.xlsx / --type sheet --prop name="Summary"
officecli set data.xlsx "/Sheet1/col[A]" --prop width=20
officecli set data.xlsx "/Sheet1" --prop freeze=A2
officecli add data.xlsx /Sheet1 --type validation --prop sqref="C2:C100" --prop type=list --prop formula1="Yes,No"
officecli add data.xlsx /Sheet1 --type chart --prop chartType=column --prop categories="Q1,Q2,Q3,Q4" --prop series1="Revenue:42,58,65,78"
officecli add data.xlsx / --type namedrange --prop name="RevenueTotal" --prop ref="Sheet1!B2"
```

## Guidance

- Formula cells should stay formula cells.
- Set number formats explicitly for currency, percentages, and dates.
- Set column widths and freeze panes deliberately.
- After creation, run `view annotated`, `view issues`, and `validate`.
