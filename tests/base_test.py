import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class BaseTest:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, request):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element(By.XPATH, "//input[@name='username']")
        )
        request.cls.driver = self.driver

        yield
        self.driver.quit()