from fastapi import FastAPI, Request

from app.api import welcome, crud, dummy_predict
from app.db import engine, metadata, database


metadata.create_all(engine)

app = FastAPI(openapi_url="/dummy/v0.0/predict/openapi.json", docs_url="/dummy/v0.0/predict/docs")


# Start and stop connection to Postgres
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconect()


app.include_router(welcome.router, prefix="/welcome", tags=["test"])
app.include_router(dummy_predict.router, prefix="/dummy/v0.0", tags=["dummy_model"])
