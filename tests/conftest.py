import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from base.webdriverfactory import WebDriverFactory

@pytest.fixture(scope="class")
def setup(request):
    wdf = WebDriverFactory()
    driver = wdf.get_webdriver_instance()
    request.cls.driver = driver
    yield
    driver.quit()


