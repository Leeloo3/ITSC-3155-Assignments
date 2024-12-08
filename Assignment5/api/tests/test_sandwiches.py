from fastapi.testclient import TestClient
from ..controllers import sandwiches
from ..main import app
import pytest
from ..models import models

client = TestClient(app)

@pytest.fixture
def db_session(mocker):
    return mocker.Mock()

def test_create_sandwich(db_session):
    sandwich_data = {
        "sandwich_name": "Club Sandwich",
        "price": 5.99
    }
    response = client.post("/sandwiches/", json=sandwich_data)
    assert response.status_code == 200
    assert response.json()["sandwich_name"] == "Club Sandwich"

def test_read_sandwiches(db_session):
    response = client.get("/sandwiches/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_one_sandwich(db_session):
    response = client.get("/sandwiches/1")
    assert response.status_code == 200

def test_update_sandwich(db_session):
    update_data = {
        "sandwich_name": "Updated Sandwich",
        "price": 6.99
    }
    response = client.put("/sandwiches/1", json=update_data)
    assert response.status_code == 200

def test_delete_sandwich(db_session):
    response = client.delete("/sandwiches/1")
    assert response.status_code == 204 