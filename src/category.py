class Category:
    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    @property
    def products(self):
        list_product = []
        for products in self.__products:
            list_product.append(f"{products["name"]}, {products["price"]} руб. Остаток: {products["quantity"]} шт.\n")

        return "".join(list_product)

    def add_products(self, value):
        self.__products.append({
            "name": value[0],
            "description": value[1],
            "price": value[2],
            "quantity": value[3]
        })
