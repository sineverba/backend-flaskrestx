from flask_restx import Api

from project.api.accounts import accounts_namespace
from project.api.ping import ping_namespace

# Disable totally docs
api = Api(doc=False)
# api = Api(version="1.0", title="Users API", doc="/doc/")

api.add_namespace(ping_namespace, path="/api/v1/ping")
api.add_namespace(accounts_namespace, path="/api/v1/accounts")
