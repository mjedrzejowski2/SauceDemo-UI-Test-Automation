from selenium import webdriver
from login_page import LoginPage
from inventory_page import InventoryPage
import time

if __name__ == '__main__':
    # Uruchamianie przeglądarki
    driver = webdriver.Chrome()

    try:
        # Inicjalizacja strony logowania
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        # Przechodzimy na stronę InventoryPage, przekazując driver
        inventory_page = InventoryPage(driver)
        # results = inventory_page.get_all_products_prices()
        # names = inventory_page.get_all_product_names()
        # items = inventory_page.get_all_inventory_items()
        # inventory_page.add_all_products_to_cart()
        inventory_page.click_sort_button()
        # print(results)
        # print(names)
        # print(items)
    finally:
        # Zamknięcie przeglądarki
        driver.quit()