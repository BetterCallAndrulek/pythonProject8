class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, _price, quantity):
        self.name = name
        self.description = description
        self._price = _price
        self.quantity = quantity

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена введена не корректно")
        elif value < self._price:
            while True:
                answer = input("Новая цена ниже чем старая, вы уверены что хотите изменить цену (y/n): ").lower()
                if answer == "y":
                    self._price = value
                    break
                elif answer == "n":
                    self._price = self._price
                    break
        else:
            self._price = value

    def get_quantity_in_stock(self):
        return self.quantity

    @classmethod
    def create_product(cls, product):
        if product["name"] == Product.name:
            Product.quantity += product["quantity"]
            return product
