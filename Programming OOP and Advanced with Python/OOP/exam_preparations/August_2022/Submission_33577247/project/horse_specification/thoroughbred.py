from project.horse_specification.horse import Horse

class Thoroughbred(Horse):
    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def get_max_speed(self):
        return 140

    def get_speed_increase(self):
        return 3
