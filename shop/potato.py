from dataclasses import dataclass


@dataclass
class Potato:

    species_name: str
    size: str
    price: float

    def calculate_price(self, quantity):
        return self.price * quantity
