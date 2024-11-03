from Page import Page
from selenium.webdriver.common.by import By

class OverviewPage(Page):

    def __init__(self, driver):
        super().__init__(driver)
        self.cancel_button = (By.ID, "cancel")
        self.finish_button = (By.ID, "finish")
        self.total_price = (By.CLASS_NAME, "summary_total_label")


    def click_cancel_button(self):
        self.click_element(self.cancel_button)

    def click_finish_button(self):
        self.click_element(self.finish_button)

    def get_total_prices(self):
        return float(self.driver.find_element(*self.total_price).text[8:])