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

    assert len(data) == 2
    assert "username" in data[1]["email"]
    assert "password" in data[1]["password"]
    assert "anotherusername" in data[0]["email"]
    assert "anotherpassword" in data[0]["password"]
