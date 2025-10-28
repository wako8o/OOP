from project.clients.base_client import BaseClient


class RegularClient(BaseClient):

    DISCOUNTS_CLIENTS = 5.0
    DISCOUNTS = 0.0
    MIN_ORDERS = 1

    def __init__(self, name: str, phone_number: str):
        super().__init__(name, phone_number)

    def update_discount(self):
        if self.total_orders >= self.MIN_ORDERS:
            self.discount = self.DISCOUNTS_CLIENTS

        else:
            self.discount = self.DISCOUNTS
