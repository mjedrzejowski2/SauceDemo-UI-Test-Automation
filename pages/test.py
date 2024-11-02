from selenium import webdriver
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage
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
        cart_page = CartPage(driver)
        # results = inventory_page.get_all_products_prices()
        # print(results)  
        #       
        # names = inventory_page.get_all_product_names()
        # print(names)  
        #       
        # items = inventory_page.get_all_inventory_items()
        # print(items)

        # inventory_page.add_all_products_to_cart()
        # inventory_page.choose_sort_name_za()
        # time.sleep(2) 

        # inventory_page.choose_sort_price_high_low()
        # time.sleep(2) 

        # inventory_page.choose_sort_price_low_high()
        # time.sleep(2)

        # inventory_page.choose_sort_name_az()
        # time.sleep(2)
        inventory_page.click_cart()

        cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.first_name()
        time.sleep(2)
        checkout_page.click_continue_button()
        time.sleep(2)
        print(checkout_page.error_exists())
        print(checkout_page.get_error_communicate())
          

    finally:
        # Zamknięcie przeglądarki
        driver.quit()