import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.skip
@pytest.mark.inventory_page
def test_add_all_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_all_products_to_cart()

    assert (int(inventory_page.get_number_in_cart()) == 6
            ), f"Expected 6 products in cart, got {inventory_page.get_number_in_cart()}."  

    inventory_page.add_all_products_to_cart()

    assert (int(inventory_page.get_number_in_cart()) == 0
            ), f"Expected 0 products in cart, got {inventory_page.get_number_in_cart()}."  
    
@pytest.mark.inventory_page
def test_sort_az(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page = InventoryPage(driver)
    inventory_page.choose_sort_name_az()

    product_names = inventory_page.get_all_product_names()
    sorted_product_names = sorted(product_names)

    for x in range(len(product_names)-1):
        assert (product_names[x] == sorted_product_names[x]
        ), f"Product {product_names[x]} is not sorted correctly, expected {sorted_product_names[x]}"


@pytest.mark.inventory_page
def test_sort_za(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page = InventoryPage(driver)
    inventory_page.choose_sort_name_za()

    product_names = inventory_page.get_all_product_names()
    sorted_product_names = sorted(product_names, reverse=True)

    for x in range(len(product_names)-1):
        assert (product_names[x] == sorted_product_names[x]
        ), f"Product {product_names[x]} is not sorted correctly, expected {sorted_product_names[x]}"

@pytest.mark.inventory_page
def test_sort_price_high_low(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page = InventoryPage(driver)
    inventory_page.choose_sort_price_high_low()

    product_prices = inventory_page.get_all_products_prices()

    for x in range(len(product_prices)-1):
        assert (float(product_prices[x]) >= float(product_prices[x+1])
        ), f"Product price {product_prices[x]} is lower than {product_prices[x+1]}"

@pytest.mark.inventory_page
def test_sort_price_low_high(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page = InventoryPage(driver)
    inventory_page.choose_sort_price_low_high()

    product_prices = inventory_page.get_all_products_prices()

    for x in range(len(product_prices)-1):
        assert (float(product_prices[x]) <= float(product_prices[x+1])
        ), f"Product price {product_prices[x]} is higher than {product_prices[x+1]}"