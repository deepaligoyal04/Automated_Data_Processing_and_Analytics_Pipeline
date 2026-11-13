import sqlite3
import pandas as pd
from .config import DB_PATH

def save_to_sqlite(df: pd.DataFrame, table_name="processed_records"):
    with sqlite3.connect(DB_PATH) as con:
        df.to_sql(table_name, con, if_exists="replace", index=False)
        # Demonstrate SQL retrieval and return records from the stored table.
        retrieved = pd.read_sql_query(f"SELECT * FROM {table_name}", con)
    return retrieved
