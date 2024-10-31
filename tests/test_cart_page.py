import pytest
from resources import credentials
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

@pytest.mark.cart_page
def test_continue_shopping(driver):
    login_page = LoginPage(driver)
    login_page.login(credentials.standard_user, credentials.correct_password)
    inventory_page = InventoryPage(driver)
    inventory_page.click_cart()
    cart_page = CartPage(driver)
    cart_page.click_continue_shopping()

    assert len(inventory_page.get_all_inventory_items()) > 0

@pytest.mark.cart_page
def test_checkout(driver):
    login_page = LoginPage(driver)
    login_page.login(credentials.standard_user, credentials.correct_password)

    inventory_page = InventoryPage(driver)
    inventory_page.click_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

@pytest.mark.cart_page
def test_remove_button(driver):
    login_page = LoginPage(driver)
    login_page.login(credentials.standard_user, credentials.correct_password)

    inventory_page = InventoryPage(driver)
    inventory_page.add_all_products_to_cart()
    inventory_page.click_cart()

    cart_page = CartPage(driver)
    cart_page.remove_all_products()

    assert int(inventory_page.get_number_in_cart()) == 0 



