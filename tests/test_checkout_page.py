import pytest 
from resources import credentials
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage

@pytest.mark.checkout_page
def test_checkout_information(driver):
    login_page = LoginPage(driver)
    login_page.login(credentials.standard_user, credentials.correct_password)
    inventory_page = InventoryPage(driver)
    inventory_page.click_cart()
    cart_page = CartPage(driver)
    cart_page.click_checkout()
    checkout_page = CheckoutPage(driver)
    checkout_page.click_continue_button()
    assert checkout_page.get_error_communicate() == "Error: First Name is required"

    checkout_page.first_name()
    checkout_page.click_continue_button()
    assert checkout_page.get_error_communicate() == "Error: Last Name is required"

    checkout_page.last_name()
    checkout_page.click_continue_button()
    assert checkout_page.get_error_communicate() == "Error: Postal Code is required"

    checkout_page.postal_code()
    checkout_page.click_continue_button()
    assert "checkout-step-two" in driver.current_url

@pytest.mark.checkout_page
def test_checkout_cancel(driver):
    login_page = LoginPage(driver)
    login_page.login(credentials.standard_user, credentials.correct_password)
    inventory_page = InventoryPage(driver)
    inventory_page.click_cart()
    cart_page = CartPage(driver)
    cart_page.click_checkout()
    checkout_page = CheckoutPage(driver)
    checkout_page.click_cancel_button()

    assert "cart" in driver.current_url