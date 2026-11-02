# Table 1 Audit Note

## Cohort

The intended cohort is adults ages 20–80 inclusive. The corrected code uses
`filter(between(Age, 20, 80))`, which includes both endpoints and documents the
cohort before the descriptive summary. It then explicitly excludes missing
`Age`, `BMI`, or `IncomeGroup` only when constructing Table 1.

## Missingness

The analysis reports missingness for `Age`, `BMI`, and `IncomeGroup` in the full
CSV before interpreting the Table 1 summaries. The complete-case rule is stated
in the methods note and implemented with explicit `!is.na()` filters.

## Planted Issues

| Issue | Category | Why it matters | Corrected approach |
|---|---|---|---|
| The starter includes an absolute Windows path and several guessed fallback paths. | Reproducibility | The first path is machine-specific and the result can depend on which working directory happens to be used. | Use the repository-relative CSV path and stop clearly if that expected path is missing. |
| The comment says the data were downloaded fresh last week. | Stewardship | It gives no reliable provenance and incorrectly suggests a fresh download when the repository contains a prepared classroom snapshot. | Name the prepared snapshot, its CDC/NCHS NHANES source, and its classroom-use boundary in the provenance note. |
| `filter(Age > 20, Age < 80)` excludes ages exactly 20 and 80. | Correctness | It does not implement the stated inclusive age 20–80 cohort. | Use `between(Age, 20, 80)` and report the cohort size before summaries. |
| `na.omit()` removes rows for missing values in every column, including variables not used in Table 1. | Correctness | Unrelated missing fields can unnecessarily change the analytic cohort, and the missingness decision is hidden. | Report missingness first and explicitly filter only missing `Age`, `BMI`, or `IncomeGroup` for this summary. |
| The starter does not report missingness before dropping rows. | Reproducibility | Readers cannot see how much data were excluded or reproduce the denominator. | Create and display a missingness table before the complete-case Table 1. |
| The parenthesized summary uses `var(BMI)` and `var(Age)` but labels the values as SD. | Correctness | Variance is not standard deviation, so the reported descriptive statistics are numerically wrong. | Use `sd()` and label the result mean (SD). |
| The interpretation claims statistical significance and that income determines BMI. | Interpretation | An unweighted descriptive table does not establish significance, causality, or direction of mechanism. | Describe observed group summaries only and state that the analysis is non-causal and unweighted. |
| The claim that the results are “publication-ready” is unsupported, and no privacy caution is provided. | Stewardship | Classroom row-level data require responsible handling and the analysis has not established external validity or disclosure safety. | Restrict the data to classroom learning, avoid uploading row-level records to external AI tools, and avoid population-level claims. |

## AI-Use Check

AI helped draft the Quarto structure, the explicit cohort and missingness
workflow, and the first wording of the audit categories. I verified the
dataset path and column names against the repository, checked that
`between(Age, 20, 80)` is inclusive, confirmed that the Table 1 filter names
only the required variables, and checked that `sd()` rather than `var()` is
used before rendering the final output.
