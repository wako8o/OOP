class Cup:

    def __init__(self, size: int, quantity: int):
        self.size = size
        self.quantity = quantity

    def fill(self, quantity):
        total_quantity = self.quantity + quantity
        if self.size >= total_quantity:
            self.quantity += quantity

    def status(self):

        return self.size - self.quantity

cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
