from starlette.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_welcome(test_app):
    response = test_app.get("/welcome")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the API"}