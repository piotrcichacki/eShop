from shop.order_element import OrderElement


class TaxRates:

    FRUITS_AND_VEGETABLES = 0.05
    FOOD = 0.08
    ALL = 0.2


class TaxCalculator:

    @staticmethod
    def tax_for_order_element(order_element: OrderElement) -> float:
        product_category = order_element.product.category
        if product_category.value == "Fruits and vegetables":
            tax_rate = TaxRates.FRUITS_AND_VEGETABLES
        elif product_category.value == "Food":
            tax_rate = TaxRates.FOOD
        else:
            tax_rate = TaxRates.ALL

        return tax_rate * order_element.calculate_total_price()

