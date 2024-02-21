def test_classes_product(class_category):
    assert class_category.get_name() == "Смартфоны"
    assert class_category.get_description() == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    assert class_category.products == ("Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
                                       "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
                                       "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n")

    class_category.add_products(("Iphone 15", "512GB, Gray space", 210000.0, 8))
