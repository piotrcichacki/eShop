from enum import Enum
from typing import List

from shop.errors import TemporaryOutOfStock, ProductNotAvailable, NotValidInput
from shop.order import Order
from shop.persistance import save_order, load_orders
from shop.store import Store, AvailableProduct


class Action(Enum):
    NEW_ORDER = "1"
    HISTORY = "2"


def handle_customer() -> None:
    say_hello()
    selected_action = select_action()
    if selected_action == Action.NEW_ORDER:
        order = init_order()
        while want_more_products():
            add_product_to_order(order, Store.AVAILABLE_PRODUCTS)
        print_order_summary(order)
        save_order(order)
    else:
        show_history()


def say_hello() -> None:
    print("Welcome to our shop!")


def select_action() -> Action:
    selected_action = input("Do you want to place new order (1) or see your orders history (2)? ")
    try:
        return Action(selected_action)
    except ValueError:
        print("There are two available options - by default we choose new order ;)")
        return Action.NEW_ORDER


def show_history() -> None:
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    orders = load_orders(first_name, last_name)
    print("Your orders list:")
    for order in orders:
        print(order)


def init_order() -> Order:
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    return Order(client_first_name=first_name, client_last_name=last_name)


def want_more_products() -> bool:
    selection = input("Do you want to add products to order? Y/N: ")
    if selection.upper() != "Y" and selection.upper() != "N":
        print("There are two available options - I assume, that you want ;)")
        return True
    return selection.upper() == "Y"


def add_product_to_order(order: Order, available_products: List[AvailableProduct]) -> None:
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
        return None

    try:
        order.add_product_to_order(available_products[product_index].product, quantity)
    except TemporaryOutOfStock as error:
        print(f"Unfortunately we have only {error.available_quantity} items of {error.product_name}")
    except ProductNotAvailable as error:
        print(f"Product {error.product_name} is not available. Choose another.")


def parse_product_index(product_index_str: str, max_index: int) -> int:
    try:
        product_index = int(product_index_str)
    except ValueError:
        raise NotValidInput("The product index must be a number")

    if not 0 <= product_index <= max_index:
        raise NotValidInput(f"The product index must be in range from 0 to {max_index}")

    return product_index


def parse_quantity(quantity_str: str) -> int:
    try:
        quantity = int(quantity_str)
    except ValueError:
        raise NotValidInput("The quantity must be a number")

    if quantity < 1:
        raise NotValidInput("The quantity must be at least 1")

    return quantity


def print_order_summary(order: Order) -> None:
    print("Your order:")
    print(order)
    print("Thank you and see you next time!")
