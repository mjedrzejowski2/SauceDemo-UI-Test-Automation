from selenium.webdriver.common.by import By
from selenium import webdriver
from Page import Page
import time

class InventoryPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        # self.add_to_cart_button = (By.CLASS_NAME, "btn_primary")
        self.add_to_cart_button = (By.XPATH, ".//*[@class='pricebar']/button")
        self.number_of_products_in_cart = (By.XPATH, "//*[@class='shopping_cart_badge']")
        self.products_price = (By.XPATH, "//*[@class='inventory_item_price']")
        self.products_names = (By.XPATH, "//*[@class='inventory_item_label']/a")
        self.inventory_item_selector = (By.XPATH, "//*[@class='inventory_item']")
        self.sort_button = (By.XPATH, "//*[@class='product_sort_container']")

    #GET 
    def get_all_products_prices(self):
        prices = []
        for price in self.driver.find_elements(*self.products_price):
            prices.append(price.text[1:])
        return prices

    def get_all_product_names(self):
        names = []
        for name in self.driver.find_elements(*self.products_names):
            names.append(name.text)
        return names

    def get_number_in_cart(self):
        try:
            number = self.driver.find_element(*self.number_of_products_in_cart)
            return number.text
        except:
            return "0"    
    
    def get_all_inventory_items(self):
        items = self.driver.find_elements(*self.inventory_item_selector)
        return items

    #ACTION
    def add_all_products_to_cart(self):
        items = self.get_all_inventory_items()

        for item in items:
            add_to_cart_button = item.find_element(*self.add_to_cart_button)
            add_to_cart_button.click()
            time.sleep(1)
    
    def click_sort_button(self):
        self.click_element(self.sort_button)
        time.sleep(2)


        
