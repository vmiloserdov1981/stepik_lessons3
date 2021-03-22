import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    """Опции командной строки.
    В командную строку передается параметр вида '--language="es" или другой язык'
    По умолчанию передается параметр, включающий английский интерфейс в браузере
    Запуск теста осуществляется, например, с русским языком так:  pytest --language=ru test_items.py
    """
    parser.addoption('--language', action='store', default='en', help='Choose language')

    parser.addoption('--browser', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    user_language = request.config.getoption('language')

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        print("Browser {} still is not implemented".format(browser_name))
    yield browser
    print("\nquit browser..")
    # получаем переменную с текущей датой и временем в формате ГГГГ-ММ-ДД_ЧЧ-ММ-СС
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    # делаем скриншот с помощью команды Selenium'а и сохраняем его с именем "screenshot-ГГГГ-ММ-ДД_ЧЧ-ММ-СС"
    browser.save_screenshot('Screenshots/screenshot-%s.png' % now)
    browser.quit()