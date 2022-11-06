
class Vet:
    animals = [] # # class attribute 1
    space = 5 # class attribute 2

    def __init__(self, name):
        self.name = name 
        self.animals = [] # Instance attribute here

    def register_animal(self, animal_name):
        if Vet.space <= len(Vet.animals):
            return "Not enough space"

        Vet.animals.append(animal_name)
        self.animals.append(animal_name)
        return f"{animal_name} registered in the clinic"


    def unregister_animal(self, animal_name):
        if animal_name not in self.animals:
            return f"{animal_name} not in the clinic"

        Vet.animals.remove(animal_name)
        self.animals.remove(animal_name)
        return f"{animal_name} unregistered successfully"

    def info(self):
        space_left = Vet.space - len(Vet.animals)
        return f"{self.name} has {len(self.animals)} animals. {space_left} space left in clinic"
