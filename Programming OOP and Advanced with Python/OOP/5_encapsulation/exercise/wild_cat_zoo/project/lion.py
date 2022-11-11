from project.animal import Animal


class Lion(Animal):
    DEFAULT_MONEY_4_CARE = 50

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, self.DEFAULT_MONEY_4_CARE)
