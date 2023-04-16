from project.meals.meal import Meal


class Starter(Meal):
    def __init__(self, name: str, price: float, quantity: int = 60):
        super().__init__(name, price, quantity)

    def details(self) -> str:
        return f"Starter {self.name}: {self.price:.2f}lv/piece"

    def __str__(self):
        return f"Starter(name={self.name}, price={self.price}, quantity={self.quantity})"
