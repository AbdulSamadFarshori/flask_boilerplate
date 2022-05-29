from aenum import Enum
from application import db
from application.core.db.models.base import Base
from application import marshmallow

class PLATFORM(Enum):
	AMAZON = 1
	FLIPKART = 2

class ITEM(Enum):
    MOBILE = 1
    LAPTOP = 2

class Scan(Base):
    name = db.Column(db.String(255))
    price = db.Column(db.Integer)
    platform = db.Column(db.Enum(PLATFORM))
    star = db.Column(db.Float)
    rating = db.Column(db.Integer)
    link = db.Column(db.String(255))
    nb_reviews = db.Column(db.Text)
    description = db.Column(db.Text)
    item = db.Column(db.Enum(ITEM))

class ScanSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Scan
        include_fk = True

