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
        hotels = HotelModel.get_all_hotels()
        if hotels:
            return {'message': 'The table is empty'}, 400
        return hotels, 200

    def post(self):
        # if HotelModel.find_hotel(id_hotel):
        #     return {'message': 'Hotel id "{}" already exists.'.format(id_hotel)}, 400
        data = Hotel.params.parse_args()
        hotel = HotelModel(**data)
        hotel.save_hotel()
        return hotel.json(), 201

    def put(self, id_hotel):
        pass

    def delete(self, id_hotel):
        pass


