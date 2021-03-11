from pages.main_page import MainPage
import time
from pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        mainPage = MainPage(browser, link)
        mainPage.open()  # открываем страницу
        time.sleep(2)
        mainPage.should_be_login_link()  # Проверить, что есть ссылка, которая ведет на логин
        time.sleep(2)
        mainPage.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
        time.sleep(2)

        loginPage = LoginPage(browser, browser.current_url)
        loginPage.should_be_login_url()
        loginPage.should_be_login_form()
        loginPage.should_be_register_form()
