from src.product import Product


def test_classes_product(class_product, class_category):
    assert class_product.get_name() == "55\" QLED 4K"
    assert class_product.get_description() == "Фоновая подсветка"
    assert class_product.price == 123000.0
    assert class_product.get_quantity_in_stock() == 7
    assert Product.create_product({
        "name": "HUAWEI P60",
        "description": "Инновационный изогнутый экран",
        "price": 62_000.0,
        "quantity": 19
    })
