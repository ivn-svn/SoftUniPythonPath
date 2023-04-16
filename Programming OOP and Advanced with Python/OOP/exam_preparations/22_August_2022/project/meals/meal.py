from abc import ABC, abstractmethod


class Meal(ABC):
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not value:
            raise ValueError("Name cannot be an empty string!")
        self._name = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        if value <= 0.0:
            raise ValueError("Invalid price!")
        self._price = value

    def details(self) -> str:
        return f"Name: {self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def __str__(self):
        return f"Meal(name={self.name}, price={self.price}, quantity={self.quantity})"
