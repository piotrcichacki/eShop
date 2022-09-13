import random

from shop.order_element import OrderElement
from shop.product import Product


class Order:

    MAX_ORDER_ELEMENTS_NUMBER = 10

    def __init__(self, client_first_name, client_last_name, order_elements=None):
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name

        if order_elements is None:
            order_elements = []
        if len(order_elements) > Order.MAX_ORDER_ELEMENTS_NUMBER:
            order_elements = order_elements[:Order.MAX_ORDER_ELEMENTS_NUMBER]
        self._order_elements = order_elements
        self.total_price = self._calculate_total_price()

    def _calculate_total_price(self):
        total_price = 0
        for order_element in self._order_elements:
            total_price += order_element.calculate_total_price()
        return total_price

    def add_product_to_order(self, product, quantity):
        if len(self._order_elements) < Order.MAX_ORDER_ELEMENTS_NUMBER:
            new_element = OrderElement(product, quantity)
            self._order_elements.append(new_element)
            self.total_price = self._calculate_total_price()
        else:
            print("Order elements limit has been reached. New product cannot be added.")

    def __str__(self):
        mark_line = "-" * 50
        order_details = f"Order placed by: {self.client_first_name} {self.client_last_name}"
        value_details = f"Of total value: {self.total_price} PLN"
        order_elements_details = "Ordered products:\n"
        for order_element in self._order_elements:
            order_elements_details += f"\t{order_element}\n"
        return "\n".join([mark_line, order_details, value_details, order_elements_details, mark_line])

    def __len__(self):
        return len(self._order_elements)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented

        if len(self._order_elements) != len(other.order_elements):
            return False

        if self.client_first_name != other.client_first_name or self.client_last_name != other.client_last_name:
            return False

        for order_element in self._order_elements:
            if order_element not in other.order_elements:
                return False

        return True

    @classmethod
    def generate_order(cls, number_of_products):
        order_elements = []
        for product_number in range(number_of_products):
            product_name = f"Product-{product_number}"
            category_name = "Others"
            unit_price = random.randint(1, 20)
            quantity = random.randint(1, 10)
            order_element = OrderElement(product=Product(product_name, category_name, unit_price), quantity=quantity)
            order_elements.append(order_element)

        order = Order(client_first_name="Piotr", client_last_name="Cichacki", order_elements=order_elements)
        return order
