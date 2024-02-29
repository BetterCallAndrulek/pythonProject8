from src.product import Product
class Smartphone(ProductsABC, ObjectMixin):


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

    def keeping(self):

        print(f'Смартфон хранится в сухом месте при комнатной температуре')