from shop.order import Order, print_order, generate_order
from shop.product import Product

if __name__ == "__main__":
    cookies = Product(name="Cookies", category_name="Food", unit_price=4)
    order = Order(client_first_name="Piotr", client_last_name="Cichacki", products=[cookies, cookies, cookies])
    print_order(order)

    generated_order = generate_order()
    print_order(generated_order)