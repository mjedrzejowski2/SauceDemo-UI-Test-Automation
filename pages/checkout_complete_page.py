from Page import Page
from selenium.webdriver.common.by import By

class CheckoutCompletePage(Page):

    def __init__(self, driver):
        super().__init__(driver)
        self.back_home_button = (By.ID, "back-to-products")

    def click_back_home_button(self):
        self.click_element(self.back_home_button)
