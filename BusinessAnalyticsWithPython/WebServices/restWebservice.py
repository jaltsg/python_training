from flask import Flask
from flask import request
from flask_restplus import Api, Resource, fields
from flask_restplus import reqparse

app = Flask(__name__)

# basic documentation
api = Api(app, version='0.1', title='BA API',
    description='A simple BA API',
)

ns = api.namespace('webservices', description='BA webservices')

# create a data object to define inputs required for a rest call
hello_post_inputs = reqparse.RequestParser()
hello_post_inputs.add_argument("name", type=str, required=True)


myName  = "Michael"

@ns.route('/hello')
class BA_WS(Resource):
    # note the function names get/put/post/delete are all restful service names
    def get(self):
        return "hello " + str(whoami())

    @ns.expect(hello_post_inputs)
    def post(self):
        # global tells the function to use the global scope of the variable myName
        global myName
        args = hello_post_inputs.parse_args(request)
        newNameString = args['name']
        if newNameString:
            myName = newNameString
        return "Success"


def whoami():
    return myName

if __name__ == '__main__':
    app.run(debug=True,port=9999)
