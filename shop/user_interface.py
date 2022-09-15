from shop.errors import TemporaryOutOfStock, ProductNotAvailable, NotValidInput
from shop.order import Order
from shop.store import Store


def handle_customer():
    say_hello()
    order = init_order()
    while want_more_products():
        add_product_to_order(order, Store.AVAILABLE_PRODUCTS)
    print_order_summary(order)


def say_hello():
    print("Welcome to our shop!")


def init_order():
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    return Order(client_first_name=first_name, client_last_name=last_name)


def want_more_products():
    selection = input("Do you want to add products to order? Y/N: ")
    if selection.upper() != "Y" and selection.upper() != "N":
        print("There are two available options - I assume, that you want ;)")
        return True
    return selection.upper() == "Y"


def add_product_to_order(order, available_products):
    print("Available products:")
    for index, available_product in enumerate(available_products):
        print(f"{index}) {available_product.product}")

    try:
        product_index_str = input("Choose number: ")
        product_index = parse_product_index(product_index_str, max_index=len(available_products) - 1)

        quantity_str = input("Enter the quantity: ")
        quantity = parse_quantity(quantity_str)
    except NotValidInput as input_error:
        print(input_error)
        return

    try:
        order.add_product_to_order(available_products[product_index].product, quantity)
    except TemporaryOutOfStock as error:
        print(f"Unfortunately we have only {error.available_quantity} items of {error.product_name}")
    except ProductNotAvailable as error:
        print(f"Product {error.product_name} is not available. Choose another.")


def parse_product_index(product_index_str, max_index):
    try:
        product_index = int(product_index_str)
    except ValueError:
        raise NotValidInput("The product index must be a number")

    if not 0 <= product_index <= max_index:
        raise NotValidInput(f"The product index must be in range from 0 to {max_index}")

    return product_index


def parse_quantity(quantity_str):
    try:
        quantity = int(quantity_str)
    except ValueError:
        raise NotValidInput("The quantity must be a number")

    if quantity < 1:
        raise NotValidInput("The quantity must be at least 1")

    return quantity


def print_order_summary(order):
    print("Your order:")
    print(order)
    print("Thank you and see you next time!")
