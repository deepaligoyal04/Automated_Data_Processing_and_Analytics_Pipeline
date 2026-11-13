import pandas as pd

def calculate_kpis(df: pd.DataFrame):
    if df.empty:
        return pd.DataFrame([{"metric": "Total records", "value": 0}])
    rows = [
        {"metric": "Total records", "value": int(len(df))},
        {"metric": "Average salary", "value": round(float(df["salary"].mean()), 2) if "salary" in df else None},
        {"metric": "Average performance score", "value": round(float(df["performance_score"].mean()), 2) if "performance_score" in df else None},
        {"metric": "Total hours", "value": round(float(df["hours"].sum()), 2) if "hours" in df else None},
        {"metric": "Departments represented", "value": int(df["department"].nunique()) if "department" in df else None},
    ]
    return pd.DataFrame(rows)

def department_metrics(df: pd.DataFrame):
    if "department" not in df:
        return pd.DataFrame()
    agg = {}
    for col in ["record_id", "salary", "performance_score", "hours"]:
        if col in df:
            agg[col] = "count" if col == "record_id" else "mean"
    result = df.groupby("department", dropna=False).agg(agg).reset_index()
    return result.rename(columns={"record_id": "record_count", "salary": "average_salary",
                                  "performance_score": "average_performance", "hours": "average_hours"})
