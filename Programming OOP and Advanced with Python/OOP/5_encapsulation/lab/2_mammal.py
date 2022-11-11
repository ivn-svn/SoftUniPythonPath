class Mammal:
    __kingdom = "animals"

    def __init__(self, name, type, sound):
        self.name = name
        self.type = type
        self.sound = sound

    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self):
        return self.__kingdom

    def info(self):
        return f"{self.name} is of type {self.type}"


# Video watched up to: +01:07:00 :
# https://softuni.bg/trainings/resources/video/73677/video-07-july-2022-ines-ivanova-kenova-python-oop-june-2022/3705

# https://www.tutorialsteacher.com/python/public-private-protected-modifiers