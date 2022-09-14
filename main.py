from shop.apple import Apple
from shop.order_element import OrderElement
from shop.potato import Potato
from shop.product import Product


def run_example():

    green_apple = Apple(species_name="Green", size="M", price=4.5)
    old_potato = Potato(species_name="Potato", size="S", price=2.8)
    print(green_apple)
    print(old_potato)

    cookies = Product(name="Cookies", category_name="Food", unit_price=2.8, identifier=10)
    print(cookies)
    order_element = OrderElement(product=cookies, quantity=8)
    print(order_element)


if __name__ == "__main__":
    run_example()
