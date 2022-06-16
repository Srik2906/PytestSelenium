import unittest

import pytest
from utilities.data import json_data
from pages.homepage import HomePage

username = json_data()['test_home_page']['name']
email= json_data()['test_home_page']['email']
dob = json_data()['test_home_page']['dob']

@pytest.mark.usefixtures("setup")
class Home(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.homepage = HomePage(self.driver)

    def test_home_page_name(self):
        self.homepage.enter_email(email)
        self.homepage.enter_name(username)
        name = self.homepage.get_name_text()
        self.homepage.click_checkbox()
        self.homepage.enter_bday(dob)
        self.homepage.click_radio()
        self.homepage.select_gender()
        binding_name = self.homepage.return_name()
        assert name == binding_name

    def test_home_page_alert_text(self):
        self.homepage.click_submit()
        alert_text = self.homepage.return_alert_text()
        assert "Success!" in alert_text
