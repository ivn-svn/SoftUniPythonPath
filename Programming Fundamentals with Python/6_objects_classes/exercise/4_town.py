class Town:
    def __init__(self, name: str):
        self.name = name
        self.longitude = "0°E"
        self.latitude = "0°N"

    def set_latitude(self, lat):
        self.latitude = lat

    def set_longitude(self, long):
        self.longitude = long


    def __repr__(self):
        return "Town: {} | Latitude: {} | Longitude: {}".format(self.name, self.latitude, self.longitude)

town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)