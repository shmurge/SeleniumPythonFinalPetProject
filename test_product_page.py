import pytest
from .pages.product_page import ProductPage
from time import sleep



@pytest.mark.parametrize('link',
                         ["http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"])
def test_guest_can_add_product_to_basket(browser, link):
    link = link
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.solve_quiz_and_get_code() # запускаем функцию для расчета значения из всплывающего алерта
    page.check_allert_after_adding_item_in_basket() # проверка наличия алерта о добавлении товара в корзину
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
def test_guest_can_add_any_products_to_basket(browser, link):
    link = link
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.solve_quiz_and_get_code() # запускаем функцию для расчета значения из всплывающего алерта
    page.check_allert_after_adding_item_in_basket() # проверка наличия алерта о добавлении товара в корзину
    page.check_name_and_price_of_item_in_basket() # проверка цены и наименования товара после добавления в корзину


