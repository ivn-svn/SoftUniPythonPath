class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.__animals = 0
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species.lower() == "fish":
            self.fishes.append(name)
        elif species.lower() == "bird":
            self.birds.append(name)
        self.__animals += 1

    def get_info(self, species):
        spec = ''
        if species == "mammal":
            all = self.mammals
            spec = "Mammals"
        elif species == "fish":
            all = self.fishes
            spec = "Fishes"
        elif species.lower() == "bird":
            all = self.birds
            spec = "Birds"

        all_ = ', '.join(all)
        return "{} in {}: {}\nTotal animals: {}".format(spec, self.zoo_name,
                                                        all_, self.__animals)


zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input())

for i in range(count):
    animal = input().split(" ")
    species = animal[0]
    name = animal[1]
    zoo.add_animal(species, name)

info = input()
print(zoo.get_info(info))
