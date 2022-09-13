class Product:

    def __init__(self, name, category_name, unit_price):
        self.name = name
        self.category_name = category_name
        self.unit_price = unit_price


def print_product(product):
    print(f"Product name: {product.name} | Category: {product.category_name} | Unit price: {product.unit_price} PLN")
