import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="class", autouse=True) # регистрация нового пользователя и проверка, что он залогинен
    def setup(self, browser):
        email = str(time.time()) + "@wiroute.com" # генерирует рандомный email
        password = "123Qwerty&"
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password) # регистрация нового пользователя
        page.should_be_authorized_user() # проверка, что пользователь авторизован

    def test_user_cant_see_success_message(self, browser):
        # при переходе в корзину юзер не должен видеть сообщение об успешном добавлении товара
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()  # открываем страницу
        page.should_not_be_success_message() # проверка отсутствия сообщения

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        # юзер может добавить товар в корзину
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()  # открываем страницу
        page.add_item_to_basket()  # добавляем товар в корзину
        page.check_alert_after_adding_item_in_basket()  # проверка наличия алерта о добавлении товара в корзину
        page.check_name_and_price_of_item_in_basket()  # проверка цены и наименования товара после добавления в корзину


@pytest.mark.parametrize('link',
                         ["http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    # гость может добавить товар в корзину
    link = link
    page = ProductPage(browser, link)
    page.open() # открываем страницу
    page.add_item_to_basket() # добавляем товар в корзину
    page.solve_quiz_and_get_code() # запускаем функцию для расчета значения из всплывающего алерта
    page.check_alert_after_adding_item_in_basket() # проверка наличия алерта о добавлении товара в корзину
    page.check_name_and_price_of_item_in_basket() # проверка цены и наименования товара после добавления в корзину


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_any_products_to_basket_promo(browser, link):
    # промо акция (гость может добавить товары в корзину)
    link = link
    page = ProductPage(browser, link)
    page.open() # открываем страницу
    page.add_item_to_basket() # добавляем товар в корзину
    page.solve_quiz_and_get_code() # запускаем функцию для расчета значения из всплывающего алерта
    page.check_alert_after_adding_item_in_basket() # проверка наличия алерта о добавлении товара в корзину
    page.check_name_and_price_of_item_in_basket() # проверка цены и наименования товара после добавления в корзину


@pytest.mark.xfail
@pytest.mark.negative
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # [негативный тест] гость добавил товар в корзину и не видит сообщение об успешном добавлении товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open() # открываем страницу
    page.add_item_to_basket()  # добавляем товар в корзину
    page.solve_quiz_and_get_code()  # запускаем функцию для расчета значения из всплывающего алерта
    page.should_not_be_success_message() # проверяем, что нет сообщения об успешном добавлении товара в корзину


def test_guest_cant_see_success_message(browser):
    # при переходе в корзину гость не должен видеть сообщение об успешном добавлении товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open() # открываем страницу
    page.should_not_be_success_message() # проверяем, что нет сообщения об успешном добавлении товара в корзину


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    # [негативный тест] сообщение об успешном добавлении товара в корзину исчезает, спустя определенное время
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open() # открываем страницу
    page.add_item_to_basket()  # добавляем товар в корзину
    page.solve_quiz_and_get_code()  # запускаем функцию для расчета значения из всплывающего алерта
    page.should_disappear_from_the_page() # проверяем, что сообщение об успешном добавлении товара в корзину исчезает с дисплея


def test_guest_should_see_login_link_on_product_page(browser):
    # гость должен видеть ссылку на логин на странице товара
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link() # проверяем, что ссылка на логин отображается


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    # гость может перейти на страницу логина со страницы товара
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page() # проверяем, что гость может перейти на страницу логина


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # у гостя не должно быть товаров в корзине (если он их не добавлял) при переходе в корзину со страницы товара
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page() # переходим на страницу корзины
    page = BasketPage(browser, browser.current_url)
    page.should_not_be_items_in_the_basket() # проверяем, что в корзине нет товаров
    page.should_be_a_message_that_the_basket_is_empty() # проверяем, наличие сообщения о пустой корзине
