class Animal:
    def __init__(self, __name):
        self.__name = __name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(self.value) < 2:
            raise ValueError("Cannot set name less than 2 chars")
        self.__name = value
c = Animal(input())

print(str(c.name))