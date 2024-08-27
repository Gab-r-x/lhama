from flask import abort, jsonify, request, make_response
from flask_restful import Resource

from ...models import Project, Step
from ...ext.database import db
from datetime import datetime


class ProjectResource(Resource):
    def get(self):
        projects = Project.query.all() or abort(204)
        return jsonify(
            {"projects": [project.to_dict() for project in projects]}
        )
    def post(self):
        data = request.get_json()
        if not data or not 'proj_name' in data or not 'proj_desc' in data:
            abort(400, description="Project name and description are required.")

        now = datetime.now()
        new_project = Project(
            proj_name = data['proj_name'],
            proj_desc = data['proj_desc'],
            contract = data['contract'],
            started_at = datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
        )
        
        db.session.add(new_project)
        db.session.commit()

        return make_response(jsonify(new_project.to_dict()), 201)    

class ProjectItemResource(Resource):
    def get(self, project_id):
        project = Project.query.filter_by(id=project_id).first() or abort(404)
        return jsonify(project.to_dict()
        )
    def put(self, project_id):
        project = Project.query.filter_by(id=project_id).first() or abort(404)
        
        data = request.get_json()
        if not data:
            abort(400, description="No input data provided.")

        # Atualizar os campos do projeto com base nos dados fornecidos
        project.proj_name = data.get('proj_name', project.proj_name)
        project.proj_desc = data.get('proj_desc', project.proj_desc)

        db.session.commit()  # Salvar as alterações no banco de dados
        return make_response(jsonify(project.to_dict()), 201)    
        
class StepResource(Resource):
    def get(self):
        steps = Step.query.all() or abort(204)
        return jsonify(
            {"steps": [step.to_dict() for step in steps]}
        )
    def post(self):
        data = request.get_json()
        if not data or not 'step_name' in data or not 'step_desc' in data or not 'project_id' in data:
            abort(400, description="Step name, description and project_id are required.")

        now = datetime.now()
        new_step = Step(
            step_name = data['step_name'],
            step_desc = data['step_desc'],
            started_at = datetime(now.year, now.month, now.day, now.hour, now.minute, now.second),
            data = data['data'],
            project_id = data['project_id']
        )
        
        db.session.add(new_step)
        db.session.commit()

        return make_response(jsonify(new_step.to_dict()), 201)    


class StepItemResource(Resource):
    def get(self, step_id):
        step = Step.query.filter_by(id=step_id).first() or abort(404)
        return jsonify(step.to_dict()
        )
    def put(self, step_id):
        step = Step.query.filter_by(id=step_id).first() or abort(404)
        
        data = request.get_json()
        if not data:
            abort(400, description="No input data provided.")

        # Atualizar os campos do projeto com base nos dados fornecidos
        step.proj_name = data.get('step_name', step.step_name)
        step.proj_desc = data.get('step_desc', step.step_desc)
        step.data = data.get('data', step.data)


        db.session.commit()  # Salvar as alterações no banco de dados
        return make_response(jsonify(step.to_dict()), 201)    
