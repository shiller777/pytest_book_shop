from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_cart_text(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "Empty basket text is not presented"

    def should_not_be_products_in_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_CONTAINER_IN_BASKET), \
        "Products are presented in cart, but should not be"