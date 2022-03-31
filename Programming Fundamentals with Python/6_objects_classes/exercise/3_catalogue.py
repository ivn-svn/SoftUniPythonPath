# Create a class Catalogue. The __init__ method should accept the name of the catalogue (string). E
# ach catalogue should also have an attribute called products, an empty list.
# The class should also have three more methods:
#     • add_product(product_name: str) - adds the product to the products' list
#     • get_by_letter(first_letter: str) - returns a list containing only the products that start with the given letter
#     • __repr__ - returns the catalogue info in the following format:
# "Items in the {name} catalogue:
# {item1}
# {item2}
# …
# {itemN}"
# The items should be sorted alphabetically in ascending order.

class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []
        self.new_list = []

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [x for x in self.products if first_letter == x[0]]

    def __repr__(self):
        result = f"Items in the {self.name} catalogue:\n"
        result += '\n'.join(sorted(self.products))
        return result
        # return self.new_list


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
# print(catalogue.products)
print(repr(catalogue))
# ref link : https://stackoverflow.com/questions/9751554/list-as-a-member-of-a-python-class-why-is-its-contents-being-shared-across-all
###
