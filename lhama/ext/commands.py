import click
from .database import db
from .auth import create_user
from ..models import Project, Step
from datetime import datetime


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""

    
    new_project = Project(proj_name="Primeiro Projeto", proj_desc="Esse é o primeiro projeto da aplicação Lhama que permite que empresas controlem o fluxo de processos de forma rápida e acessivel", started_at=datetime(2024, 8, 19, 13, 0, 0), finished_at=datetime(2024, 8, 19, 15, 0, 0)),
    
    step1 = Step(
            id=1,
            step_name="Briefing com cliente",
            step_desc="Processo 01 Description",
            started_at=datetime(2024, 8, 19, 13, 0, 0),
            finished_at=datetime(2024, 8, 19, 15, 0, 0),
            is_active=False,
            data='"Recurso": "R$5milhoes", "Fonte": "Governo do Estado", "Área": "550m²", "Projeto":"https:americalatina.eng.br"', 
            project_id=1
        )

    step2 = Step(
            id=2,
            step_name="Processo 02",
            step_desc="Processo 02 Description",
            started_at=datetime(2024, 8, 20, 13, 0, 0),
            finished_at=datetime(2024, 8, 20, 15, 0, 0),
            is_active=False,
            data='"Recurso": "R$8milhoes", "Fonte": "Recurso Prefeitura"', 
            project_id=1
        )    

    step3 = Step(
            id=3,
            step_name="Processo 03",
            step_desc="Processo 03 Description",
            started_at=datetime(2024, 8, 20, 13, 0, 0),
            finished_at=datetime(2024, 8, 20, 15, 0, 0),
            is_active=True,
            data='"Link do projeto": "https://americalatina.eng.br", "Link da planilha": "https://americalatina.eng.br"', 
            project_id=1
        )    
    
    db.session.bulk_save_objects(new_project)
    db.session.add(step1)
    db.session.add(step2)
    db.session.add(step3)
    db.session.commit()
    return Project.query.all()


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