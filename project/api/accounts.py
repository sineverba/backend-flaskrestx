from flask import request
from flask_restx import Namespace, Resource, fields

# fmt: off
from project.api.crud import (add_account, get_account_by_email,
                              get_all_accounts)

# fmt: on

accounts_namespace = Namespace("accounts")

account = accounts_namespace.model(
    "Account",
    {
        "id": fields.Integer(readOnly=True),
        "email": fields.String(required=True),
        "password": fields.String(required=True),
        "created_at": fields.DateTime,
        "updated_at": fields.DateTime,
        "deleted_at": fields.DateTime,
    },
)


class accountsList(Resource):
    @accounts_namespace.marshal_with(account, as_list=True)
    def get(self):
        """Returns all accounts"""
        return get_all_accounts(), 200  # updated

    @accounts_namespace.expect(account, validate=True)
    def post(self):
        """Create new account"""
        post_data = request.get_json()
        email = post_data.get("email")
        password = post_data.get("password")
        response_object = {}

        account = get_account_by_email(email)
        if account:
            response_object["message"] = "Sorry. That email already exists."
            return response_object, 400
        add_account(email, password)  # new
        response_object["message"] = f"{email} registered!"
        return response_object, 201


accounts_namespace.add_resource(accountsList, "")
