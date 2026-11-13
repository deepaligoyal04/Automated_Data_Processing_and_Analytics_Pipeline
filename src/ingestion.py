import logging
from pathlib import Path
import pandas as pd

def load_files(input_dir: Path) -> pd.DataFrame:
    """Read all CSV and Excel files and combine them into one dataframe."""
    frames = []
    for path in sorted(input_dir.iterdir()):
        try:
            suffix = path.suffix.lower()
            if suffix == ".csv":
                df = pd.read_csv(path)
            elif suffix in (".xlsx", ".xls"):
                df = pd.read_excel(path)
            else:
                continue
            df["source_file"] = path.name
            frames.append(df)
            logging.info("Loaded %s (%s rows)", path.name, len(df))
        except Exception:
            logging.exception("Failed to load file: %s", path.name)
    if not frames:
        raise FileNotFoundError(f"No readable CSV/Excel files found in {input_dir}")
    return pd.concat(frames, ignore_index=True, sort=False)
