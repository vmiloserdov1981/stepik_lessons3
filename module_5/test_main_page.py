from pages.main_page import MainPage
import time
import pytest
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        # Подготовка
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        mainPage = MainPage(browser)
        mainPage.open()  # открываем страницу
        mainPage.should_be_login_link()  # Проверить, что есть ссылка, которая ведет на логин

        # Действия
        mainPage.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
        loginPage = LoginPage(browser)

        # Проверка
        # Вызываю класс should_be_login_page для проверок url, страниц логина и регистрации
        loginPage.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser)
        page.open()
        page.should_be_login_link()


class TestMainPage:
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        # Подготовка
        page = MainPage(browser)
        page.open()
        page.go_to_basket_page()

        # Действия
        page = BasketPage(browser)

        # Проверка
        page.should_be_no_items_in_basket()
        page.should_be_text_empty_basket()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        # Данные
        item_link = "coders-at-work_207/"

        # Подготовка
        product_page = ProductPage(browser, item_link)
        product_page.open()
        product_page.add_to_basket()

        # Действия
        product_page.go_to_basket_page()
        basket_page = BasketPage(browser)

        # Проверка
        basket_page.check_browser_url()
        basket_page.should_be_no_items_in_basket()
        basket_page.should_be_text_empty_basket()
