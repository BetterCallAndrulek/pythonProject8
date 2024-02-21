def test_shop(shop_fixture):
    shop_fixture.__iter__()
    assert shop_fixture.__next__() == ({
                "name": "Xiaomi Redmi Note 11",
                "description": "1024GB, Синий",
                "price": 31000.0,
                "quantity": 14
            })
    for s in shop_fixture:
        var = s == ({
            "name": "Xiaomi Redmi Note 11",
            "description": "1024GB, Синий",
            "price": 31000.0,
            "quantity": 14
        })