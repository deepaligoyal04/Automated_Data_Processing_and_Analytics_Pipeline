from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INPUT_DIR = ROOT / "input_data"
OUTPUT_DIR = ROOT / "output"
LOG_DIR = ROOT / "logs"
DB_PATH = OUTPUT_DIR / "analytics.db"
REPORT_PATH = OUTPUT_DIR / "analytics_report.xlsx"
CHART_PATH = OUTPUT_DIR / "department_performance.png"
LOG_PATH = LOG_DIR / "pipeline.log"
