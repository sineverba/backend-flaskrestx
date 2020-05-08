from flask import request
from flask_restx import Namespace, Resource, fields

from project.api.v1.accounts.crud import get_account_by_email

from project import bcrypt


auth_namespace = Namespace("auth")

login = auth_namespace.model(
    "Account",
    {"email": fields.String(required=True), "password": fields.String(required=True)},
)


class Login(Resource):
    @auth_namespace.expect(login, validate=True)
    def post(self):
        post_data = request.get_json()
        email = post_data.get("email")
        password = post_data.get("password")
        response_object = {}

        account = get_account_by_email(email)
        if not account or not bcrypt.check_password_hash(account.password, password):
            auth_namespace.abort(404, "User does not exists")
        response_object = {"access_token": "123456789", "refresh_token": "987654321"}
        return response_object, 200


auth_namespace.add_resource(Login, "/login")
