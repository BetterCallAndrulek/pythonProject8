from src.product import Product
class LawnGrass(ProductsABC, ObjectMixin):

    def __init__(self,
                 name: str,
                 description: str,
                 price: float,
                 quantity: int,
                 color: str,
                 country: str,
                 germination_period: int):
        super().__init__(name, description, price, quantity, color)
        self.country = country
        self.germination_period = germination_period

    def keeping(self):

        print('Газонная трава хранится в помещении при температуре не выше +10 градусов')
