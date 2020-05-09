from flask_restx import Namespace, Resource

from flask import current_app

ping_namespace = Namespace("ping")


class Ping(Resource):
    def get(self):
        return {
            "status": "success",
            "message": "system up and running",
            "api_version": current_app.config["APP_VERSION"],
        }


ping_namespace.add_resource(Ping, "")
