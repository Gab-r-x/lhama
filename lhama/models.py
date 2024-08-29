from .ext.database import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.dialects.postgresql import JSON  # ou use `db.JSON` se não estiver usando PostgreSQL


class Contract(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    contract_name = db.Column(db.String(140))
    started_at = db.Column(db.DateTime)
    finished_at = db.Column(db.DateTime)

class Project(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    proj_name = db.Column(db.String(140))
    proj_desc = db.Column(db.String(512))
    contract_id = db.Column(db.Integer)
    started_at = db.Column(db.DateTime)
    finished_at = db.Column(db.DateTime)

class Step(db.Model, SerializerMixin):
    datetime_format = '%Y %b %d %H:%M:%S.%f'

    id = db.Column(db.Integer, primary_key=True)
    step_name = db.Column(db.String(140))
    step_desc = db.Column(db.String(512))
    started_at = db.Column(db.DateTime)
    finished_at = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean, default=False)
    status = db.Column(db.String(140))
    data = db.Column(db.Text)
    project_id = db.Column(db.Integer)

    
class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(140))
    password = db.Column(db.String(512))