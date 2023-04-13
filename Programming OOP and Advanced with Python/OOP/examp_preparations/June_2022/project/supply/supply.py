class Supply:
    def __init__(self, name: str, energy: int):
        if name == "":
            raise ValueError("Name cannot be an empty string.")
        self.name = name

        if energy < 0:
            raise ValueError("Energy cannot be less than zero.")
        self.energy = energy

    def details(self):
        return f"{self.__class__.__name__}: {self.name}, {self.energy}"
