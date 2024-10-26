from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

class Page:
    def __init__(self, driver):
        self.driver = driver
        self.URL = "https://www.saucedemo.com/"

    def load_site(self):
        self.driver.get(self.URL)
    
    def click_element(self, selector, wait_time=5):
        element = WebDriverWait(self.driver, wait_time).until(EC.element_to_be_clickable(selector))
        element.click()

    def send_keys_to_element(self, selector, text, wait_time=5):
        element = WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located(selector))
        element.send_keys(text)
