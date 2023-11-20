import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from time import sleep


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page() # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url) # переназначаем объект page
    login_page.should_be_login_page() # выполняем проверку урла, форм регистрации и логина (см. login_page.py)


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, browser.current_url)
    page.should_not_be_items_in_the_basket()
    page.should_be_a_message_that_the_basket_is_empty()

