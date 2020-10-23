import os
import pandas as pd
from databases import Database
from sqlalchemy import create_engine

def connect_to_postgres():
    DATABASE_URL = os.getenv('DATABASE_URL')
    return create_engine(DATABASE_URL)

def get_postgres_data(query, engine):
    table_data = pd.read_sql(
        query,
        con=engine
    )
    table_data.datetime = table_data.datetime.dt.tz_localize('utc').dt.tz_convert('US/Pacific')
    return table_data