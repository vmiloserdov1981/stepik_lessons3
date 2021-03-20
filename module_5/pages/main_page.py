from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    def __init__(self, browser):
        self.page_url = ""
        super().__init__(browser, MainPage.site_url)
