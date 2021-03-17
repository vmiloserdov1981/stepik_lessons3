from pages.main_page import MainPage
import time
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


class TestMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        mainPage = MainPage(browser, link)
        mainPage.open()  # открываем страницу
        time.sleep(1)
        mainPage.should_be_login_link()  # Проверить, что есть ссылка, которая ведет на логин
        time.sleep(1)
        mainPage.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
        time.sleep(1)

        loginPage = LoginPage(browser, browser.current_url)
        #Вызываю класс should_be_login_page для проверок url, страниц логина и регистрации
        loginPage.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        time.sleep(1)
        page.go_to_basket_page()
        time.sleep(1)
        page = BasketPage(browser, browser.current_url)
        page.should_be_no_items_in_basket()
        page.should_be_text_empty_basket()
        time.sleep(1)

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = MainPage(browser, link)
        page.open()
        time.sleep(1)
        page.go_to_basket_page()
        time.sleep(1)
        page = BasketPage(browser, browser.current_url)
        page.should_be_no_items_in_basket()
        page.should_be_text_empty_basket()
        time.sleep(1)


