import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_time():
    response = client.get("/time")
    assert response.status_code == 200
    data = response.json()
    assert "time" in data
    assert isinstance(data["time"], int)
    assert data["time"] > 0
