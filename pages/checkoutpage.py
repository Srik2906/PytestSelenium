from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.seleniumDriver import BaseClass


class CheckoutPage(BaseClass):

    #locators of checkout page
    products_title_css = ".card-title a"
    add_buttons_css = ".card-footer button"
    checkout_button_css = "a.nav-link.btn.btn-primary"
    item_price_xpath = "//tr[1]/td/button/preceding::strong[1]"
    total_price_xpath = "//tr[2]//td[5]/h3/strong"
    checkout_button_xpath = "//tr[3]/td/button[contains(.,'Checkout')]"
    terms_conditions_xpath = "//div[@class='checkbox checkbox-primary']"
    purchase_button_css = "input[type='submit']"

     #constructor of CheckoutPage class
    def __init__(self,driver):
        BaseClass.__init__(self,driver)
        self.base = BaseClass(self.driver)

    # to get product names
    def get_product_titles(self):
        return self.driver.find_elements(By.CSS_SELECTOR,CheckoutPage.products_title_css)

    #to click add button
    def get_add_button(self):
        return self.driver.find_elements(By.CSS_SELECTOR,CheckoutPage.add_buttons_css)

    #clicks checkout button
    def click_checkout(self):
         self.driver.find_element(By.CSS_SELECTOR,CheckoutPage.checkout_button_css).click()

    #get item price
    def get_item_price(self):
        item_price = self.driver.find_element(By.XPATH,CheckoutPage.item_price_xpath).text
        item_price = item_price.split(".")
        item_price = int(item_price[1].strip())
        return item_price

    #get total price
    def get_total_price(self):
        total_price = self.driver.find_element(By.XPATH,CheckoutPage.total_price_xpath).text
        total_price = total_price.split(".")
        total_price = int(total_price[1].strip())
        return total_price

    #click checkout button
    def click_checkout_button(self):
         self.driver.find_element(By.XPATH,CheckoutPage.checkout_button_xpath).click()

    #chooses country
    def select_country(self):
         self.driver.find_element(By.ID, "country").send_keys("India")
         self.base.verify_element_presence("link","India")
         self.driver.find_element(By.LINK_TEXT,"India").click()

    #clicks on terms and conditions
    def clicks_terms_conditions(self):
        self.base.verify_element_presence("xpath",CheckoutPage.terms_conditions_xpath)
        self.driver.find_element(By.XPATH,CheckoutPage.terms_conditions_xpath).click()

    #clicks on purchase button
    def click_purchase_button(self):
         self.driver.find_element(By.CSS_SELECTOR,CheckoutPage.purchase_button_css).click()

    #get success text
    def get_success_text(self):
        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        return successText
