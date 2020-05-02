import json
from datetime import datetime


import project.api.accounts


def test_add_account(test_app, monkeypatch):
    def mock_get_account_by_email(email):
        return None

    def mock_add_account(email, password):
        return True

    monkeypatch.setattr(
        project.api.accounts, "get_account_by_email", mock_get_account_by_email
    )
    monkeypatch.setattr(project.api.accounts, "add_account", mock_add_account)

    client = test_app.test_client()
    resp = client.post(
        "/api/v1/accounts",
        data=json.dumps({"email": "info@example.com", "password": "mypassword"}),
        content_type="application/json",
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 201
    assert "info@example.com registered" in data["message"]


def test_all_accounts(test_app, monkeypatch):
    def mock_get_all_accounts():
        return [
            {
                "id": 1,
                "email": "user@example.com",
                "password": "mysecretpassword",
                "created_at": datetime.now(),
            },
            {
                "id": 2,
                "email": "info@example.com",
                "password": "anothersecretpassword",
                "created_at": datetime.now(),
            },
        ]

    monkeypatch.setattr(project.api.accounts, "get_all_accounts", mock_get_all_accounts)
    client = test_app.test_client()
    resp = client.get("/api/v1/accounts")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert len(data) == 2
    assert "user@example.com" in data[0]["email"]
    assert "info@example.com" in data[1]["email"]
