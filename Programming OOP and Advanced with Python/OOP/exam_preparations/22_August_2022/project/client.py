class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0.0

    @property
    def phone_number(self) -> str:
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value: str):
        if not self.is_valid_phone_number(value):
            raise ValueError("Invalid phone number!")
        self._phone_number = value

    @staticmethod
    def is_valid_phone_number(phone_number: str) -> bool:
        return len(phone_number) == 10 and phone_number.startswith("0") and phone_number.isdigit()

    def __str__(self):
        return f"Client(phone_number={self.phone_number}, bill={self.bill}, shopping_cart={self.shopping_cart})"
