

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import os
os.environ['WDM_LOG_LEVEL'] = '0'

class WebDriverFactory:
    base_url = "https://rahulshettyacademy.com/angularpractice/"

    #returns driver object
    def get_webdriver_instance(self):
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options,service=service)
        driver.delete_all_cookies()
        driver.get(self.base_url)
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        return  driver





