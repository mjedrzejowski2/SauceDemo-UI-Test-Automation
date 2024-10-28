import pytest
from pages.login_page import LoginPage

@pytest.mark.login
def test_login_page_loads_correctly(driver):
    login_page = LoginPage(driver)
    login_page.load_site()

    #* sluzy do odpakowania
    assert driver.find_element(*login_page.USERNAME_INPUT).is_displayed()
    assert driver.find_element(*login_page.PASSWORD_INPUT).is_displayed()
    assert driver.find_element(*login_page.LOGIN_BUTTON).is_displayed()

@pytest.mark.login
@pytest.mark.standard_user
def test_login_standard_user(driver):
    login_page = LoginPage(driver)
    login_page.load_site()
    login_page.login("standard_user", "secret_sauce")

    assert 'inventory' in driver.current_url, f"Expected 'inventory' in URL, got {driver.current_url}"


@pytest.mark.login
@pytest.mark.locked_out_user
def test_login_locked_out_user(driver):
    login_page = LoginPage(driver)
    login_page.load_site()
    login_page.login("locked_out_user", "secret_sauce")
    expected_error = 'Epic sadface: Sorry, this user has been locked out.'
    assert (login_page.get_error_communicate() == expected_error
            ), f"Expected {expected_error} in URL, got {login_page.get_error_communicate()}"

@pytest.mark.login
@pytest.mark.no_username
def test_login_no_username(driver):
    login_page = LoginPage(driver)
    login_page.login("", "secret_sauce")
    expected_error = "Epic sadface: Username is required"

    assert (login_page.get_error_communicate() == expected_error
            ), f"Expected {expected_error} in URL, got {login_page.get_error_communicate()}"
    
@pytest.mark.login
@pytest.mark.no_password
def test_login_no_username(driver):
    login_page = LoginPage(driver)
    login_page.login("random_string", "")
    expected_error = "Epic sadface: Password is required"

    assert (login_page.get_error_communicate() == expected_error
            ), f"Expected {expected_error} in URL, got {login_page.get_error_communicate()}"
    
@pytest.mark.skip
@pytest.mark.parametrize("username, password", [("asd", "secret_sauce"), ("standard_user", "123")])
@pytest.mark.login
@pytest.mark.bad_credentials
def test_login_no_username(driver, username, password):
    login_page = LoginPage(driver)
    login_page.login(username, password)
    expected_error = "Epic sadface: Username and password do not match any user in this service"

    assert (login_page.get_error_communicate() == expected_error
            ), f"Expected {expected_error} in URL, got {login_page.get_error_communicate()}"
    
