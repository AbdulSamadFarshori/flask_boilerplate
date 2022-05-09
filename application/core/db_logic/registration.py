from application import db
from application.core.db.models.User import User

def create_user(username, password):
    obj = User(username=username, password=password)
    db.session.add(obj)
    db.session.commit()
    