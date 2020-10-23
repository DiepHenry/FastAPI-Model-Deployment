from pydantic import BaseModel
from datetime import datetime


class DummyInputs(BaseModel):
    gender: int
    age: int
    bmi: float


class DummyRow(BaseModel):
    gender: int
    age: int
    bmi: float
    outcome: str