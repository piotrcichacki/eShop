import random

from shop.product import print_product, Product


class Order:

    def __init__(self, client_first_name, client_last_name, products=None):
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name

        if products is None:
            products = []
        self.products = products

        total_price = 0
        for product in products:
            total_price += product.unit_price
        self.total_price = total_price


def print_order(order):
    print("-" * 20)
    print(f"Order placed by: {order.client_first_name} {order.client_last_name}")
    print(f"Of total value: {order.total_price} PLN")
    print("Ordered products:")
    for product in order.products:
        print("\t", end="")
        print_product(product)
    print("-" * 20)
    print()


def generate_order():
    number_of_products = random.randint(1, 10)
    products = []
    for product_number in range(number_of_products):
        product_name = f"Product-{product_number}"
        category_name = "Others"
        unit_price = random.randint(1, 20)
        product = Product(product_name, category_name, unit_price)
        products.append(product)

    order = Order(client_first_name="Piotr", client_last_name="Cichacki", products=products)
    return order