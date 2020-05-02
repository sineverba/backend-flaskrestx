import json
from project.api.models import Account


# Get all accounts
def test_can_get_all_account(test_app, test_database, add_account):

    # Delete all
    test_database.session.query(Account).delete()

    # Add new account

    add_account("username", "password")
    add_account("anotherusername", "anotherpassword")

    client = test_app.test_client()

    resp = client.get("/api/v1/accounts")
    data = json.loads(resp.data.decode())

    assert resp.status_code == 200

    assert len(data["data"]) == 2
    assert "username" in data["data"][1]["email"]
    assert "anotherusername" in data["data"][0]["email"]
    assert "password" not in data["data"][0]


# Test that new account has deleted at null as field
def test_new_account_has_deleted_at_null(test_app, test_database, add_account):
    test_database.session.query(Account).delete()

    # Add new account
    add_account("username", "password")
    client = test_app.test_client()

    resp = client.get("/api/v1/accounts")
    data = json.loads(resp.data.decode())

    assert resp.status_code == 200
    assert len(data["data"]) == 1
    assert "username" in data["data"][0]["email"]
    assert "password" not in data["data"][0]
    assert data["data"][0]["created_at"] is not None
    assert data["data"][0]["updated_at"] is not None


# Test can add new account
def test_can_add_new_account(test_app, test_database):
    test_database.session.query(Account).delete()

    client = test_app.test_client()

    payload = {"email": "info@example.com", "password": "password"}
    resp = client.post(
        "/api/v1/accounts", data=json.dumps(payload), content_type="application/json"
    )
    assert resp.status_code == 201


# Test cannot add new account if exists
def test_cannot_add_new_account_if_exists(test_app, test_database, add_account):
    test_database.session.query(Account).delete()

    add_account("info@example.com", "password")
    client = test_app.test_client()

    payload = {"email": "info@example.com", "password": "password"}
    resp = client.post(
        "/api/v1/accounts", data=json.dumps(payload), content_type="application/json"
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert "Sorry. That email already exists." == data["message"]
