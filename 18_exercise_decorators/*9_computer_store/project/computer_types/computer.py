from abc import ABC, abstractmethod
from math import log2


class Computer(ABC):
    
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if value.strip() == '':
            raise ValueError("Manufacturer name cannot be empty.")
        self._manufacturer = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if value.strip() == '':
            raise ValueError("Model name cannot be empty.")
        self._model = value

    @property
    @abstractmethod
    def computer_processors(self):
        pass

    @property
    @abstractmethod
    def max_ram(self):
        pass

    @property
    def valid_ram(self):
        result_price_ram = [2 ** c for c in range(1, int(log2(self.max_ram)) + 1)]
        return result_price_ram

    @property
    @abstractmethod
    def name_comp(self):
        pass

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.computer_processors:
            raise ValueError(f"{processor} is not compatible with {self.name_comp} {self.manufacturer} {self.model}!")

        if ram not in self.valid_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with {self.name_comp} {self.manufacturer} {self.model}!")

        processor_price = self.computer_processors[processor]
        ram_price = int(log2(ram) * 100)
        self.processor = processor
        self.ram = ram
        self.price = processor_price + ram_price
        return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
