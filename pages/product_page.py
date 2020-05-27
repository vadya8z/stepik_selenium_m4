from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    def add_product_to_cart(self):
        btn = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART)
        btn.click()

    def check_product_name(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        name_success = self.browser.find_element(*ProductPageLocators.SUCCESS_PRODUCT_NAME)
        # print('name=', name.text)
        # print('name_success=', name_success.text)
        assert name_success.text == name.text, "Name not found in success message"

    def check_product_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        price_success = self.browser.find_element(*ProductPageLocators.SUCCESS_PRODUCT_PRICE)
        # print('price=', price.text)
        # print('price_success=', price_success.text)
        assert price.text == price_success.text, "Price not found in success message"
