from flask import Blueprint
from flask_restful import Api

from .resources import ProjectItemResource, ProjectResource, StepItemResource, StepResource, ContractResource, ContractItemResource

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app):
    api.add_resource(ContractResource, "/contract/")
    api.add_resource(ContractItemResource, "/contract/<contract_id>")
    api.add_resource(ProjectResource, "/project/")
    api.add_resource(ProjectItemResource, "/project/<project_id>")
    api.add_resource(StepResource, "/step/")
    api.add_resource(StepItemResource, "/step/<step_id>")

    app.register_blueprint(bp)