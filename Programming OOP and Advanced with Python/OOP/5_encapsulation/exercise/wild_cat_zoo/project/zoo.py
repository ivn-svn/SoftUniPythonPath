from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = list()
        self.workers = list()

    def add_animal(self, animal, price):
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"
        if price > self.__budget:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name___} added to the zoo"

    def fire_worker(self, worker_name: str):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker_name)
                return f"{worker_name} fired successfully"
            return f"There is no {worker_name} worker in the zoo"

    def pay_workers(self):
        pay_salaries = sum(w.salary for w in self.workers)
        if self.__budget > pay_salaries:
            self.__budget -= pay_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy."

    def tend_animals(self):
        animal_care = sum(c.money_for_care for c in self.animals)
        if self.__budget >= animal_care:
            self.__budget -= animal_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f'You have {len(self.animals)} animals\n'
        lions = [repr(l) for l in self.animals if isinstance(l, Lion)]
        result += f'----- {len(lions)} Lions:\n' + '\n'.join(lions) + '\n'
        tigers = [repr(t) for t in self.animals if isinstance(t, Tiger)]
        result += f'----- {len(tigers)} Tigers:\n' + '\n'.join(tigers) + '\n'
        cheetahs = [repr(c) for c in self.animals if isinstance(c, Cheetah)]
        result += f'----- {len(cheetahs)} Cheetahs:\n' + '\n'.join(cheetahs) + '\n'
        return result

    def workers_status(self):
        result = f'You have {len(self.workers)} workers\n'
        keepers = [repr(l) for l in self.workers if isinstance(l, Keeper)]
        result += f'----- {len(keepers)} Keepers:\n' + '\n'.join(keepers) + '\n'
        caretakers = [repr(c) for c in self.workers if isinstance(c, Caretaker)]
        result += f'----- {len(caretakers)} Caretakers:\n' + '\n'.join(caretakers) + '\n'
        vets = [repr(v) for v in self.workers if isinstance(v, Vet)]
        result += f'----- {len(vets)} Vets:\n' + '\n'.join(vets) + '\n'
        return result



