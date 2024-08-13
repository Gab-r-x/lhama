from .ext.database import db
from sqlalchemy_serializer import SerializerMixin


class Pixel(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    x = db.Column(db.Integer, nullable=False)
    y = db.Column(db.Integer, nullable=False)
    collor = db.Column(db.String(7))
    alt_text = db.Column(db.Text(255), nullable=True)
    wallet = db.Column(db.String(255), nullable=True)


class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(140))
    password = db.Column(db.String(512))