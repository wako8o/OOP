from typing import List, Dict, Type

from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:

    VALID_COMPUTER_NAME: Dict[str, Type[Computer]] = {
                            "Desktop Computer": DesktopComputer,
                           "Laptop": Laptop
                        }

    def __init__(self):
        self.warehouse: List[Computer] = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in self.VALID_COMPUTER_NAME:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        result = self.VALID_COMPUTER_NAME[type_computer](manufacturer, model)
        computer = result.configure_computer(processor, ram)
        self.warehouse.append(result)
        return computer

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        computer = next((x for x in self.warehouse
                         if client_budget >= x.price and wanted_processor == x.processor and  wanted_ram <= x.ram
                         ), None)
        if computer is None:
            raise Exception("Sorry, we don't have a computer for you.")

        self.profits += client_budget - computer.price
        self.warehouse.remove(computer)
        return f"{repr(computer)} sold for {client_budget}$."
