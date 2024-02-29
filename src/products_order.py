from abc import ABC, abstractmethod


class ProductsABC(ABC):
    @classmethod
    @abstractmethod
    def new_product(cls, product_data):
        pass
