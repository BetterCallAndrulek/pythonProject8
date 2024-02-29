import json

from src.category import Category
from src.product import Product


def main():

    with open(FILE_JSON) as file:
        raw_json = file.read()
        data = json.loads(raw_json)
        categories = []
        for cat_data in data:
            products_instances = []
            for product_data in cat_data['products']:
                new_product = Product.new_product(product_data)
                products_instances.append(new_product)
            category = Category(cat_data['name'], cat_data['description'], products_instances)
            categories.append(category)
        print(categories)


if __name__ == '__main__':
    main()

