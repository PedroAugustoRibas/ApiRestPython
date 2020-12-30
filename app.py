from flask import Flask
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)


class Hostel(Resource):

    def get(self):
        return {'hosteis': 'meus hoteis'}


api.add_resource(Hostel, '/hoteis')

if __name__ == '__main__':
    app.run(debug=True)

 # http://127.0.0.1:5000/