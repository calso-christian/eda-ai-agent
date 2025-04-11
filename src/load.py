import pandas as pd
from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine, inspect

def load_data(path, db_name, table_name):
    df = pd.read_excel(path)

    db_name="performance"

    engine=create_engine(f"sqlite:///{db_name}.db")

    inspector = inspect(engine)
    table_names = inspector.get_table_names()

    table_name="detalized" # Change to Desired Table Name

    if "detalized" not in table_names:
        
        df.to_sql(table_name, engine, index=False)
        print(f"Table {table_name} has been created in {db_name} database\n\n")
    else:
        print(f"Table {table_name} already exists in {db_name} database\nSkipping...\n\n")

    db=SQLDatabase(engine=engine)

    return db
    
