from flask import Blueprint
from flask_restful import Api

from .resources import PixelItemResource, PixelResource

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app):
    api.add_resource(PixelResource, "/pixel/")
    api.add_resource(PixelItemResource, "/pixel/<pixel_id>")
    app.register_blueprint(bp)