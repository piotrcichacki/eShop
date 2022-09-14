import random

from shop.order import Order
from shop.order_element import OrderElement
from shop.product import Product
from shop.discount_policy import loyal_customer_policy, christmas_policy


def generate_order_elements():
    order_elements = []
    for product_number in range(5):
        product_name = f"Product-{product_number}"
        category_name = "Others"
        unit_price = random.randint(1, 30)
        product = Product(product_name, category_name, unit_price)
        quantity = random.randint(1, 10)
        order_elements.append(OrderElement(product, quantity))
    return order_elements


def run_example():

    first_name, last_name = "Piotr", "Cichacki"
    order_elements = generate_order_elements()
    normal_order = Order(first_name, last_name, order_elements)
    loyal_customer_order = Order(first_name, last_name, order_elements, discount_policy=loyal_customer_policy)
    christmas_order = Order(first_name, last_name, order_elements, discount_policy=christmas_policy)

    print(normal_order)
    print(loyal_customer_order)
    print(christmas_order)


if __name__ == "__main__":
    run_example()
