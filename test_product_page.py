from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time
import pytest

@pytest.mark.parametrize('promo_link_part', ["?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3", 
    "?promo=offer4", "?promo=offer5", "?promo=offer6", pytest.param("?promo=offer7", marks=pytest.mark.xfail), "?promo=offer8", "?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, promo_link_part):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo_link_part}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()

    product_name_expected = page.get_product_name()
    product_price_expected = page.get_product_price()

    page.add_to_basket()

    page.solve_quiz_and_get_code()

    page.should_be_success_message()

    page.check_message_product_name(product_name_expected)
    page.check_message_product_price(product_price_expected)

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_to_basket()
    page.should_disappear_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products_in_cart()
    basket_page.should_be_empty_cart_text()
