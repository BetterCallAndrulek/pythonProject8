from object_mixin import ObjectMixin
from product import Product
class Smartphone(Product, ObjectMixin):

    def __init__(self,
                 name: str,
                 description: str,
                 price: float,
                 quantity: int,
                 color: str,
                 efficiency: str,
                 model: str,
                 memory: int):
        super().__init__(name, description, price, quantity, color)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory