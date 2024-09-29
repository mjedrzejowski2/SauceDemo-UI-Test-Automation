import pytest
from pages.login_page import LoginPage

def test_login_page_loads_correctly(browser):
    login_page = LoginPage(browser)
    login_page.load()

    assert browser.find_element(*LoginPage.USERNAME_INPUT).is_displayed()
    assert browser.find_element(*LoginPage.PASSWORD_INPUT).is_displayed()
    assert browser.find_element(*LoginPage.LOGIN_BUTTON).is_displayed()




# def test_login_page(browser):
#     login_page = LoginPage(browser)
#     login_page.load()