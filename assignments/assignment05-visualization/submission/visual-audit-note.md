# Visual Audit Note

## Plot Question

How does mean BMI differ across NHANES cycles for adults age 20-80 in each income group in the classroom NHANES equity dataset?

## Issues Checked

| Issue | Category | Why it matters | Correction |
|---|---|---|---|
| Y-axis is clipped to 24-28 | Correctness | This narrow scale exaggerates the gap between income groups and makes a modest difference look much larger than it is. | Use the full BMI range relevant to the data and keep the scale transparent in the caption. |
| Title claims a causal story: "Low income drives rising obesity" | Interpretation | The chart is descriptive and cannot show cause or population-level health effects. | Replace the title with a neutral description of the pattern, such as "Mean BMI by income group across NHANES cycles." |
| Only the first and last cycles are used in the flawed plot | Design | Dropping the intermediate cycles hides the actual trajectory and makes the pattern look cleaner than the evidence supports. | Keep all available NHANES cycles in the summary so the time trend is fully visible. |
| Missing or unclear age and exclusion rules are not stated | Correctness | The sample selection should be explicit because the classroom figure is not a full-population estimate. | Filter to adults age 20-80 and state in the caption that BMI, income group, and cycle missing values were excluded. |

## Final Caption

Descriptive, unweighted classroom summary. Mean BMI among adults age 20-80 is shown by NHANES cycle and income group in the prepared NHANES equity dataset (source: examples/nhanes-equity/data/nhanes_equity_v6.csv). Missing BMI, income group, and cycle values were excluded; no survey weights were applied, so this is a descriptive comparison rather than a weighted national estimate or causal analysis.

## AI-Use Check

AI helped draft the ggplot2 code and suggest a neutral title, but the column names, filtering logic, and interpretation were checked against the actual NHANES CSV and the dplyr output. I verified the mean BMI values by cycle and income group, confirmed that the plotting scale does not exaggerate the signal, and kept the final wording descriptive and unweighted rather than causal.
