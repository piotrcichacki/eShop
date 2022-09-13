class OrderElement:

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def __str__(self):
        return f"{self.product} x {self.quantity}"

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented

        return self.product == other.product and self.quantity == other.quantity

    def calculate_total_price(self):
        return self.quantity * self.product.unit_price
