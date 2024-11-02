from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Page import Page
import time

class CartPage(Page):

    def __init__(self, driver):
        super().__init__(driver)
        self.continue_shopping_button = (By.ID, "continue-shopping")
        self.checkout_button = (By.ID, "checkout")
        self.remove_button = (By.XPATH, "//*[@class='item_pricebar']/button")
        self.item_price_bars = (By.XPATH, "//*[@class='inventory_item_price']")
        self.inventory_items =(By.CLASS_NAME, "inventory_item_name")

    def click_continue_shopping(self):
        self.click_element(self.continue_shopping_button)

    def click_checkout(self):
        self.click_element(self.checkout_button)

    def click_remove_button(self):
        self.click_element(self.checkout_button)

    def get_sum_prices(self):
        items_prices = self.driver.find_elements(*self.item_price_bars)
        sum = 0

        for price in items_prices:
            sum += float(price.text[1:])

        return sum

    def remove_all_products(self):
        items = self.driver.find_elements(*self.inventory_items)

        for item in items:
            remove_cart_button = WebDriverWait(item, 5).until(EC.element_to_be_clickable(self.remove_button))
            remove_cart_button.click()
            time.sleep(1)


