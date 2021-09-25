from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from config.hotel_schema import HotelResponseSchema, HotelRequestSchema


class Hotel(Resource):
    params = reqparse.RequestParser()
    params.add_argument('name')
    params.add_argument('stars')
    params.add_argument('hotel_night')
    params.add_argument('city')

    # @doc(description='My First GET Awesome API.', tags=['Awesome'])
    # @marshal_with(HotelResponseSchema)  # marshalling
    def get(self, id_hotel=None):
        hotel = HotelModel.find_hotel(id_hotel)
        if hotel:
            return hotel.json(), 200

        return {'message': 'Hotel not found'}, 400

    def post(self):
        data = Hotel.params.parse_args()
        hotel = HotelModel(**data)
        hotel.save_hotel()
        return hotel.json(), 201

    def put(self, id_hotel):
        data = Hotel.params.parse_args()
        hotel_found = HotelModel.find_hotel(id_hotel)
        if hotel_found:
            hotel_found.update_hotel(**data)
            hotel_found.save_hotel()
            return hotel_found.json(), 200
        hotel = HotelModel(**data)
        hotel.save_hotel()
        return hotel.json(), 201

    def delete(self, id_hotel):
        hotel = HotelModel.find_hotel(id_hotel)
        if hotel:
            hotel.delete_hotel()
            return {'message': 'Hotel deleted'}, 200

        return {'message': 'Hotel not found'}, 404


