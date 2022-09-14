from dataclasses import dataclass


@dataclass
class Product:

    name: str
    category_name: str
    unit_price: float
    identifier: int

    def __str__(self):
        return f"Product name: {self.name} | Category: {self.category_name} | Price: {self.unit_price} PLN"


@dataclass
class ExpiringProduct(Product):

    production_year: int
    validity_years: int

    def does_expire(self, current_year):
        return current_year > self.production_year + self.validity_years

