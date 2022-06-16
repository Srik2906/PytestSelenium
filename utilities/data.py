import  pytest

pytest.fixture()
def json_data():
    return{
        "test_home_page":{"name":"srikanth",
                          "email":"srikanth.june29@gmail.com",
                            "dob":"29/06/1994"
        },
        "test_shop_page":{
            "products" : ["Blackberry","Nokia Edge","iphone X","Samsung Note 8"]
        }
    }

