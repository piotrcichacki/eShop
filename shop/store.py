import random
from typing import Optional

from shop.errors import TemporaryOutOfStock, ProductNotAvailable
from shop.product import Product, ProductCategory


class AvailableProduct:

    def __init__(self, quantity: int, name: str, category: ProductCategory,
                 unit_price: Optional[float] = None, identifier: Optional[int] = None):

        unit_price = random.uniform(1, 100) if unit_price is None else unit_price
        identifier = random.randint(1, 100) if identifier is None else identifier

        self.quantity = quantity
        self.product = Product(name=name, category=category, unit_price=unit_price, identifier=identifier)


class Store:
    AVAILABLE_PRODUCTS = [
        AvailableProduct(quantity=2, name="Hammer", category=ProductCategory.TOOLS),
        AvailableProduct(quantity=5, name="Bread", category=ProductCategory.FOOD),
        AvailableProduct(quantity=1, name="Mower", category=ProductCategory.TOOLS),
        AvailableProduct(quantity=1, name="Bike", category=ProductCategory.OTHER),
    ]

    @staticmethod
    def reserve_product(product: Product, quantity: int) -> None:
        for available_product in Store.AVAILABLE_PRODUCTS:
            if available_product.product == product:
                if available_product.quantity >= quantity:
                    available_product.quantity -= quantity
                    return None
                else:
                    raise TemporaryOutOfStock(product_name=product.name, available_quantity=available_product.quantity)
        raise ProductNotAvailable(product_name=product.name)
