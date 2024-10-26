import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    web_driver = webdriver.Chrome()
    web_driver.maximize_window()
    web_driver.delete_all_cookies()
    yield web_driver
    web_driver.quit()