
class Zoo:
    def __init__(self, name): # attributes come within the __init__ Init is a reserved Python name.
        self.name = name


    # TODO: create 3 lists (mammals, fishes, birds)
    def add_animal(self, species, name):
    # TODO: add the name to the given species
    def get_info(self, species):
    # TODO: create the resulting string and return it

zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input())
total_animals = 0
for i in range(count):
# Read the input
# Add the new animal
# Update the total_animals variable
info = input()
print(zoo.get_info(info))