from .base_page import BasePage
from .locators import BookPageLocators
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math


class ProductPage(BasePage):

    def add_to_basket(self):
        add_to_basket = self.browser.find_element(*BookPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket.click()

    def get_product_name(self):
        book_name = self.browser.find_element(*BookPageLocators.PRODUCT_NAME)
        expected = book_name.text
        book_name_after_adding_to_basket = self.browser.find_element(*BookPageLocators.PRODUCT_NAME_IN_BASKET)
        actual = book_name_after_adding_to_basket.text
        assert actual == expected, "Wrong book title is displayed after adding to basket"

    def get_product_price(self):
        product_price = self.browser.find_element(*BookPageLocators.PRODUCT_PRICE)
        expected = product_price.text
        product_price_after_adding_to_basket = self.browser.find_element(*BookPageLocators.PRODUCT_PRICE_IN_BASKET)
        actual = product_price_after_adding_to_basket.text
        assert expected == actual, "Wrong product price after adding to basket"

    def should_be_added_to_basket(self):
        self.get_product_name()
        self.get_product_price()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BookPageLocators.PRODUCT_SUCCESSFULLY_ADDED_IN_BASKET), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*BookPageLocators.PRODUCT_SUCCESSFULLY_ADDED_IN_BASKET), \
            "Success message disappeared, but should not be"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
