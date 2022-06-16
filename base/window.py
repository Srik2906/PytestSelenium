from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base.webdriverfactory import WebDriverFactory


class Window(WebDriverFactory):
    def __init__(self):
        WebDriverFactory.__init__(self,"chrome")
        self.driver = self.get_webdriver_instance()


    def handler(self):
        self.driver.find_element(By.LINK_TEXT,"Click Here").click()
        child_tab = self.driver.window_handles[1]
        self.driver.switch_to.window(child_tab)
        child_text = self.driver.find_element(By.TAG_NAME,"h3").text
        print(child_text)
        parent_tab = self.driver.window_handles[0]
        self.driver.implicitly_wait(5)
        self.driver.switch_to.window(parent_tab)
        parent_text = self.driver.find_element(By.TAG_NAME,"h3").text
        print(parent_text)
        self.driver.switch_to.window(child_tab)
        self.driver.close()
        self.driver.switch_to.window(parent_tab)
        print(self.driver.current_window_handle)
        self.driver.quit()
        action = ActionChains(self.driver)
        action.double_click().perform()

win = Window()
win.handler()
