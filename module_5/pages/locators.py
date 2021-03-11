from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    login_url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    login_form = (By.CSS_SELECTOR, "#login_form > h2")
    register_form = (By.CSS_SELECTOR, "#register_form > h2")

class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".add-to-basket button")
    ADDED_PRODUCT_TEXT = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    BASKET_PRICE_TEXT = (By.CSS_SELECTOR, ".alertinner p strong")
    PRODUCT_NAME_TEXT = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE_TEXT = (By.CSS_SELECTOR, ".product_main .price_color")
