from starlette.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_dummy_predict(test_app):
    endpoint = "/dummy/v0.0/predict"
    data = {
        "gender": 1,
        "age": 30,
        "bmi": 24.6
    }
    response = test_app.post(endpoint, json=data)
    assert response.status_code == 200
    assert response.json() == {"prediction": "approved"}
