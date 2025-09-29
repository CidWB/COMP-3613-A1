from App.controllers.user import create_user
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    create_user("tom", 'bobpass', 'bob@example.com')
