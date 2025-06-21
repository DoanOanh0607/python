from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions
from base_test import BaseTest
import pytest

class TestLogin(BaseTest):
    def test_login(self):
            sleep(5)
            user_name = self.driver.find_element(By.NAME, "username")
            user_name.send_keys("Admin")
            password = self.driver.find_element(By.NAME, "password")
            password.send_keys("admin123")
            self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
            sleep(5)
            dashboard_text = self.driver.find_element(By.XPATH,"//h6[text()='Dashboard']")
            assert dashboard_text.text == "Dashboard"
