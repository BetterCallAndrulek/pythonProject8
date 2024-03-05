import json

from src.category import Category
from src.product import Product


def main():

    with open('products.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)

    categories = []

    for category_data in data:
        category = Category(category_data['name'], category_data['description'])
        for product_data in category_data['products']:
            product = Product(product_data['name'], product_data['description'], product_data['price'], product_data['quantity'])
            category.add_product(product)

        print(f'{category.name}\n{category.description}\n{category.products}')
        print(category)
        categories.append(category)


if __name__ == '__main__':
    main()
