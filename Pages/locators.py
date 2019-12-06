from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.CSS_SELECTOR, ".btn-group > .btn:nth-child(1)")


class BasketPageLocators:
    EMPTY_BASKET_TITLE = (By.CSS_SELECTOR, "#content_inner > p")
    ITEMS_TO_BUY_NOW_TITLE = (By.CSS_SELECTOR, ".h3:nth-child(1)")


class MainPageLocators:
    pass

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
