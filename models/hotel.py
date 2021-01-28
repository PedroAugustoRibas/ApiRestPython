from config.sql_alchemy import database


class HotelModel(database.Model):
    __tablename__ = 'hotels'

    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(80))
    starts = database.Column(database.Float(precision=1))
    hotel_night = database.Column(database.Float(precision=2))
    city = database.Column(database.String(40))

    def __init__(self,  name, stars, hotel_night, city):

        self.name = name
        self.stars = stars
        self.hotel_night = hotel_night
        self.city = city

    def json(self):
        return {
                'id': self.id,
                'name': self.name,
                'stars': self.stars,
                'hotel_night': self.hotel_night,
                'city': self.city
              }

    @classmethod
    def find_hotel(cls, id_hotel):
        """Busca pelo hotel na tabela hotels
           Args:
               id_hotel (int): dados que devem ser inseridos na tabela.
           Returns:
                resultado
        """

        hotel = cls.query.filter_by(id=5)
        if hotel:
            return hotel
        return None

    @classmethod
    def get_all_hotels(cls):
        """Pega todos os hoteis do banco
           Args:

           Returns:
                dict
        """

        hotel = cls.query
        if hotel:
            return hotel
        return None

    def save_hotel(self):
        """Salva o dado na tabela de hotels"""

        database.session.add(self)
        database.session.commit()



