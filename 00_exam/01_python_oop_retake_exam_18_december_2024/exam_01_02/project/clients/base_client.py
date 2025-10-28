from abc import ABC, abstractmethod


class BaseClient(ABC):
    def __init__(self, name: str, phone_number: str):
        self.name = name
        self.phone_number = phone_number
        self.discount = 0.0
        self.total_orders = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Name must be at least two characters long!")
        self._name = value

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        if not value.isdigit():
            raise ValueError("Phone number can contain only digits!")
        self._phone_number = value

    @abstractmethod
    def update_discount(self):
        pass

    def update_total_orders(self):
        self.total_orders += 1

    def client_details(self):
        return (f"Client: {self.name}, "
                f"Phone number: {self.phone_number}, "
                f"Orders count: {self.total_orders}, "
                f"Discount: {int(self.discount)}%")