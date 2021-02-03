from flask_restful import Resource, reqparse
from models.hotel import HotelModel

class Hoteis(Resource):
    def get(self):
        return "hotels"


class Hotel(Resource):
    params = reqparse.RequestParser()
    params.add_argument('name')
    params.add_argument('stars')
    params.add_argument('hotel_night')
    params.add_argument('city')

    def get(self, id_hotel):
        hotel = HotelModel.find_hotel(id_hotel)
        if hotel:
            return hotel.json()
        return {'message': 'Hotel not found'}, 400

    def post(self, id_hotel=None):
        data = Hotel.params.parse_args()
        hotel = HotelModel(**data)
        hotel.save_hotel()
        return hotel.json(), 201

    def put(self, id_hotel):
        pass

    def delete(self, id_hotel):
        pass


