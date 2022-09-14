from shop.data_generator import generate_order_elements
from shop.discount_policy import AbsoluteDiscount, PercentageDiscount
from shop.order import Order


def run_example():

    first_name, last_name = "Piotr", "Cichacki"
    order_elements = generate_order_elements()
    normal_order = Order(first_name, last_name, order_elements)

    percentage_discount = PercentageDiscount(discount_percentage=10)
    percentage_discount_order = Order(first_name, last_name, order_elements, discount_policy=percentage_discount)

    absolute_discount = AbsoluteDiscount(discount_value=100)
    absolute_discount_order = Order(first_name, last_name, order_elements, discount_policy=absolute_discount)

    print(normal_order)
    print(percentage_discount_order)
    print(absolute_discount_order)


if __name__ == "__main__":
    run_example()
