import os
from flask import Flask, g
from datetime import datetime
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func


app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)
marshmallow = Marshmallow(app)

# import models here from core/models
from application.core.db.models.User import User
from application.core.db.models.scan import Scan
#-------------

db.create_all()

# add and register buleprints here
from application.apis import blueprint as apis_blueprint

app.register_blueprint(apis_blueprint, prefix_url="/api")