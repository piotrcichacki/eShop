import random

from shop.order import Order
from shop.order_element import OrderElement
from shop.product import Product, ProductCategory

MIN_QUANTITY = 1
MAX_QUANTITY = 10

MIN_UNIT_PRICE = 1
MAX_UNIT_PRICE = 30

MIN_IDENTIFIER = 1
MAX_IDENTIFIER = 100


def generate_product(name=None):
    category = ProductCategory.OTHER
    unit_price = random.randint(MIN_UNIT_PRICE, MAX_UNIT_PRICE)
    identifier = random.randint(MIN_IDENTIFIER, MAX_IDENTIFIER)

    if name is None:
        name = f"Product-{identifier}"

    return Product(name, category, unit_price, identifier)


def generate_order_elements(number_of_products=None):
    if number_of_products is None:
        number_of_products = random.randint(1, Order.MAX_ORDER_ELEMENTS_NUMBER)

    order_elements = []
    for product_number in range(number_of_products):
        product_name = f"Product-{product_number}"
        product = generate_product(product_name)
        quantity = random.randint(MIN_QUANTITY, MAX_QUANTITY)
        order_elements.append(OrderElement(product, quantity))

    return order_elements
