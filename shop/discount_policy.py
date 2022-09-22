class DiscountPolicy:

    def apply_discount(self, total_price: float) -> float:
        return total_price


class PercentageDiscount(DiscountPolicy):

    def __init__(self, discount_percentage: int) -> None:
        self.discount_percentage = discount_percentage

    def apply_discount(self, total_price: float) -> float:
        return (100 - self.discount_percentage) / 100 * total_price


class AbsoluteDiscount(DiscountPolicy):

    def __init__(self, discount_value: int):
        self.discount_value = discount_value

    def apply_discount(self, total_price: float) -> float:
        if total_price < self.discount_value:
            return 0
        return total_price - self.discount_value
