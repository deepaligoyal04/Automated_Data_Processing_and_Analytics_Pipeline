# Automated Data Processing and Analytics Pipeline

A modular Python project that reads multiple CSV/Excel files, cleans and validates records, performs Pandas/NumPy analysis, stores processed data in SQLite, and creates Excel reports and Matplotlib charts.

## Features
- Automated ingestion of all `.csv`, `.xlsx` and `.xls` files in `input_data/`.
- Data cleaning: standardised text/date formats, duplicate removal, invalid numeric handling and missing-value imputation.
- Custom validation functions with a separate validation-issues report.
- Pandas transformations and department-wise aggregations.
- SQLite storage and SQL-based retrieval.
- KPI calculations and department metrics.
- Multi-sheet Excel report generated with OpenPyXL.
- Matplotlib department performance chart.
- Logging and exception handling.

## Tech stack
Python, Pandas, NumPy, SQLite, SQL, Matplotlib, OpenPyXL.

## Run on Windows
1. Extract the ZIP and open the folder in VS Code.
2. Open the terminal in the project folder.
3. Create and activate a virtual environment:

```bash
python -m venv venv
venv\\Scripts\\activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run:

```bash
python main.py
```

## Input files
Place any CSV or Excel files inside `input_data/`. The sample folder includes:
- `employees.csv`
- `activities.xlsx`

The demo combines files into one dataset. Since the sample files have different columns, fields that do not exist in a particular source remain blank and are handled by the cleaning/validation steps. For a real organisation, align source schemas or add a mapping layer before combining.

## Generated outputs
After execution, check the `output/` folder:
- `analytics.db` — SQLite database with `processed_records` table.
- `analytics_report.xlsx` — KPI Summary, Department Metrics, Processed Data, Validation Issues sheets.
- `department_performance.png` — Matplotlib chart.

The `logs/pipeline.log` file records pipeline execution and errors.

## Customisation
- Update cleaning rules in `src/cleaning.py`.
- Add validation rules in `src/validation.py`.
- Modify KPIs and groupings in `src/analytics.py`.
- Extend reporting sheets in `src/reporting.py`.

## Notes
This is an academic ETL/analytics prototype. The included sample data intentionally contains a duplicate, inconsistent date formatting, missing values and invalid numeric entries to demonstrate cleaning and validation. Adapt the schema and business rules to your actual datasets.
