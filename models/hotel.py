class HotelModel:
    # def __init__(self, id, name, stars, hotel_night, city):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        # self.stars = stars
        # self.hotel_night = hotel_night
        # self.city = city

    def json(self):
        return {
                'id': self.id,
                'name': self.name
                # 'stars': self.stars,
                # 'hotel_night': self.hotel_night,
                # 'city': self.city
              }
