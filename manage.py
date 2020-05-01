import sys

from flask.cli import FlaskGroup

from project import create_app, db
from project.api.models import Account

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command('seed_db')
def seed_db():
    db.session.add(Account(email="foo@gmail.com", password="foopassword"))
    db.session.add(Account(email="bar@gmail.com", password="barpassword"))
    db.session.commit()

@cli.command('db')

def init():
    init

def migrate():
    migrate

def upgrade():
    upgrade

if __name__ == '__main__':
    cli()