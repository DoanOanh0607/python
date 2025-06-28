from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class LoginPage():
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.username_input = (By.XPATH, "//input[@name='username']")
        self.password_input = (By.XPATH, "//input[@name='password']")
        self.login_btn = (By.XPATH, "//button")

    def enter_username(self, username: str):
        username_input = self.wait.until(lambda d: d.find_element(*self.username_input))
        username_input.send_keys(username)

    def enter_password(self, password: str):
        password_input = self.wait.until(lambda d: d.find_element(*self.password_input))
        password_input.send_keys(password)

    def click_login(self):
        login_btn = self.wait.until(lambda d: d.find_element(*self.login_btn))
        login_btn.click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()