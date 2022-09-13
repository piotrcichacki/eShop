from shop.order import Order
from shop.order_element import OrderElement
from shop.product import Product
from shop.tax_calculator import TaxCalculator


def run_example():

    order = Order.generate_order(number_of_products=20)
    print(order)

    cookie = Product(name="Cookie", category_name="Food", unit_price=4)
    order.add_product_to_order(cookie, 10)
    print(order)

    cookies = Product(name="Cookies", category_name="Food", unit_price=9)
    cookies_order_element = OrderElement(product=cookies, quantity=10)
    cookies_tax = TaxCalculator.tax_for_order_element(cookies_order_element)
    print(f"Cookies price: {cookies_order_element.calculate_total_price()} PLN + tax {cookies_tax} PLN")


if __name__ == "__main__":
    run_example()
