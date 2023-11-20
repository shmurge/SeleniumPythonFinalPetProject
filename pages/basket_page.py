from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_a_message_that_the_basket_is_empty(self):
        self.browser.implicitly_wait(5)
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Test failed: The message that the basket is empty is not displayed!"

    def should_not_be_items_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_TO_BUY), \
            "There are items in the basket, but they shouldn't be there!"
