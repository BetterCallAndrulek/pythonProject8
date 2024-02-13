from src.utils import open_file
from src.category import Category
from src.product import Product


def main():
    c1 = Category("Смартфоны", "Смартфоны", [
        {
            "name": "Samsung Galaxy C23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5
        },
        {
            "name": "Iphone 15",
            "description": "512GB, Gray space",
            "price": 210000.0,
            "quantity": 8
        },
        {
            "name": "Xiaomi Redmi Note 11",
            "description": "1024GB, Синий",
            "price": 31000.0,
            "quantity": 14
        }
    ])

    p1 = Product("Iphone 15", "512GB, Gray space", 210_000.0, 8)
    print(c1.products)

    c1.products = Product.create_product({"name": "Iphone 15",
                                          "description": "512GB, Gray space",
                                          "price": 210000.0,
                                          "quantity": 8
                                          })
    print(c1.products)


if __name__ == "__main__":
    main()
