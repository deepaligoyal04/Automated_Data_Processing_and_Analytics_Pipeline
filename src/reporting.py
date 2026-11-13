import logging
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from .config import REPORT_PATH, CHART_PATH

def create_chart(dept_df: pd.DataFrame):
    if dept_df.empty:
        return
    metric = "average_performance" if "average_performance" in dept_df else dept_df.columns[-1]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(dept_df["department"].astype(str), dept_df[metric])
    ax.set_title("Department-wise Performance")
    ax.set_xlabel("Department")
    ax.set_ylabel(metric.replace("_", " ").title())
    ax.tick_params(axis="x", rotation=25)
    fig.tight_layout()
    fig.savefig(CHART_PATH, dpi=150)
    plt.close(fig)
    logging.info("Saved chart to %s", CHART_PATH)

def export_excel(sheets: dict):
    with pd.ExcelWriter(REPORT_PATH, engine="openpyxl") as writer:
        for sheet_name, frame in sheets.items():
            frame.to_excel(writer, sheet_name=sheet_name[:31], index=False)
    logging.info("Saved Excel report to %s", REPORT_PATH)
