from shop.apple import Apple
from shop.order import generate_order, Order
from shop.order_element import OrderElement
from shop.potato import Potato
from shop.product import Product


def run_example():

    green_apple = Apple(species_name="Green", size="M", price=2.8)
    print(green_apple)
    old_potato = Potato(species_name="Potato", size="M", price=3.2)
    print(old_potato)

    cookie = Product(name="Cookie", category_name="Food", unit_price=4)
    other_cookie = Product(name="Cookie", category_name="Food", unit_price=4)
    print("Cookies are equal:", cookie == other_cookie)

    first_order_elements = [
        OrderElement(product=cookie, quantity=5),
        OrderElement(product=other_cookie, quantity=4)
    ]
    first_order = Order(client_first_name="Piotr", client_last_name="Cichacki", order_elements=first_order_elements)
    second_order_elements = [
        OrderElement(product=cookie, quantity=5),
        OrderElement(product=other_cookie, quantity=4)
    ]
    second_order = Order(client_first_name="Piotr", client_last_name="Cichacki", order_elements=second_order_elements)
    print("Orders are equal: ", first_order == second_order)

    print(first_order)


if __name__ == "__main__":
    run_example()
