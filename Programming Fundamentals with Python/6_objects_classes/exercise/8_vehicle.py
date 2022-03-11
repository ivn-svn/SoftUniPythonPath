class Vehicle:
    def __init__(self, type, model, price: int, owner=None):
        self.type = type
        self.model = model
        self.price = price
        self.owner = owner

    def buy(self, money: int, owner: str):
        change = 0
        if money >= self.price:
            if self.owner is None:
                change = money - self.price
                self.owner = owner
                pass
            return "Successfully bought a {}. Change: {:0.2f}".format(self.type, change)
        elif money < self.price and self.owner is None:
            return "Sorry, not enough money"
        elif self.owner is not None:
            return "Car already sold"

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner is not None:
            return "{} {} is owned by: {}".format(self.model, self.type, self.owner)
        else:
            return "{} {} is on sale: {}".format(self.model, self.type, self.price)


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)
