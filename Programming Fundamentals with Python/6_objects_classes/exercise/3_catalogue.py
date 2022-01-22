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
    def __init__(self, catalogue_name):
        self.people = []
        party = Party()
        line = input()
        while line != "End":
            party.people.append(line)
            line = input()
        print(f"Going: {', '.join(party.people)}")
        print(f"Total: {len(party.people)}")
