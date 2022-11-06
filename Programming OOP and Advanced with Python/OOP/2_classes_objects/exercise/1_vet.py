class Vet:
    def __init__(self, name: str, animals: list, space = 5):
        self.name = name
        self.animals = []
        self.space = int(space)
    def register_animal(self, animal_name):
        pass
        if self.space >= 0:
            if animal_name not in self.animals:
                self.animals.append(animal_name)
                return f"{animal_name} registered in the clinic"
        else:
            return f"Not enough space"
    def unregister_animal(self, animal_name):
        self.animal_name = animal_name
        if animal_name not in self.animals:
            return f"{animal_name} not in the clinic"
        else:
            self.animals.remove(self.animal_name)
    def info(self):
        space_left_in_clinic = len(self.animals) 

        return f"{vet_name} has {number_animals} animals. {space_left_in_clinic} space left in clinic"

peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())


# -	register_animal(animal_name)
# o	If there is space in the vet clinic, adds the animal to both animals' lists and returns a message: "{name} registered in the clinic"
# o	Otherwise, returns "Not enough space"
# -	unregister_animal(animal_name)
# o	If the animal is in the clinic, removes it from both animals' lists and returns "{animal} unregistered successfully"
# o	Otherwise, returns "{animal} not in the clinic"
# -	info()
# o	Returns info about the vet, the number of animals in his list and the free space in the clinic:
# "{vet_name} has {number_animals} animals. {space_left_in_clinic} space left in clinic"
