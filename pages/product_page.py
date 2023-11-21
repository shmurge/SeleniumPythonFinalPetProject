from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_basket(self):
        # добавить товар в корзину
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def check_alert_after_adding_item_in_basket(self):
        # проверка отображения сообщения об успешном добавлении товара в корзину
        assert self.is_element_present(*ProductPageLocators.ITEM_ADDED_MESSAGE), \
            "Test failed: The message about adding an item to basket is not displayed!"

    def check_name_and_price_of_item_in_basket(self):
        # проверка соответствия наименования и цены товара до и после добавления в корзину
        try:
            item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text #
            item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text #
            item_name_in_message = self.browser.find_element(*ProductPageLocators.ITEM_NAME_IN_MESSAGE).text
            basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text #
        finally:
            assert item_name == item_name_in_message,"Test failed: Wrong item added to basket!"
            assert item_price in basket_price, \
                "Test failed: The price of the item in the basket does not match the original price of the item!"

    def should_not_be_success_message(self):
        # проверка отсутствия сообщения об успешном добавлении товара в корзину
        assert self.is_not_element_present(*ProductPageLocators.ITEM_ADDED_MESSAGE), \
            "The message is presented, but should not be!"

    def should_disappear_from_the_page(self):
        # проверка: сообщение о добавлении товара исчезает со страницы
        assert self.is_disappeared(*ProductPageLocators.ITEM_ADDED_MESSAGE), \
            "The message did not disappear within the allotted time!"