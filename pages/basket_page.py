from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_products(self):
        assert not self.is_element_present(
            *BasketPageLocators.PRODUCTS_FORM), "PRODUCTS is presented, but should not be"

    def should_be_empty_message(self):
        assert self.is_element_present(
            *BasketPageLocators.EMPTY_CONTENT), "Empty message is not presented"
