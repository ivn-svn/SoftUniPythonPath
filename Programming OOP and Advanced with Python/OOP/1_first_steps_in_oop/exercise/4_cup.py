# Create a class called Cup. Upon initialization, it should receive size (integer) 
# and quantity (an integer representing how much liquid is in it).
# The class should have two methods:
# •	fill(quantity) that will increase the amount of liquid in the cup with 
# the given quantity (if there is space in the cup, otherwise ignore).
# •	status() that will return the amount of free space left in the cup.
# Submit only the class in the judge system. Do not forget to test your code.
# 



class Cup: 
    def __init__(self, size, quantity):
        self.size = int(size)
        self.quantity = int(quantity)
    def fill(self, fill_quantity):
        self.fill_quantity = int(fill_quantity)
        if self.quantity + self.fill_quantity < self.size: 
            self.quantity += self.fill_quantity

    def status(self):
        left = self.size - self.quantity
        return left 

cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
