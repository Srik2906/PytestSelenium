from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class HomePage:
    ##Locators of home page
    email_xpath = "//form//input[@name='email']"
    name_xpath = "//form//input[@name='name']"
    password_xpath = "//input[@id='exampleInputPassword1']"
    dropdown_xpath = (By.XPATH,"//select")
    shop_button_xpath = "//a[contains(.,'Shop')]"
    checkbox_css = "input[id=exampleCheck1]"
    radio_css = "input[id='inlineRadio1']"
    bday_css = "input[name='bday']"
    submit_buton_css = ".btn.btn-success"
    name_field1_js = "return document.getElementsByName('name')[0].value"
    name_field2_js = "return document.getElementsByName('name')[1].value"
    alert_text_xpath = "//div[ @class ='alert alert-success alert-dismissible']//strong"

    #contructor of HomePage class
    def __init__(self,driver):
        self.driver=driver

    #sends email in the email fields
    def enter_email(self,email):
        return self.driver.find_element(By.XPATH,HomePage.email_xpath).send_keys(email)

    #sends name in the name field
    def enter_name(self,name):
        return self.driver.find_element(By.XPATH,HomePage.name_xpath).send_keys(name)

    #get name text
    def get_name_text(self):
        return self.driver.execute_script(HomePage.name_field1_js)

    #clicks on check box
    def click_checkbox(self):
        return self.driver.find_element(By.CSS_SELECTOR,HomePage.checkbox_css).click()

    #clicks on radio button
    def click_radio(self):
        return self.driver.find_element(By.CSS_SELECTOR,HomePage.radio_css).click()

    #enters bday
    def enter_bday(self,bday):
        return self.driver.find_element(By.CSS_SELECTOR,HomePage.bday_css).send_keys(bday)

    #select gender
    def select_gender(self):
        dropdown = Select(self.driver.find_element(*HomePage.dropdown_xpath))
        return dropdown.select_by_visible_text("Female")

    #clicks on submit button
    def click_submit(self):
        return self.driver.find_element(By.CSS_SELECTOR,HomePage.submit_buton_css).click()

    #Clicks on shop button
    def click_shop(self):
        self.driver.find_element(By.XPATH,HomePage.shop_button_xpath).click()

    ####################################################################################
            ###Functions used for assertions######
    ####################################################################################

    #return name
    def return_name(self):
        name = self.driver.execute_script(HomePage.name_field2_js)
        return name

    #returns alert message
    def return_alert_text(self):
        alert_text = self.driver.find_element(By.XPATH,HomePage.alert_text_xpath).text
        return alert_text
