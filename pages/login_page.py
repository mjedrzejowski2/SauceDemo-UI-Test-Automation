from selenium.webdriver.common.by import By
from selenium import webdriver

class LoginPage:

    URL = "https://www.saucedemo.com/"
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_INFO = (By.XPATH, "//*[@id='login_button_container']/div/form")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def error_exists(self):
        return len(self.driver.find_elements(*self.ERROR_INFO)) > 0

    def get_error_communicate(self):
        if self.error_exists():
            return self.driver.find_element(*self.ERROR_INFO).text
        
        return None

if __name__ == '__main__':
    x = LoginPage(webdriver.Chrome())
    x.load()
    x.login("standard_user", "secret_sauce")
    x.get_error_communicate()