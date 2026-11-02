# AI-use note

AI helped organize the rerunnable Quarto analysis, suggest explicit missingness
handling, draft the Table 1 code,drafting explainations and identify categories of planted errors.

I verified the work by checking the repository-relative data path and the
`Age`, `BMI`, and `IncomeGroup` columns confirming that the cohort filter uses
inclusive ages 20–80; checking that missingness is reported before complete-case
exclusion; confirming that `sd()` is used for the reported standard deviations
and rendering the Quarto file to compare the displayed Table 1 with the
generated `table1.csv`.
