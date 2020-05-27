from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "header .basket-mini a.btn-default")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_page .product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_page .product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:first-child .alertinner")
    SUCCESS_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success:first-child .alertinner strong")
    SUCCESS_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner p:first-child strong")
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, ".product_page .product_main #add_to_basket_form button.btn-add-to-basket")


class BasketPageLocators():
    PRODUCTS_FORM = (By.CSS_SELECTOR, "#basket_formset")
    EMPTY_CONTENT = (By.CSS_SELECTOR, "#content_inner > p")
