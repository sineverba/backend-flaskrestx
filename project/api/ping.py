from flask_restx import Namespace, Resource

ping_namespace = Namespace("ping")


class Ping(Resource):
    def get(self):
        return {
            "status": "success",
            "message": "system up and running",
            "api_version": "0.1.0"
        }


ping_namespace.add_resource(Ping, "")
