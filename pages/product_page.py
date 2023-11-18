from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_item_to_basket(self):
        self.browser.implicitly_wait(5)
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def check_allert_after_adding_item_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_ADDED_MESSAGE), \
            print(f"\nTest failed: The message about adding an item to basket is not displayed!")

    def check_name_and_price_of_item_in_basket(self):
        self.browser.implicitly_wait(5)
        try:
            item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text #
            item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text #
            item_name_in_message = self.browser.find_element(*ProductPageLocators.ITEM_NAME_IN_MESSAGE).text
            basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text #
        finally:
            assert item_name == item_name_in_message, print(f"\nTest failed: Wrong item added to basket!")
            assert item_price in basket_price, \
                print(f"\n Test failed: The price of the item in the basket does not match the original price of the item!")