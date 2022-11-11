class Student:
    def __init__(self, number, id_number):
        self.number = number
        self.__id_number = id_number
        self._grades = [5, 6]
    def calculate_age(self):
        year = self.__id_number[:2]
#
# age = datetime.now() - year