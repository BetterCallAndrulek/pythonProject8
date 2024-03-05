class ProductError(Exception):

    def __init__(self, *args):
        self.message = args if args else 'Неизвестная ошибка'

    def __str__(self):
        return self.message


class ProductClassError(ProductError):

    def __init__(self, *args):
        self.message = args if isinstance(args, self.__class__) else 'Добавлять можно только объекты Product и дочерние от них'


class ProductZeroError(ProductError):

    def __init__(self, *args):
        self.message = args if args != 0 else 'Добавлять можно только объекты Product и дочерние от них'
