from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BaseClass:

    def __init__(self,driver):
        self.driver = driver

    def verify_element_presence(self,locator,element):
        wait = WebDriverWait(self.driver, 10)
        if locator == "link":
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, element)))
        elif locator == "xpath":
            wait.until(EC.presence_of_element_located((By.XPATH, element)))

