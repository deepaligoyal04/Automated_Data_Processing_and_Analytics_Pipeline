import pandas as pd

def validate_records(df: pd.DataFrame):
    """Return (valid_rows, issue_rows) using custom business validation rules."""
    data = df.copy()
    issues = pd.Series("", index=data.index, dtype="string")

    if "record_id" in data.columns:
        issues.loc[data["record_id"].isna()] += "Missing record_id; "
    if "employee" in data.columns:
        issues.loc[data["employee"].isna() | (data["employee"].astype(str).str.strip() == "")] += "Missing employee; "
    if "date" in data.columns:
        issues.loc[data["date"].isna()] += "Invalid/missing date; "
    if "performance_score" in data.columns:
        issues.loc[~data["performance_score"].between(0, 5)] += "Performance score outside 0-5; "
    if "hours" in data.columns:
        issues.loc[data["hours"] < 0] += "Negative hours; "

    data["validation_issues"] = issues
    invalid = data[data["validation_issues"] != ""].copy()
    valid = data[data["validation_issues"] == ""].drop(columns=["validation_issues"]).copy()
    return valid, invalid
