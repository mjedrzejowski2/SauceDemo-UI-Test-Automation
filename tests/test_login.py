import pytest
from pages.login_page import LoginPage

@pytest.mark.skip
def test_login_page_loads_correctly(browser):
    login_page = LoginPage(browser)
    login_page.load()

    #* sluzy do odpakowania
    assert browser.find_element(*LoginPage.USERNAME_INPUT).is_displayed()
    assert browser.find_element(*LoginPage.PASSWORD_INPUT).is_displayed()
    assert browser.find_element(*LoginPage.LOGIN_BUTTON).is_displayed()


# Standard User: 1 przypadek testowy (poprawne logowanie).
# Locked Out User: 1 przypadek testowy (komunikat o zablokowanym koncie).
# Problem User: 1 przypadek testowy (logowanie z problemami).
# Performance Glitch User: 1 przypadek testowy (logowanie, ale wolne działanie).
# Error User: 1 przypadek testowy (błąd przy logowaniu).
# Visual User: 1 przypadek testowy (poprawne logowanie + sprawdzenie UI).

@pytest.mark.login
@pytest.mark.standard_user
def test_login_standard_user(browser):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    assert 'inventory' in browser.current_url, f"Expected 'inventory' in URL, got {browser.current_url}"


@pytest.mark.login
@pytest.mark.locked_out_user
def test_login_locked_out_user(browser):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login("locked_out_user", "secret_sauce")

    assert login_page.get_error_communicate() == 'Epic sadface: Sorry, this user has been locked out.'
