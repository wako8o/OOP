class Product:

    def __init__(self, name : str, quantity: int):
        self.name = name
        self.quantity = quantity

    def decrease(self, quantity: int) -> str:
        if self.quantity >= quantity:
            self.quantity -= quantity

    def increase(self, quantity: int) -> str:
        self.quantity += quantity

    def __repr__(self):

        return self.name
