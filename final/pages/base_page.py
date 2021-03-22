import math
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators
from .locators import MainPageLocators
from .locators import ProductPageLocators

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.page_url = ""
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(
            timeout)  # В конструктор BasePage добавим команду для неявного ожидания со значением по умолчанию в 10

    site_url = "http://selenium1py.pythonanywhere.com"

    def get_element_text(self, how, what):
        element = self.browser.find_element(how, what)
        return element

    def check_browser_url(self):
        assert self.browser.current_url.contains(BasePage.site_url)
        assert self.browser.current_url.contains(self.page_url)

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.GO_TO_BASKET_BTN)
        link.click()

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def get_product_name_and_price_search_results(self):
        product = {}
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_TEXT_SEARCH).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_TEXT_SEARCH).text
        product['product_name'] = product_name
        product['product_price'] = product_price
        return product

    def should_be_added_to_basket_search_results(self, product_name):
        assert product_name == self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_TEXT_SEARCH).text, "The name of the product differs"

    def should_be_product_price_search_results(self, product_price):
        assert product_price == self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE_TEXT_SEARCH).text, "The price in the basket differs"

    def result_invalid_search_request(self):
        assert self.is_element_present(
            *MainPageLocators.INVALID_SEARCH_QUERY_TEXT), "An incorrect message is displayed to the fake user"

    def write_in_search_bar_from_main_page(self, name_existing_product):
        self.browser.find_element(*MainPageLocators.SEARCH_LINE).send_keys(name_existing_product)
        self.browser.find_element(*MainPageLocators.FIND_BTN).click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def get_element_text(self, how, what):
        element = self.browser.find_element(how, what)
        return element.text

    def get_elements_text(self, how, what):
        elements = self.browser.find_elements(how, what)
        return [element.text for element in elements]

    def open(self):
        self.browser.get(self.url)

    # реализуем метод is_element_present, в котором будем перехватывать исключение
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    # проверяет, что элемент не появляется на странице в течение заданного времени
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    # проверить, что какой-то элемент исчезает, то следует воспользоваться явным ожиданием
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    # Посчитать результат математического выражения и ввести ответ
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
