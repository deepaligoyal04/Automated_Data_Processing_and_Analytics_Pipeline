import logging
from .config import INPUT_DIR, OUTPUT_DIR, LOG_DIR, LOG_PATH
from .ingestion import load_files
from .cleaning import clean_records
from .validation import validate_records
from .analytics import calculate_kpis, department_metrics
from .database import save_to_sqlite
from .reporting import create_chart, export_excel

def run_pipeline():
    OUTPUT_DIR.mkdir(exist_ok=True)
    LOG_DIR.mkdir(exist_ok=True)
    logging.basicConfig(filename=LOG_PATH, level=logging.INFO,
                        format="%(asctime)s | %(levelname)s | %(message)s", force=True)
    try:
        logging.info("Pipeline started")
        raw = load_files(INPUT_DIR)
        cleaned = clean_records(raw)
        valid, issues = validate_records(cleaned)
        stored = save_to_sqlite(valid)
        kpis = calculate_kpis(stored)
        departments = department_metrics(stored)
        create_chart(departments)
        export_excel({
            "KPI Summary": kpis,
            "Department Metrics": departments,
            "Processed Data": stored,
            "Validation Issues": issues
        })
        logging.info("Pipeline completed successfully")
        print("Pipeline completed.")
        print(f"Input rows: {len(raw)} | Cleaned rows: {len(cleaned)}")
        print(f"Valid rows stored: {len(valid)} | Rows with validation issues: {len(issues)}")
        print(f"Excel report: {OUTPUT_DIR / 'analytics_report.xlsx'}")
        print(f"Chart: {OUTPUT_DIR / 'department_performance.png'}")
        print(f"SQLite database: {OUTPUT_DIR / 'analytics.db'}")
    except Exception:
        logging.exception("Pipeline failed")
        raise
