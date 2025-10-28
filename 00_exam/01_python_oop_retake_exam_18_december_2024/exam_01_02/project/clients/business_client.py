from project.clients.base_client import BaseClientz


class BusinessClient(BaseClient):
    DISCOUNTS_CLIENTS = 10.0
    DISCOUNTS = 0.0
    MIN_ORDERS = 2

    def __init__(self, name: str, phone_number: str):
        super().__init__(name, phone_number)

    def update_discount(self):
        if self.total_orders >= self.MIN_ORDERS:
            self.discount = self.DISCOUNTS_CLIENTS

        else:
            self.discount = self.DISCOUNTS
