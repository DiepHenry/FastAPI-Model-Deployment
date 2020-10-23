from app.api.models import DummyRow
from app.db import database, dummy_predictions


# Load model inputs and outputs to Postgres
async def post_dummy_predict(payload: DummyRow):
    query = dummy_predictions.insert().values(
        gender=payload["gender"],
        age=payload["age"],
        bmi=payload["bmi"],
        outcome=payload["outcome"]
    )
    return await database.execute(query=query)