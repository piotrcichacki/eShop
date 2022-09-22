import random
from typing import Optional, List

from shop.order import Order
from shop.order_element import OrderElement
from shop.product import Product, ProductCategory

MIN_QUANTITY = 1
MAX_QUANTITY = 10

MIN_UNIT_PRICE = 1
MAX_UNIT_PRICE = 30

MIN_IDENTIFIER = 1
MAX_IDENTIFIER = 100


def generate_product(name: Optional[str] = None) -> Product:
    category = ProductCategory.OTHER
    unit_price = random.randint(MIN_UNIT_PRICE, MAX_UNIT_PRICE)
    identifier = random.randint(MIN_IDENTIFIER, MAX_IDENTIFIER)
    name = f"Product-{identifier}" if name is None else name

    return Product(name, category, unit_price, identifier)


def generate_order_elements(number_of_products: Optional[int] = None) -> List[OrderElement]:
    number_of_products = random.randint(1, Order.MAX_ORDER_ELEMENTS_NUMBER) \
        if number_of_products is None else number_of_products

    order_elements = []
    for product_number in range(number_of_products):
        product_name = f"Product-{product_number}"
        product = generate_product(product_name)
        quantity = random.randint(MIN_QUANTITY, MAX_QUANTITY)
        order_elements.append(OrderElement(product, quantity))

    return order_elements
