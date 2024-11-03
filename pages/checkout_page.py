from pages.Page import Page
from selenium.webdriver.common.by import By

class CheckoutPage(Page):

    def __init__(self, driver):
        super().__init__(driver)
        self.first_name_textbox = (By.ID, "first-name")
        self.last_name_textbox = (By.ID, "last-name")
        self.postal_code_textbox = (By.ID, "postal-code")
        self.error_info = (By.XPATH, "//*[@class='error-message-container error']/h3")
        self.continue_button = (By.ID, "continue")
        self.cancel_button = (By.ID, "cancel")
    
    def error_exists(self):
        return len(self.driver.find_elements(*self.error_info)) > 0
 
    def get_error_communicate(self):
        if self.error_exists():
            return self.driver.find_element(*self.error_info).text
        return None
        
    def first_name(self):
        self.send_keys_to_element(self.first_name_textbox, "first_name")

    def last_name(self):
        self.send_keys_to_element(self.last_name_textbox, "last_name")

    def postal_code(self):
        self.send_keys_to_element(self.postal_code_textbox, "postal_code")

    def click_continue_button(self):
        self.click_element(self.continue_button)

    def click_cancel_button(self):
        self.click_element(self.cancel_button)