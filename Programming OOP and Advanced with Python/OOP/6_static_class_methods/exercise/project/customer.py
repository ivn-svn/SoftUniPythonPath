
class Customer:
    def __init__(self, name: str, age: int, id: int):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []

    def __repr__(self):
        dvd_names = ", ".join(dvd.name for dvd in self.rented_dvds)
        count_rented_dvds = len(self.rented_dvds)
        return f"{self.id}: {self.name} of age {self.age} has {count_rented_dvds} rented DVD's ({dvd_names})"


c1 = Customer("John", 16, 1)
c2 = Customer("Anna", 55, 2)
