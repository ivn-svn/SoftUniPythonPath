# https://judge.softuni.org/Contests/Practice/Index/1943#0

from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass

    @property
    @abstractmethod
    def AC_consumption(self):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        consumption = self.fuel_consumption + self.AC_consumption
        needed_fuel = distance * consumption
        if needed_fuel > self.fuel_quantity:
            return False
        self.fuel_quantity -= needed_fuel
        return True

    def refuel(self, fuel):
        self.fuel_quantity += fuel

    @property
    def AC_consumption(self):
        return 0.9


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        consumption = self.fuel_consumption + self.AC_consumption
        needed_fuel = distance * consumption
        if needed_fuel > self.fuel_quantity:
            return False
        self.fuel_quantity -= needed_fuel
        return True

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95

    @property
    def AC_consumption(self):
        return 1.6
