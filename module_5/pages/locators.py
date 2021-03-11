from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    login_url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    login_form = (By.CSS_SELECTOR, "#login_form > h2")
    register_form = (By.CSS_SELECTOR, "#register_form > h2")