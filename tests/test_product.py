from src.product import Product


def test_classes_product(class_product, class_category):
    assert class_product.get_name() == "55\" QLED 4K"
    assert class_product.get_description() == "Фоновая подсветка"
    assert class_product._price == 123000.0
    assert class_product.get_quantity_in_stock() == 7
    assert Product.create_product() == ("HUAWEI P60", "Инновационный изогнутый экран", 62000.0, 19)
