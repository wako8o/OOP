from abc import ABC, abstractmethod


class BasePlant(ABC):

    WATERS_NEEDED = range(1, 2001)

    def __init__(self, name: str, price: float, water_needed: int):
        self.name = name
        self.price = price
        self.water_needed = water_needed

    @abstractmethod
    def plant_details(self):
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Plant name cannot be null or empty!")
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price must be greater than zero!")
        self._price = value

    @property
    def water_needed(self):
        return self._water_needed

    @water_needed.setter
    def water_needed(self, value):
        if value not in self.WATERS_NEEDED:
            raise ValueError("Water needed must be between 1 and 2000 ml!")
        self._water_needed = value
