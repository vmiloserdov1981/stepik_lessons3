from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-group>a[href*='basket']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    SEARCH_LINE = (By.CSS_SELECTOR, "#id_q")
    FIND_BTN = (By.CSS_SELECTOR, "input.btn.btn-default")
    INVALID_SEARCH_QUERY_TEXT = (By.CSS_SELECTOR, "div.container-fluid.page p")

class LoginPageLocators():
    login_url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    login_form = (By.CSS_SELECTOR, "#login_form > h2")
    register_form = (By.CSS_SELECTOR, "#register_form > h2")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PROVE_PASS = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BTN = (By.NAME, "registration_submit")

    LOGIN_FORM_EMAIL_ADDRESS_LOCATOR = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_FORM_PASSWORD_LOCATOR = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_FORM_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".btn.btn-lg")
    REGISTRATION_RESULT_FAILED_LOCATOR = (By.CSS_SELECTOR, "#login_form > div:nth-child(4)")


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".add-to-basket button")
    ADDED_PRODUCT_TEXT = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    BASKET_PRICE_TEXT = (By.CSS_SELECTOR, ".alertinner p strong")
    PRODUCT_NAME_TEXT = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE_TEXT = (By.CSS_SELECTOR, ".product_main .price_color")
    INFO_MESSAGE = (By.XPATH, "//div[contains(@class, 'alert-info')] //p[not(.//a)]")
    PRODUCT_NAME_TEXT_SEARCH = (By.CSS_SELECTOR, "#default > div.container-fluid.page > div > div > div > section > div > ol > li > article > h3 > a")
    PRODUCT_PRICE_TEXT_SEARCH = (By.CSS_SELECTOR, "p.price_color")


class BasketPageLocators():
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEMS_HEADER = (By.CSS_SELECTOR, ".basket-items")
