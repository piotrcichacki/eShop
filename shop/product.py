class Product:

    def __init__(self, name, category_name, unit_price, identifier):
        self.name = name
        self.category_name = category_name
        self.unit_price = unit_price
        self.identifier = identifier

    def __str__(self):
        return f"Product name: {self.name} | Category: {self.category_name} | Price: {self.unit_price} PLN"

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented

        return self.name == other.name and \
            self.category_name == other.category_name and \
            self.unit_price == other.unit_price


class ExpiringProduct(Product):

    def __init__(self, production_year, validity_years, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.production_year = production_year
        self.validity_years = validity_years

    def does_expire(self, current_year):
        return current_year > self.production_year + self.validity_years

