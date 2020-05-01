from flask_restx import Namespace, Resource

ping_namespace = Namespace("ping")


class Ping(Resource):
    def get(self):
        return {
            "status": "success",
            "message": "system up and running",
            "api_version": "0.2.1",
        }


ping_namespace.add_resource(Ping, "")
