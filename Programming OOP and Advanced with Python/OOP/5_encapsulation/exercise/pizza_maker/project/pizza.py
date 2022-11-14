from project.dough import Dough
from project.topping import Topping


class Pizza:
    def __init__(self, name, dough, toppings_capacity):
        self.__name = None
        self.__dough = None
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity

    @property
    def name(self):
        return self.__name

    @name.setter
    def flour_type(self, value):
        if value == "":
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    @property
    def name(self):
        return self.__dough

    @name.setter
    def flour_type(self, value):
        if value is not None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value is not None:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self.__toppings_capacity = value

    def add_topping(self, topping: Topping):
        if len(self.toppings) == self.toppings_capacity:
            raise ValueError("Not enough space for another topping")
        if topping.topping_type in self.toppings:
            self.toppings[topping.topping_type] += topping.weight
        else:
            self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        total_weight = sum(self.toppings.values()) + self.dough.weight
        return total_weight
