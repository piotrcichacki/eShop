from shop.data_generator import generate_order_elements
from shop.order import Order


def run_example():

    first_name, last_name = "Piotr", "Cichacki"
    order_elements = generate_order_elements()
    order = Order(first_name, last_name, order_elements)

    for order_element in order.order_elements:
        print(order_element)
    print("Order price:", order.total_price)

    other_order_elements = generate_order_elements()
    order.order_elements = other_order_elements

    for order_element in order.order_elements:
        print(order_element)
    print("Order price:", order.total_price)


if __name__ == "__main__":
    run_example()
