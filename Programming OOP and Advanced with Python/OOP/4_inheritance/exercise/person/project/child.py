from movie_world.project import Person


class Child(Person):
    def __init__(self, name, age: int):
        super().__init__(name, age)
