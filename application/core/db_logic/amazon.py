from application.core.db.models.scan import Scan
from application import db

def store_amazon_data(data):
    for row in data:
        obj = Scan(**row)
        db.session.add(obj)
        db.session.commit()

def get_scan_item(name):
    obj = Scan.query.filter_by(name=name).all()
    return obj