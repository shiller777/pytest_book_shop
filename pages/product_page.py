from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_name()
        self.should_be_product_price()
        self.should_be_add_to_cart_button()
        
    def should_be_success_message(self):
        self.should_be_message_product_name()
        self.should_be_message_product_price()

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name not found on product page"

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price not found on product page"

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), "'Add to cart' button not found on product page"

    def should_be_message_product_name(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRODUCT_NAME), "Product name not found in success message"

    def should_be_message_product_price(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRODUCT_PRICE), "Product price not found in success message"
        
    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def get_product_name(self):
        product_name_link = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name_link.text

    def get_product_price(self):
        product_price_link = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price_link.text

    def get_message_product_name(self):
        message_product_name_link = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME)
        return message_product_name_link.text

    def get_message_product_price(self):
        message_product_price_link = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_PRICE)
        return message_product_price_link.text

    def check_message_product_name(self):
        product_name_expected = self.get_product_name()
        product_name_actual = self.get_message_product_name()
        assert product_name_actual == product_name_expected, f"Product names don't match. Expected <{product_name_expected}>, found <{product_name_actual}>"

    def check_message_product_price(self):
        product_price_expected = self.get_product_price()
        product_price_actual = self.get_message_product_price()
        assert product_price_actual == product_price_expected, f"Product prices don't match. Expected <{product_price_expected}>, found <{product_price_actual}>"
