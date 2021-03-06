from flask_restx import Api

from project.api.v1.accounts.accounts import accounts_namespace
from project.api.v1.auth.auth import auth_namespace
from project.api.v1.ping.ping import ping_namespace

# Disable totally docs
api = Api(doc=False)
# api = Api(version="1.0", title="Users API", doc="/doc/")

api.add_namespace(ping_namespace, path="/api/v1/ping")
api.add_namespace(accounts_namespace, path="/api/v1/accounts")
api.add_namespace(auth_namespace, path="/api/v1/auth")
