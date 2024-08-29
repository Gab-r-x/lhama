from flask import Flask, render_template
import json

from .ext import configuration


def minimal_app(**config):
    app = Flask(__name__)
    configuration.init_app(app, **config)
    return app


def create_app(**config):
    app = minimal_app(**config)
    configuration.load_extensions(app)
    
    @app.route('/projetos/<int:project_id>')
    def index(project_id):
        return render_template('index.html', project_id=json.dumps(project_id))

    @app.route('/projetos/')
    def projects():
        return render_template('projects.html')
    return app
