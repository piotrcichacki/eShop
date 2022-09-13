class Apple:
    
    def __init__(self, species_name, size, price):
        self.species_name = species_name
        self.size = size
        self.price = price

    def __repr__(self):
        return f"<Apple species_name={self.species_name}, size={self.size}, price={self.price}>"

    def calculate_total_price(self, quantity):
        return self.price * quantity
