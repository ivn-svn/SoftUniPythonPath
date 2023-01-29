
class Shop:
    def __init__(self, name: str, type: str, capacity: int):
        self.name = str(name)
        self.type = str(type)
        self.capacity = int(capacity)
        self.items = dict()

    # the method below needs to create a new instance of our class, therefore according to the convention, it should be a
    # class method as it instantiates and performs actions upon the class.
    @classmethod
    def small_shop(cls, name: str, type: str):
        return cls(name, type, 10)

    # The method below only instantiates the class, therefore it shall be an instance method
    def add_item (self, item_name):
        if self.capacity > sum(self.items.values()):
            if item_name not in self.items:
                self.items[item_name] = 0
            self.items[item_name] += 1
            return f"{item_name} added to the shop"
        return "Not enough capacity in the shop"
 
    # We do not need a staticmethod here as there is no isolated action to be performed.
    def remove_item(self, item_name: str, amount: int):
        if item_name in self.items.keys():
            if self.items[item_name] <= 0:
                del self.items[item_name]
            else:
                self.items[item_name] -= amount
                return  f"{amount} {item_name} removed from the shop"
        else:
            return f"Cannot remove {amount} {item_name}"
    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"
# TODO:
# •	small_shop(name: str, type: str) - a new shop with a capacity of 10 should be created
# •	add_item(item_name:str) - adds 1 to the quantity of the given item. On success, the method should
# return "{item_name} added to the shop". If the addition is not possible, the following message should be returned
# "Not enough capacity in the shop"
# •	remove_item(item_name:str, amount:int) - removes the given amount from the item. On success, it should
# return "{amount} {item_name} removed from the shop". Otherwise, the method should
# return "Cannot remove {amount} {item_name}"
# o	If the item quantity reaches 0, the item should be removed from the items' dictionary.
# •	__repr__() - returns a string representation in the format "{shop_name} of type {shop_type} with capacity {shop_capacity}"
# 
# to follow through the lecture , starting from:
# https://softuni.bg/trainings/resources/video/73898/video-12-july-2022-ines-ivanova-kenova-python-oop-june-2022/3705

