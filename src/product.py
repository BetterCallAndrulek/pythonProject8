class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
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
    def create_product(cls):
        new_product = {
            "name": "HUAWEI P60",
            "description": "Инновационный изогнутый экран",
            "price": 62_000.0,
            "quantity": 19
        }
        name, description, price, quantity = \
            (
                new_product["name"], new_product["description"], new_product["price"], new_product["quantity"]
            )
        return cls(name, description, price, quantity)
