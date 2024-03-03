from category_order import CategoryOrderABC
from product_error import ProductZeroError, ProductClassError
from object_mixin import ObjectMixin
from product import Product


class Category(ObjectMixin, CategoryOrderABC):

    total_number_of_categories = 0
    total_number_of_unique_products = 0

    def __init__(self, name: str, description: str, products: list):

        self.name = name
        self.description = description
        self.__products = products
        super().__init__()

        Category.total_number_of_categories += 1
        Category.total_number_of_unique_products += len(self.__products)

    def add_product(self, product):

        try:
            if isinstance(product, Product):
                if product.quantity != 0:
                    Category.total_number_of_unique_products += 1
                    self.__products.append(product)
        except ProductClassError as e:
            print(e)
        except ProductZeroError as e:
            print(e)
        else:
            print("Товар добавлен")
        finally:
            print("Обработка добавления товара завершена")

    @property
    def products(self):
        product_info = []
        for prod in self.__products:
            product_info.append(f'{prod.name}, {int(prod.price)} руб. Остаток: {prod.quantity} шт.')
        return product_info

    def __len__(self):

        return len(self.__products)

    def __str__(self):

        return f'{self.name}, количество продуктов: {self.__len__()} шт.'

    def total_cost(self):

        product_cost_list = []
        for prod in self.__products:
            product_cost_list.append(prod.price * prod.quantity)
        return sum(product_cost_list)

    def average_price(self):

        try:
            sum_prod_price = 0
            for prod in self.__products:
                sum_prod_price += prod.price
            return sum_prod_price / len(self)
        except ZeroDivisionError:
            print('В категории отсутствуют продукты')
            return 0