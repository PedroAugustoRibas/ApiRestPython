from flask_restful import Resource, reqparse
from models.hotel import HotelModel

hotels = [{'id': 1, 'name': 'hotel 1'}, {'id': 2, 'name': 'hotel 2'}, {'id': 3, 'name': 'hotel 3'}]


class Hoteis(Resource):
    def get(self):
        return hotels

class Hotel(Resource):
    params = reqparse.RequestParser()
    params.add_argument('name')

    def get(self, id_hotel):
        hotel = Hotel.find_hotel(id_hotel)
        if hotel:
            return hotel
        return {'message': 'Hotel not found'}, 404

    def post(self, id_hotel):
        data = Hotel.params.parse_args()
        hotel_object = HotelModel(id_hotel, **data)
        new_hotel = hotel_object.json()
        hotels.append(new_hotel)
        return {'message': 'Hotel successfully created!'}, 201

    def put(self, id_hotel):
        data = Hotel.params.parse_args()
        hotel = Hotel.find_hotel(id_hotel)
        hotel_object = HotelModel(id_hotel, **data)
        new_hotel = hotel_object.json()
        if hotel:
            hotel.update(new_hotel)
            return new_hotel, 200
        hotels.append(new_hotel)
        return new_hotel, 201

    def delete(self, id_hotel):
        hotel = Hotel.find_hotel(id_hotel)
        if hotel:
            hotels.remove(hotel)
            return "Successfully deleted", 200
        return "Hotel not found", 404

    def find_hotel(id_hotel):
        for hotel in hotels:
            if hotel['id'] == id_hotel:
                return hotel
        return None
