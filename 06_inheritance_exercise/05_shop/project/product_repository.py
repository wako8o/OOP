from typing import List

from project.product import Product


class ProductRepository:

    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        name = next((pro for pro in self.products if pro.name == product_name), None)
        if name:
            return name

    def remove(self, product_name: str):
        remove_product = self.find(product_name)
        if remove_product:
            self.products.remove(remove_product)

    def __repr__(self):
        return '\n'.join(f"{p.name}: {p.quantity}" for p in self.products)
