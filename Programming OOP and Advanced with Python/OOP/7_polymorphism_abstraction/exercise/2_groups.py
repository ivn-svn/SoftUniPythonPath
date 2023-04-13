class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name} {self.surname}"

    def __repr__(self):
        return f"('{self.name}' '{self.surname}')"

    @classmethod
    def __add__(cls, person1, person2):
        return cls(person1.name, person2.surname)


class Group:
    def __init__(self, name: str, people: list):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    @classmethod
    def __add__(cls, other):
        return Group(f"{cls.name} {other.name}", cls.people + other.people)

    def __str__(self):
        return f"Group {self.name} with members {', '.join(map(str, self.people))}"

    def __repr__(self):
        return f"Group('{self.name}', {self.people})"

    def __iter__(self):
        return iter(enumerate(self.people, 1))