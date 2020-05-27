from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time
import pytest


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
#@pytest.mark.skip(reason="skip test")
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    # print('link=', link)
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()  # Добавляем в корзину
    page.solve_quiz_and_get_code()  # Вводим проверочный код
    page.check_product_name()  # Проверяем название продукта
    page.check_product_price()  # Проверяем цену продукта
    # time.sleep(5)


@pytest.mark.skip(reason="skip test")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()  # Добавляем в корзину
    page.solve_quiz_and_get_code()  # Вводим проверочный код
    page.should_not_be_success_message_is_not_el()


@pytest.mark.skip(reason="skip test")
def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message_is_not_el()


@pytest.mark.skip(reason="skip test")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()  # Добавляем в корзину
    page.solve_quiz_and_get_code()  # Вводим проверочный код
    page.should_not_be_success_message_is_disappeared()


@pytest.mark.skip(reason="skip test")
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


# @pytest.mark.skip(reason="skip test")
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()


# @pytest.mark.skip(reason="skip test")
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)  # Переходим на страницу корзины
    basket_page.should_not_be_products()  # проверяем есть ли продукты
    basket_page.should_be_empty_message()  # проверяем сообщение пустой корзины


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + 'somepass'
        ppage = ProductPage(browser, link)
        ppage.open()
        ppage.go_to_login_page()  # Переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)  # Переходим на страницу логина
        login_page.should_be_login_page()  # проверяем находимся ли на странице логина
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()
        # time.sleep(5)

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message_is_not_el()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_cart()  # Добавляем в корзину
        page.solve_quiz_and_get_code()  # Вводим проверочный код
        page.check_product_name()  # Проверяем название продукта
        page.check_product_price()  # Проверяем цену продукта
