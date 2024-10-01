import pytest
from pages.login_page import LoginPage

@pytest.mark.skip
def test_login_page_loads_correctly(browser):
    login_page = LoginPage(browser)
    login_page.load()

    #* sluzy do odpakowania
    assert browser.find_element(*LoginPage.USERNAME_INPUT).is_clickable()
    assert browser.find_element(*LoginPage.PASSWORD_INPUT).is_clickable()
    assert browser.find_element(*LoginPage.LOGIN_BUTTON).is_clickable()


# Standard User: 1 przypadek testowy (poprawne logowanie).
# Locked Out User: 1 przypadek testowy (komunikat o zablokowanym koncie).
# Problem User: 1 przypadek testowy (logowanie z problemami).
# Performance Glitch User: 1 przypadek testowy (logowanie, ale wolne działanie).
# Error User: 1 przypadek testowy (błąd przy logowaniu).
# Visual User: 1 przypadek testowy (poprawne logowanie + sprawdzenie UI).

@pytest.mark.skip
@pytest.mark.login
@pytest.mark.standard_user
def test_login_standard_user(browser):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    assert 'inventory' in browser.current_url, f"Expected 'inventory' in URL, got {browser.current_url}"


@pytest.mark.skip
@pytest.mark.login
@pytest.mark.locked_out_user
def test_login_locked_out_user(browser):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login("locked_out_user", "secret_sauce")
    expected_error = 'Epic sadface: Sorry, this user has been locked out.'
    assert (login_page.get_error_communicate() == expected_error
            ), f"Expected {expected_error} in URL, got {login_page.get_error_communicate()}"


@pytest.mark.skip
@pytest.mark.login
@pytest.mark.no_username
def test_login_no_username(browser):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login("", "secret_sauce")
    expected_error = "Epic sadface: Username is required"

    assert (login_page.get_error_communicate() == expected_error
            ), f"Expected {expected_error} in URL, got {login_page.get_error_communicate()}"

@pytest.mark.skip
@pytest.mark.login
@pytest.mark.no_password
def test_login_no_username(browser):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login("random_string", "")
    expected_error = "Epic sadface: Password is required"

    assert (login_page.get_error_communicate() == expected_error
            ), f"Expected {expected_error} in URL, got {login_page.get_error_communicate()}"
    

@pytest.mark.parametrize("username, password", [("asd", "secret_sauce"), ("standard_user", "123")])
@pytest.mark.login
@pytest.mark.bad_credentials
def test_login_no_username(browser, username, password):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login(username, password)
    expected_error = "Epic sadface: Username and password do not match any user in this service"

    assert (login_page.get_error_communicate() == expected_error
            ), f"Expected {expected_error} in URL, got {login_page.get_error_communicate()}"
    
