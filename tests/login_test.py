import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from tests.base_test import BaseTest
from pages.login_page import LoginPage

class TestLogin(BaseTest):
    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.login("Admin", "admin123")
        login_page.click_login()

