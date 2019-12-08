from .base_page import BasePage
from .locators import LoginPageLocators
import time


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

    def generate_new_email(self):
        email = str(time.time()) + "@email.com"
        return email

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD)
        password_field.send_keys(password)
        confirm_password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD)
        confirm_password_field.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()




