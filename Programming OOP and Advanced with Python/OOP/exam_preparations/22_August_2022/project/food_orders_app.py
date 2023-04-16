from project.meals.starter import Starter
from project.meals.main_dish import MainDish
from project.meals.dessert import Dessert
from project.meals.meal import Meal
from project.client import Client


class FoodOrdersApp:
    def __init__(self):
        self._menu = []
        self._clients_list = []
        self._receipt_counter = 0

    @property
    def menu(self):
        return self._menu

    @property
    def clients_list(self):
        return self._clients_list

    def register_client(self, client_phone_number: str) -> str:
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                raise Exception("The client has already been registered!")
        client = Client(client_phone_number)
        self.clients_list.append(client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals):
        for meal in meals:
            if isinstance(meal, (Starter, MainDish, Dessert)):
                self.menu.append(meal)

    def show_menu(self) -> str:
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        return "\n".join(meal.details() for meal in self.menu)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        client = next((client for client in self.clients_list if client.phone_number == client_phone_number), None)
        if not client:
            client = self.register_client(client_phone_number)

        ordered_meals = []
        for meal_name, quantity in meal_names_and_quantities.items():
            meal = next((meal for meal in self.menu if meal.name == meal_name), None)
            if not meal:
                raise Exception(f"{meal_name} is not on the menu!")
            if meal.quantity < quantity:
                meal_type = type(meal).__name__
                raise Exception(f"Not enough quantity of {meal_type}: {meal_name}!")
            meal.quantity -= quantity
            client.shopping_cart.append((meal, quantity))
            ordered_meals.append(meal.name)
            client.bill += meal.price * quantity

        return f"Client {client_phone_number} successfully ordered {', '.join(ordered_meals)} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = next((client for client in self.clients_list if client.phone_number == client_phone_number), None)

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for meal, quantity in client.shopping_cart:
            meal.quantity += quantity

        client.shopping_cart.clear()
        client.bill = 0

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = next((client for client in self.clients_list if client.phone_number == client_phone_number), None)

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        total_paid = client.bill

        for meal, quantity in client.shopping_cart:
            meal.quantity += quantity

        client.shopping_cart.clear()
        client.bill = 0
        self._receipt_counter += 1

        return f"Receipt #{self._receipt_counter} with total amount of {total_paid:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
