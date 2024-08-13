from flask import abort, jsonify
from flask_restful import Resource

from ...models import Pixel


class PixelResource(Resource):
    def get(self):
        pixels = Pixel.query.all() or abort(204)
        return jsonify(
            {"pixels": [pixel.to_dict() for pixel in pixels]}
        )


class PixelItemResource(Resource):
    def get(self, pixel_id):
        pixel = Pixel.query.filter_by(id=pixel_id).first() or abort(404)
        return jsonify(pixel.to_dict())