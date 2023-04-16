from abc import ABC, abstractmethod

class Supply(ABC):
    def __init__(self, name: str, energy: int):
        self.name = name
        self.energy = energy

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if value == "":
            raise ValueError("Name cannot be an empty string.")
        self.__name = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        if value < 0:
            raise ValueError("Energy cannot be less than zero.")
        self.__energy = value

    # This decorator marks the method as abstract, ensuring the class cannot be instantiated
    @abstractmethod
    def details(self) -> str:
        ...
