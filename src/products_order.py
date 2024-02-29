class ProductsABC(ABC):


    def __init__(self):
        super().__init__()

    @classmethod
    @abstractmethod
    def new_product(cls, product_data):
        pass
