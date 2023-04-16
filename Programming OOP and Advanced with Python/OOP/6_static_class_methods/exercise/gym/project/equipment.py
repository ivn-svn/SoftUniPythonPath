class Equipment:
    id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Equipment.id
        Equipment.id += 1

    def __repr__(self):
        f"Equipment <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Equipment.id