import unittest
import pytest
from selenium.webdriver.common.by import By

from pages.checkoutpage import CheckoutPage
from pages.homepage import HomePage
from utilities.data import json_data

productlist = json_data()['test_shop_page']['products']
@pytest.mark.usefixtures("setup")
class Shop(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.homepage = HomePage(self.driver)
        self.checkoutpage = CheckoutPage(self.driver)

    def test_product_price(self):
        self.homepage.click_shop()
        products = self.checkoutpage.get_product_titles()
        i = -1
        for product in products:
            i = i + 1
            productName = product.text
            if productName == productlist[0]:
                self.checkoutpage.get_add_button()[i].click()
        self.checkoutpage.click_checkout()
        item_price = self.checkoutpage.get_item_price()
        total_price = self.checkoutpage.get_total_price()
        assert item_price == total_price

    def test_success_message(self):
        self.checkoutpage.click_checkout_button()
        self.checkoutpage.select_country()
        self.checkoutpage.clicks_terms_conditions()
        self.checkoutpage.click_purchase_button()
        successText = self.checkoutpage.get_success_text()
        assert "Success! Thank you!" in successText