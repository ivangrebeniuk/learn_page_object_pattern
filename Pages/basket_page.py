from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_should_be_empty(self):
        empty_title = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TITLE)
        text = empty_title.text
        assert "Your basket is empty. Continue shopping" == text
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TITLE), \
            "Basket is not empty, but should be"

    def no_products_should_be_added(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_TO_BUY_NOW_TITLE), \
            "Items are in the basket, but they should not be"
