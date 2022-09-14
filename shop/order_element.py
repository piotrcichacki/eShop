from dataclasses import dataclass

from shop.product import Product


@dataclass
class OrderElement:

    product: Product
    quantity: int

    def __str__(self):
        return f"{self.product} x {self.quantity}"

    def calculate_total_price(self):
        return self.quantity * self.product.unit_price
