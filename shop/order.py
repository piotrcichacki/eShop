from __future__ import annotations
from typing import Optional, List
from datetime import date

from shop.discount_policy import DiscountPolicy
from shop.order_element import OrderElement
from shop.errors import ElementsInOrderLimitError
from shop.product import Product
from shop.store import Store


class Order:

    MAX_ORDER_ELEMENTS_NUMBER = 10

    def __init__(self, client_first_name: str, client_last_name: str,
                 order_elements: Optional[List[OrderElement]] = None,
                 discount_policy: Optional[DiscountPolicy] = None):
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        self.order_elements = order_elements if order_elements is not None else []
        self.discount_policy = discount_policy if discount_policy is not None else DiscountPolicy()

    @property
    def order_elements(self) -> List[OrderElement]:
        return self._order_elements

    @order_elements.setter
    def order_elements(self, value: List[OrderElement]) -> None:
        if len(value) > Order.MAX_ORDER_ELEMENTS_NUMBER:
            raise ElementsInOrderLimitError(allowed_limit=Order.MAX_ORDER_ELEMENTS_NUMBER)
        self._order_elements = value

    @property
    def total_price(self) -> float:
        total_price = 0.0
        for order_element in self._order_elements:
            total_price += order_element.calculate_total_price()
        return self.discount_policy.apply_discount(total_price)

    def add_product_to_order(self, product: Product, quantity: int) -> None:
        if len(self._order_elements) >= Order.MAX_ORDER_ELEMENTS_NUMBER:
            raise ElementsInOrderLimitError(allowed_limit=Order.MAX_ORDER_ELEMENTS_NUMBER,
                                            message="Order elements limit has been reached. "
                                                    "New product cannot be added.")
        Store.reserve_product(product, quantity)
        new_element = OrderElement(product, quantity)
        self._order_elements.append(new_element)

    def __str__(self) -> str:
        mark_line = "-" * 50
        order_details = f"Order placed by: {self.client_first_name} {self.client_last_name}"
        value_details = f"Of total value: {self.total_price} PLN"
        order_elements_details = "Ordered products:\n"
        for order_element in self._order_elements:
            order_elements_details += f"\t{order_element}\n"
        return "\n".join([mark_line, order_details, value_details, order_elements_details, mark_line])

    def __len__(self) -> int:
        return len(self._order_elements)

    def __eq__(self, other):  # type: ignore
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

    def __init__(self, delivery_date: date, *args, **kwargs):  # type: ignore
        super().__init__(*args, **kwargs)
        self.delivery_date = delivery_date

    @property
    def total_price(self) -> float:
        return super().total_price + ExpressOrder.EXPRESS_DELIVERY_FEE

    def __str__(self) -> str:
        mark_line = "-" * 50
        order_details = f"Express order placed by: {self.client_first_name} {self.client_last_name}"
        value_details = f"Of total value: {self.total_price} PLN"
        delivery_date = f"With delivery date: {self.delivery_date}"
        order_elements_details = "Ordered products:\n"
        for order_element in self._order_elements:
            order_elements_details += f"\t{order_element}\n"
        return "\n".join([mark_line, order_details, value_details, delivery_date, order_elements_details, mark_line])


