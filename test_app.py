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

def test_get_metrics():
    response = client.get("/metrics")

    assert response.status_code == 200

    data = response.json()

    assert "count" in data
    assert isinstance(data["count"], int)


def test_metrics_count_increases_after_time_request():
    before = client.get("/metrics").json()["count"]

    response = client.get("/time")
    assert response.status_code == 200

    after = client.get("/metrics").json()["count"]

    assert after == before + 1
