from flask_restplus import Namespace, Resource, reqparse
from application.apis.login.service.service import authentication
from flask import request

nsApi = Namespace('login', description='login operations')
#ApiModel = Api.model("User", User.schema())

@nsApi.route('/login')
class login(Resource):
    @nsApi.doc('verify the user')
    #@Api.marshal_with(ApiModelList)
    # @errorHandler
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str)
        parser.add_argument('password', type=str)
        args = parser.parse_args()
        result = authentication(args.username, args.password)
        return {"msg":result}



