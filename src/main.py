from src.utils import open_file
from src.category import Category
from src.product import Product


def main():
    file = open_file()
    result = []
    for elem in file:
        list_products = [el["name"] for el in elem["products"]]
        category = Category(elem["name"], elem["description"], list_products)
        result.append(f"{category.get_name()}\n"
                      f"{category.get_description()}\n"
                      f"{category.get_products()}\n\n")

        full_list_products = [el for el in elem["products"]]
        for el in full_list_products:
            products = Product(el["name"], el["description"], el["price"], el["quantity"])
            result.append(f"{products.get_name()}\n"
                          f"{products.get_description()}\n"
                          f"{products.get_price()}\n"
                          f"Количество в наличии - {products.get_quantity_in_stock()}\n\n")

    result.append(f"Количество категорий - {category.number_categories}\n"
                  f"Количество товаров - {category.number_products}")

    return "".join(result)


if __name__ == '__main__':
    print(main())