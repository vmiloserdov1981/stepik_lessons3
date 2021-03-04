import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    """Опции командной строки.
    В командную строку передается параметр вида '--language="es" или другой язык'
    По умолчанию передается параметр, включающий английский интерфейс в браузере
    Запуск теста осуществляется, например, с русским языком так:  pytest --language=ru test_items.py
    """
    parser.addoption('--language', action='store', default='en', help='Choose language')


@pytest.fixture(scope="function")
def browser(request):
    #  В переменную user_language передается параметр из командной строки
    user_language = request.config.getoption('language')

    # Инициализируются опции браузера - используется класс Options и метод add_experimental_option
    options = Options()

    # В опции вебдрайвера передаем параметр из командной строки
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)

    browser.implicitly_wait(5)
    yield browser
    browser.quit()