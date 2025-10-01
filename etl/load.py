import pandas as pd
from db_utils import connection, create_table
from sqlalchemy import text

def load_data(df):
    create_table()
    engine = connection()
    
    # Clear existing data before loading
    with engine.begin() as conn:
        conn.execute(text("TRUNCATE TABLE employee_data;"))
    
    # Load fresh data
    df.to_sql("employee_data", engine, index=False, if_exists="append")
    print(f"Loaded {len(df)} records into employee_data table")
        