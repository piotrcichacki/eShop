from shop.discount_policy import DiscountPolicy
from shop.order_element import OrderElement


class Order:

    MAX_ORDER_ELEMENTS_NUMBER = 10

    def __init__(self, client_first_name, client_last_name, order_elements=None, discount_policy=None):
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name

        if order_elements is None:
            order_elements = []
        if len(order_elements) > Order.MAX_ORDER_ELEMENTS_NUMBER:
            order_elements = order_elements[:Order.MAX_ORDER_ELEMENTS_NUMBER]
        self._order_elements = order_elements

        if discount_policy is None:
            discount_policy = DiscountPolicy()
        self.discount_policy = discount_policy

    @property
    def order_elements(self):
        return self._order_elements

    @order_elements.setter
    def order_elements(self, value):
        if len(value) > Order.MAX_ORDER_ELEMENTS_NUMBER:
            value = value[:Order.MAX_ORDER_ELEMENTS_NUMBER]
        self._order_elements = value

    @property
    def total_price(self):
        total_price = 0
        for order_element in self._order_elements:
            total_price += order_element.calculate_total_price()
        return self.discount_policy.apply_discount(total_price)

    def add_product_to_order(self, product, quantity):
        if len(self._order_elements) < Order.MAX_ORDER_ELEMENTS_NUMBER:
            new_element = OrderElement(product, quantity)
            self._order_elements.append(new_element)
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


class ExpressOrder(Order):

    EXPRESS_DELIVERY_FEE = 10

    def __init__(self, delivery_date, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.delivery_date = delivery_date

    @property
    def total_price(self):
        return super().total_price + ExpressOrder.EXPRESS_DELIVERY_FEE

    def __str__(self):
        mark_line = "-" * 50
        order_details = f"Express order placed by: {self.client_first_name} {self.client_last_name}"
        value_details = f"Of total value: {self.total_price} PLN"
        delivery_date = f"With delivery date: {self.delivery_date}"
        order_elements_details = "Ordered products:\n"
        for order_element in self._order_elements:
            order_elements_details += f"\t{order_element}\n"
        return "\n".join([mark_line, order_details, value_details, delivery_date, order_elements_details, mark_line])


