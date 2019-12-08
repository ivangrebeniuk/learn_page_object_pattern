from .Pages.login_page import LoginPage
import time


def test_verify_url(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()


def test_register_new_user(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    a = page.generate_new_email()
    page.register_new_user(a, "000000zzz")
    page.should_be_authorized_user()
    time.sleep(5)
