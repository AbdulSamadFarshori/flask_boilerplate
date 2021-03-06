from flask_restplus import Api
from flask import Blueprint
from application.apis.login.controller.controller import nsApi as nslogin
from application.apis.registration.controller.controller import nsApi as nsregistration
from application.apis.scanner.controller.amazon import nsApi as nsamazon
blueprint = Blueprint("api", __name__)
api = Api(blueprint,
        title='API',
        version="1.0",
        description="-",
        doc="/doc")

api.add_namespace(nslogin, path="/login")
api.add_namespace(nsregistration, path="/registration")
api.add_namespace(nsamazon, path="/amazon")