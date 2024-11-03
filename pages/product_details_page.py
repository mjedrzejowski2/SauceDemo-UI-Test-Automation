from Page import Page
from selenium.webdriver.common.by import By

class ProductDetailsPage(Page):
    
    def __init__(self, driver):
        super().__init__(driver)

        self.add_to_cart_button = (By.ID, "add-to-cart")
        self.price = (By.CLASS_NAME, "inventory_details_price")
        self.back_button = (By.ID, "back-to-products")
        self.product_name = (By.CLASS_NAME, "inventory_details_name large_size")

    
    def click_add_to_cart(self):
        self.click_element(self.add_to_cart_button)
    
    def click_back_button(self):
        self.click_element(self.back_button)

    def get_price(self):
        return self.driver.find_element(*self.price)
    
    def get_product_name(self):
        return self.driver.find_element(*self.product_name)