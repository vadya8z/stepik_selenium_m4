from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_page .product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_page .product_main .price_color")
    SUCCESS_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success:first-child .alertinner strong")
    SUCCESS_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner p:first-child strong")
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, ".product_page .product_main #add_to_basket_form button.btn-add-to-basket")
