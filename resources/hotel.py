from flask_restful import Resource, reqparse

hotels = [{'id': 1, 'name': 'hotel 1'}, {'id': 2, 'name': 'hotel 2'}, {'id': 3, 'name': 'hotel 3'}]


class Hoteis(Resource):
    def get(self):
        return hotels


class Hotel(Resource):

    def get(self, id_hotel):
        for hotel in hotels:
            if hotel['id'] == id_hotel:
                return hotel
        return {'message': 'Hotel not found'}, 404

    def post(self, id_hotel):
        params = reqparse.RequestParser()
        params.add_argument('name')
        data = params.parse_args()

        new_hotel = {
            'id': id_hotel,
            'name': data['name']
        }
        hotels.append(new_hotel)
        return 'Hotel criado com sucesso!'

    def put(self, id_hotel):
        pass

    def delete(self, id_hotel):
        pass
