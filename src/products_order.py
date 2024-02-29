class ProductsABC(ABC):


    def __init__(self,
                 name: str,
                 description: str,
                 price: float,
                 quantity: int,
                 color: str):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.color = color
        super().__init__()

    @abstractmethod
    def keeping(self):

        pass