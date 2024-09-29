from selenium.webdriver.common.by import By

class LoginPage:
    URL = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        self.driver = driver

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def load(self):
        self.driver.get(self.URL)

