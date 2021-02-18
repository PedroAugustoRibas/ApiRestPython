from flask import Flask
from flask_restful import Api
from resources.hotel import Hotel, Hoteis

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database_hotel.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_first_request
def start_database():
    database.create_all()


api.add_resource(Hoteis, '/hoteiss')
api.add_resource(Hotel, '/hoteis', '/hoteis/<int:id_hotel>')

if __name__ == '__main__':
    from config.sql_alchemy import database
    database.init_app(app)
    app.run(debug=True)

