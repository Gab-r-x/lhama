from flask import Flask, render_template

from .ext import configuration


def minimal_app(**config):
    app = Flask(__name__)
    configuration.init_app(app, **config)
    return app


def create_app(**config):
    app = minimal_app(**config)
    configuration.load_extensions(app)
    
    @app.route('/')
    def index():
        return render_template('index.html')
    return app
