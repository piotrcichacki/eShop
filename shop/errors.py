from typing import Optional


class ElementsInOrderLimitError(Exception):

    def __init__(self, allowed_limit: int, message: Optional[str] = None):
        self.allowed_limit = allowed_limit
        if message is None:
            message = f"Order elements limit has been reached. The limit is {self.allowed_limit}."
        super().__init__(message)


class ProductNotAvailable(Exception):

    def __init__(self, product_name: str):
        self.product_name = product_name
        super().__init__()


class TemporaryOutOfStock(ProductNotAvailable):

    def __init__(self, product_name: str, available_quantity: int):
        self.available_quantity = available_quantity
        super().__init__(product_name)


class NotValidInput(Exception):
    pass
