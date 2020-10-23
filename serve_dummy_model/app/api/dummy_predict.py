from fastapi import APIRouter
from joblib import load
from pydantic import BaseModel

from app.api import crud
from app.api.models import DummyInputs
from app.db import database, dummy_predictions

router = APIRouter()


clf = load(r"./app/models/d_tree_v00.joblib")


def get_prediction(gender, age, bmi):
    x = [[gender, age, bmi]]
    y = clf.predict(x)[0]
    prob = clf.predict_proba(x)[0].tolist()
    return {"outcome": y}


@router.post("/predict")
async def predict(payload: DummyInputs):
    pred = get_prediction(payload.gender, payload.age, payload.bmi)
    '''
    TODO: Parse endpoint to get model and version to save to Postgres
    '''
    dummy_row = {
        "gender": payload.gender,
        "age": payload.age,
        "bmi": payload.bmi,
        "outcome": str(pred["outcome"])
    }
    await crud.post_dummy_predict(dummy_row)
    return pred
