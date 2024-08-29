import click
from .database import db
from .auth import create_user
from ..models import Project, Step, Contract
from datetime import datetime


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""
    
    contract1 = Contract(
            contract_name="ALE-001",
            started_at=datetime(2024, 8, 19, 13, 0, 0),
            finished_at=datetime(2024, 8, 19, 15, 0, 0)
        )
    
    contract2 = Contract(
            contract_name="ALE-002",
            started_at=datetime(2024, 8, 19, 13, 0, 0),
            finished_at=datetime(2024, 8, 19, 15, 0, 0)
        )
    
    project1 = Project(
            proj_name="Primeiro Projeto",
            proj_desc="Esse é o primeiro projeto da aplicação Lhama que permite que empresas controlem o fluxo de processos de forma rápida e acessivel",
            contract_id=1,
            started_at=datetime(2024, 8, 19, 13, 0, 0),
            finished_at=datetime(2024, 8, 19, 15, 0, 0)
        )
    
    project2 = Project(
            proj_name="Segundo Projeto",
            proj_desc="Esse é o primeiro projeto da aplicação Lhama que permite que empresas controlem o fluxo de processos de forma rápida e acessivel",
            contract_id=2,
            started_at=datetime(2024, 8, 19, 13, 0, 0),
            finished_at=datetime(2024, 8, 19, 15, 0, 0)
        )
    
    step1 = Step(
            step_name="Briefing com cliente",
            step_desc="Desenvolver com o cliente as necessidades do contrato como programa de necessidades, manuais de referência, informações adicionais como recurso, fonte e etc...",
            is_active=False,
            status='Não Iniciado',
            data='', 
            project_id=1
        )

    step2 = Step(
            step_name="Apresentação do BEP",
            step_desc="Apresentação do BIM Execution Plan",
            is_active=False,
            status='Não Iniciado',
            data='', 
            project_id=1
        )    

    step3 = Step(
            step_name="Levantamento / Topografia",
            step_desc="Armazenar os dados sobre levantamento e topografia",
            is_active=False,
            status='Não Iniciado',
            data='', 
            project_id=2
        )    
    
    db.session.add(contract1)
    db.session.add(contract2)
    db.session.add(project1)
    db.session.add(project2)

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