from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_item_to_basket(self):
        self.browser.implicitly_wait(5)
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def check_allert_after_adding_item_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_ADDED_MESSAGE), \
            "The message about adding an item to basket is not displayed!"

    def check_name_and_price_of_item_in_basket(self):
        self.browser.implicitly_wait(5)
        try:
            item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
            item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
            item_added_message = self.browser.find_element(*ProductPageLocators.ITEM_ADDED_MESSAGE).text
            basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        finally:
            assert item_name in item_added_message, "Wrong item added to cart!"
            assert item_price in basket_price, "The price of the item in the basket does not match the original price of the item!"