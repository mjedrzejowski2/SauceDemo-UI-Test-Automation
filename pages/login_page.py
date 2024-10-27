from selenium.webdriver.common.by import By
from selenium import webdriver
from Page import Page

class LoginPage(Page):

    def __init__(self, driver):
        #wywołuje konstruktor klasy Page (superklasy) i przekazuje jej argument driver.
        super().__init__(driver)
        self.USERNAME_INPUT = (By.ID, "user-name")
        self.PASSWORD_INPUT = (By.ID, "password")
        self.LOGIN_BUTTON = (By.ID, "login-button")
        self.ERROR_INFO = (By.XPATH, "//*[@id='login_button_container']/div/form")
        self.load_site()

    def login(self, username, password):
        self.send_keys_to_element(self.USERNAME_INPUT, username)
        self.send_keys_to_element(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)

    def error_exists(self):
        return len(self.driver.find_elements(*self.ERROR_INFO)) > 0

    def get_error_communicate(self):
        if self.error_exists():
            return self.driver.find_element(*self.ERROR_INFO).text
        
        return None
