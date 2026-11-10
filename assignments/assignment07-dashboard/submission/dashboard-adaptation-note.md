# Dashboard Adaptation Note

## Audience

Public-health analyst preparing a short briefing on descriptive BMI trends in the classroom NHANES equity dataset.

## Dashboard Question

Among adults age 20-80, how does mean BMI vary across NHANES cycles for the selected income group?

## Control And Visualization

- Control or interaction: `selected_income` chooses the income group shown in the dashboard.
- Visualization affected: the line chart of mean BMI by NHANES cycle.
- What changes when the control changes: the title, summary table, and plotted values all update to the selected group, while the underlying logic and exclusion rules remain the same.

## Before And After

| Original text | Revised text | Why the revision helps |
|---|---|---|
| `selected_income <- "Low Income (<1.3)"` | `selected_income <- "Middle Income"` | This shifts the product from a default example to a more balanced middle-income comparison that is easier to discuss in a briefing. |
| `title = paste("Mean BMI for", selected_income)` | `title = paste("Mean BMI among", selected_income, "adults")` | The revised wording is more audience-facing and reads as a descriptive summary rather than a generic code label. |
| Generic interpretation referencing only the selected group | Description of a time trend for briefing use and a reminder that the pattern is descriptive, not causal | This makes the dashboard easier for a public-health audience to interpret while preserving the methodological caution. |

## Test Result

The dashboard was rendered from the repository root with `quarto render assignments/assignment07-dashboard/submission/dashboard.qmd`. The render completed successfully and produced the expected HTML output with the updated control value, summary table, and plot.

## Limitation

This dashboard is descriptive and unweighted, so it should not be used to claim causality or generalize to the national population.

## Privacy Check

The preview uses aggregated means only, excludes row-level data, and keeps the interpretation descriptive and non-causal. The text avoids small-cell overclaiming and does not suggest that income determines BMI.
