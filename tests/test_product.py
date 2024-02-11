import pytest
from src.product import Product


@pytest.fixture()
def class_product():
    return Product("Телевизоры", "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником", 123000.0, 7)


def test_classes_product(class_product):
    assert class_product.get_name() == "Телевизоры"
    assert class_product.get_description() == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    assert class_product.get_price() == 123000.0
    assert class_product.get_quantity_in_stock() == 7