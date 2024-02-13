class Category:
    name: str
    description: str
    _products: list
    number_categories = 0
    number_products = 0

    def __init__(self, name, description, _products):
        self.name = name
        self.description = description
        self._products = _products
        Category.number_categories += 1
        Category.number_products += len(self._products)

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    @property
    def products(self):
        list_product = []
        for products in self._products:
            list_product.append(f"{products["name"]}, {products["price"]} руб. Остаток: {products["quantity"]} шт.\n")

        return "".join(list_product)

    @products.setter
    def products(self, value):
        self._products.append(value)
