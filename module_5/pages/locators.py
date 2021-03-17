from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-group>a[href*='basket']")
#    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

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

class BasketPageLocators():
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEMS_HEADER = (By.CSS_SELECTOR, ".basket-items")