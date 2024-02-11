import pytest
from src.category import Category


@pytest.fixture()
def class_product():
    return Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни", ["Samsung Galaxy C23 Ultra", "Iphone 15", "Xiaomi Redmi Note 11"])


def test_classes_product(class_product):
    assert class_product.get_name() == "Смартфоны"
    assert class_product.get_description() == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    assert class_product.get_products() == ["Samsung Galaxy C23 Ultra", "Iphone 15", "Xiaomi Redmi Note 11"]
    assert class_product.number_categories == 1
    assert class_product.number_products == 3