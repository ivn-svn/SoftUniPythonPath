# •	In the fruit.py file, create a class called Fruit with will
# receive a name (str) and an expiration_date (str) upon initialization.
# Fruit should inherit from Food.
# Submit in Judge a zip file of the folder project.
from food import Food

class Fruit (Food):
    def _init__(self, name, expiration_date):
        super().__init__(expiration_date)
        self.name = name