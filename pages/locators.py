from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "a[href*='basket']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "form#register_form")
    REGISTRATION_EMAIL_INPUT = (By.CSS_SELECTOR, "input#id_registration-email")
    REGISTRATION_PASSWORD_INPUT = (By.CSS_SELECTOR, "input#id_registration-password1")
    REGISTRATION_CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "input#id_registration-password2")
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "div#messages > div.alert-success:nth-child(1) > div.alertinner strong")
    MESSAGE_PRODUCT_PRICE = (By.CSS_SELECTOR, "div#messages > div.alert-info > div.alertinner strong")
    PRODUCT_NAME= (By.CSS_SELECTOR, "article.product_page h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "article.product_page p.price_color")

class BasketPageLocators():
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
    PRODUCTS_CONTAINER_IN_BASKET = (By.CSS_SELECTOR, "form#add_to_basket_button")
