"""Reusable summary helpers for the Assignment 4 pandas translation."""

import pandas as pd


def summarize_bmi_by_group(
    data: pd.DataFrame,
    age_min: int = 20,
    age_max: int = 80,
) -> pd.DataFrame:
    """Summarize BMI by income group and gender for an inclusive age range."""
    filtered = data.loc[
        data["BMI"].notna()
        & data["IncomeGroup"].notna()
        & data["Gender"].notna()
        & data["Age"].between(age_min, age_max, inclusive="both")
    ]

    summary = (
        filtered.groupby(["IncomeGroup", "Gender"], as_index=False, sort=True)
        .agg(
            n=("BMI", "size"),
            mean_bmi=("BMI", "mean"),
            sd_bmi=("BMI", "std"),
        )
    )
    summary[["mean_bmi", "sd_bmi"]] = summary[["mean_bmi", "sd_bmi"]].round(1)
    return summary
