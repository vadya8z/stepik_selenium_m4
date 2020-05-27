from .pages.product_page import ProductPage
import time
import pytest

@pytest.fixture(scope="function")
def link():
    return 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()  # Добавляем в корзину
    page.solve_quiz_and_get_code()  # Вводим проверочный код
    page.should_not_be_success_message_is_not_el()  # Проверяем цену продукта

def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message_is_not_el()  # Проверяем цену продукта

def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()  # Добавляем в корзину
    page.solve_quiz_and_get_code()  # Вводим проверочный код
    page.should_not_be_success_message_is_disappeared()  # Проверяем цену продукта
