import os

from databases import Database

from sqlalchemy import Column, DateTime, Integer, JSON, MetaData, String, Table, create_engine, Float
from sqlalchemy.sql import func


DATABASE_URL = os.getenv('DATABASE_URL')


# SQLAlchemy
engine = create_engine(DATABASE_URL)


metadata = MetaData()
dummy_predictions = Table(
    "dummy_predictions",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("gender", Integer),
    Column("age", Integer),
    Column("bmi", Float),
    Column("outcome", String(50)),
    Column("datetime", DateTime, default=func.now(), nullable=False),
)


# databases query builder
database = Database(DATABASE_URL)
