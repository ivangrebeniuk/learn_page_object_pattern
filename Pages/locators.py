from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form > h2")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form > h2")


class BookPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".active:nth-child(5)")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, ".alert:nth-child(1) strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color:nth-child(2)")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alertinner > p > strong")
    PRODUCT_SUCCESSFULLY_ADDED_IN_BASKET = (By.CSS_SELECTOR, ".alert:nth-child(1) > .alertinner")
