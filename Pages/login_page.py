from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "current URL is invalid"

    def should_be_login_form(self):
        # "*" используется потому что мы передаем кортеж (2 элемента: how(id or CSS of ...) и what(сам селектор))
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present on the page"

    def should_be_register_form(self):
        # "*" используется потому что мы передаем кортеж (2 элемента: how(id or CSS of ...) и what(сам селектор))
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not displayed"
