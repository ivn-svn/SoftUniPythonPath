class Inventory:
    def __init__(self, __capacity: int):
        self.items = []
        self.__capacity = __capacity
        self.cap_left = __capacity

    def add_item(self, item: str):
        if self.cap_left > 0:
            self.items.append(item)
            self.cap_left -= 1
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.cap_left

    def __repr__(self):
        joined_items = ', '.join(self.items)
        return "Items: {}.\nCapacity left: {}".format(joined_items, self.__capacity)


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)

# Python's convention to make an instance variable protected is to add a prefix _ (single underscore) to it. ' \
# 'This effectively prevents it from being accessed unless it is from within a sub-class.
#
# capacity - public |
# _capacity - protected |
# __capacity - private |
