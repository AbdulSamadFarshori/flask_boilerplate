from application import db
from application.core.db.models.base import Base
from application import marshmallow




class User(Base):
    username = db.Column(db.String(255), nullable=False)
    password = usename = db.Column(db.String(255), nullable=False)

class UserSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_fk = True 

