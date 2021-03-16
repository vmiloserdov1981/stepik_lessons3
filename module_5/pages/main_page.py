from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    #заглушка, так как все методы реализованы в base_page.py
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
