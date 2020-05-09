import json


def test_ping(test_app):
    client = test_app.test_client()
    resp = client.get("/api/v1/ping")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert "success" in data["status"]
    assert "system up and running" in data["message"]
    assert "api_version" in data
    assert "1.0.0" in data["api_version"]
    assert "1.0.1" not in data["api_version"]
