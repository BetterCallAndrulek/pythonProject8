class Category:
    name: str
    description: str
    products: list
    number_categories = 0
    number_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.number_categories += 1
        Category.number_products += len(self.products)

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_products(self):
        return self.products