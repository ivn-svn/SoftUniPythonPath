from project.animal import Animal


class Cheetah(Animal):
    DEFAULT_MONEY_4_CARE = 60

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, self.DEFAULT_MONEY_4_CARE)


