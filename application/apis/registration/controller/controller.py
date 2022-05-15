from flask import request
from flask_restplus import Namespace, Resource, reqparse
from application.apis.registration.service.service import user_register

nsApi = Namespace("registration", description="registration related operations")

@nsApi.route("/registration")
class registration(Resource):
    @nsApi.doc("post request save data")
    def post(self):
        parser = reqparse.RequestParse()
        parser.add_argument("username", type=str)
        parser.add_argument("password", type=str)
        args = parser.parse_agrs()
        data = user_register(args.username, args.password)
        if data:
            return {"msg":"user register successfully"}
        return {"msg":"fail"}


