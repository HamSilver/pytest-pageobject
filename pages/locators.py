from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_TITLE = (By.CLASS_NAME, "basket-title")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASS1 = (By.ID, "id_registration-password1")
    REGISTER_PASS2 = (By.ID, "id_registration-password2")
    REGISTER_SUBMIT = (By.CSS_SELECTOR, "#register_form button")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    PRICE_IN_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alertinner p strong")
    NAME_IN_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages div:first-child .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:first-child")
