import types


class Vehicle:
    def __init__(self, type, model, price, owner=None):
        self.type = type
        self.model = model
        self.price = price
    def buy(self, money: int, owner: str):
        if money > self.price and owner == None:
            change = money - self.price 
            self.owner = owner
            return "Successfully bought a {}. Change: {}".format(self.type, self.change)
        elif money < self.price and owner == None:
            return "Sorry, not enough money"
        elif self.owner != None:
            return "Car already sold"
    def sell():
        if owner != None:
            owner = None
        else:
            return "Vehicle has no owner"
    def __repr__():
        if owner != None:
            "Vehicle has no owner {model} {type} is owned by: {owner}"
        else:
            return "{model} {type} is on sale: {price}"
vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)