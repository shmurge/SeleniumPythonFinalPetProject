import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
from time import sleep


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.solve_quiz_and_get_code()
    page.check_allert_after_adding_item_in_basket()
    page.check_name_and_price_of_item_in_basket()




