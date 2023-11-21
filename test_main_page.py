import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        # гость может перейти на страницу логина с главной страницы
        link = "http://selenium1py.pythonanywhere.com/en-gb/"
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page() # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url) # переназначаем объект page
        login_page.should_be_login_page() # выполняем проверку урла, форм регистрации и логина (см. login_page.py)

    def test_guest_should_see_login_link(self, browser):
        # гость должен видеть ссылку на логин с главной страница
        link = "http://selenium1py.pythonanywhere.com/en-gb/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link() # проверяем, что ссылка на логин отображается


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    # у гостя не должно быть товаров в корзине (если он их не добавлял) при переходе в корзину со страницы товара
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, browser.current_url) # переназначаем объект page
    page.should_not_be_items_in_the_basket() # проверяем, что в корзине нет товаров
    page.should_be_a_message_that_the_basket_is_empty() # проверяем, наличие сообщения о пустой корзине

