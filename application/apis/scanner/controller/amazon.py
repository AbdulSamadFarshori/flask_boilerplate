from flask_restplus import Namespace, Resource, reqparse
from flask import request
from application.apis.scanner.service.amazon import run_amazon_scanner

nsApi = Namespace('amazon', description='amazon operations')
#ApiModel = Api.model("User", User.schema())

@nsApi.route('/fetch-data')
class GetAmazonData(Resource):
    @nsApi.doc('run bot that fetch data')
    #@Api.marshal_with(ApiModelList)
    # @errorHandler
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('pages', type=int)
        parser.add_argument('search_keyword', type=str)
        args = parser.parse_args()
        data = run_amazon_scanner(args.search_keyword, args.pages)
        return {"msg":data}