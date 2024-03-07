from product import Product
class ProductError(Exception):
    def __init__(self, message="Произошла ошибка связанная с продуктом"):
        super().__init__(message)


def add_product(self, product):
    try:
        if not isinstance(product, Product):
            raise ProductError("Добавлять можно только объекты класса Product и его подклассы")
        if product.quantity == 0:
            raise ProductError("Количество товара не может быть нулевым")

        Category.total_number_of_unique_products += 1
        self.__products.append(product)
        print("Товар добавлен")
    except ProductError as e:
        print(e)
    finally:
        print("Обработка добавления товара завершена")