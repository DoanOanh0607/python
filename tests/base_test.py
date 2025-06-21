import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class BaseTest:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, request):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        request.cls.driver = self.driver

        yield
        self.driver.quit()