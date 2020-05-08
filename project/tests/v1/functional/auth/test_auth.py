import json
from project.api.models import Account


# Test user can do login
def test_user_can_do_login(test_app, test_database, add_account):

    # Delete all
    test_database.session.query(Account).delete()

    # Add new account
    add_account("info@example.com", "passwordforlogin")

    # Prepare Client
    client = test_app.test_client()

    payload = {"email": "info@example.com", "password": "passwordforlogin"}

    # Make request
    resp = client.post(
        "/api/v1/auth/login", data=json.dumps(payload), content_type="application/json"
    )

    # Read answer
    data = json.loads(resp.data.decode())

    assert resp.status_code == 200
    assert data["access_token"]
    assert data["refresh_token"]


# Test user can do login
def test_user_with_wrong_password_cannot_do_login(test_app, test_database, add_account):

    # Delete all
    test_database.session.query(Account).delete()

    # Add new account
    add_account("info@example.com", "passwordforlogin")

    # Prepare Client
    client = test_app.test_client()

    payload = {"email": "info@example.com", "password": "passwordforloginwrong"}

    # Make request
    resp = client.post(
        "/api/v1/auth/login", data=json.dumps(payload), content_type="application/json"
    )

    # Read answer
    data = json.loads(resp.data.decode())

    assert resp.status_code == 404
    assert "access_token" not in data
    assert "refresh_token" not in data
