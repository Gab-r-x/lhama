import click
from .database import db
from .auth import create_user
from ..models import Pixel


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""
    data = [
        Pixel(id=1, x=1, y=1, collor="#FFFFFF", alt_text="Pixel 01", wallet="123"),
        Pixel(id=2, x=2, y=1, collor="#FFFFFF", alt_text="Pixel 02", wallet="123"),
        Pixel(id=3, x=3, y=1, collor="#FFFFFF", alt_text="Pixel 03", wallet="123"),

    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return Pixel.query.all()


def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))

    # add a single command
    @app.cli.command()
    @click.option('--username', '-u')
    @click.option('--password', '-p')
    def add_user(username, password):
        """Adds a new user to the database"""
        return create_user(username, password)