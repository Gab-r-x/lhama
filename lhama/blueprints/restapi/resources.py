from flask import abort, jsonify
from flask_restful import Resource

from ...models import Project, Step


class ProjectResource(Resource):
    def get(self):
        projects = Project.query.all() or abort(204)
        return jsonify(
            {"projects": [project.to_dict() for project in projects]}
        )

class ProjectItemResource(Resource):
    def get(self, project_id):
        project = Project.query.filter_by(id=project_id).first() or abort(404)
        return jsonify(project.to_dict()
        )
    
class StepResource(Resource):
    def get(self):
        steps = Step.query.all() or abort(204)
        return jsonify(
            {"steps": [step.to_dict() for step in steps]}
        )

class StepItemResource(Resource):
    def get(self, step_id):
        step = Step.query.filter_by(id=step_id).first() or abort(404)
        return jsonify(step.to_dict()
        )