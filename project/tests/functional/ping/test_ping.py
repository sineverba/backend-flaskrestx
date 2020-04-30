import json


def test_ping(test_app):
    client = test_app.test_client()
    resp = client.get("/api/v1/ping")
    data = json.loads(resp.data.decode())
    structure_data = json.loads(resp.data)
    assert resp.status_code == 200
    assert "success" in data["status"]
    assert "system up and running" in data["message"]
    assert "api_version" in structure_data
