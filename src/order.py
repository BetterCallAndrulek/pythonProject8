from category_order import CategoryOrderABC
from product_error import ProductZeroError


class Order(CategoryOrderABC):
    def __init__(self, name: str, quantity: int, price: float):
        self.name = name
        try:
            if quantity != 0:
                self.quantity = quantity
        except ProductZeroError as e:
            print(e)
        else:
            print("Товар добавлен")
        finally:
            print("Обработка добавления товара завершена")
        self.price = price

    def total_cost(self):
        return self.quantity * self.price