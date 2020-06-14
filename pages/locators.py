from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "form#register_form")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "div#messages > div.alert-success:nth-child(1) > div.alertinner strong")
    MESSAGE_PRODUCT_PRICE = (By.CSS_SELECTOR, "div#messages > div.alert-info > div.alertinner strong")
    PRODUCT_NAME= (By.CSS_SELECTOR, "article.product_page h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "article.product_page p.price_color")
    