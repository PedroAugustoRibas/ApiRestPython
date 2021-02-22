from flask import Flask
from flask_restful import Api
from resources.hotel import Hotel
from flasgger import Swagger
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database_hotel.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Hotel Project',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
})
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
docs = FlaskApiSpec(app)
api = Api(app)


@app.before_first_request
def start_database():
    database.create_all()


api.add_resource(Hotel, '/hoteis', '/hotel/<int:id_hotel>')
docs.register(Hotel)

if __name__ == '__main__':
    from config.sql_alchemy import database
    database.init_app(app)
    app.run(debug=True)

