import logging
import pandas as pd
import numpy as np

def clean_records(df: pd.DataFrame) -> pd.DataFrame:
    """Standardise common fields, remove duplicates and repair invalid numeric values."""
    data = df.copy()
    data.columns = [str(c).strip().lower().replace(" ", "_") for c in data.columns]

    if "employee" in data.columns:
        data["employee"] = data["employee"].astype("string").str.strip().str.title()
    if "department" in data.columns:
        data["department"] = data["department"].astype("string").str.strip().str.title()
        data["department"] = data["department"].replace({"Hr": "Hr", "It": "It"})
    if "date" in data.columns:
        data["date"] = pd.to_datetime(data["date"], errors="coerce", dayfirst=True)

    for col in ["salary", "performance_score", "hours"]:
        if col in data.columns:
            data[col] = pd.to_numeric(data[col], errors="coerce")
            data.loc[data[col] < 0, col] = np.nan

    before = len(data)
    subset = [c for c in ["record_id", "employee", "project"] if c in data.columns]
    data = data.drop_duplicates(subset=subset or None)
    logging.info("Removed %s duplicate rows", before - len(data))

    # Fill numeric missing values with the median; preserve NaN if a column is entirely empty.
    for col in ["salary", "performance_score", "hours"]:
        if col in data.columns and data[col].notna().any():
            data[col] = data[col].fillna(data[col].median())

    if "department" in data.columns:
        data["department"] = data["department"].fillna("Unknown")
    return data
