from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def __init__(self, browser, item_url, timeout=10):
        self.page_url = "catalogue"
        super().__init__(browser, ProductPage.site_url + "/" + self.page_url + "/" + item_url, timeout)

    def add_product_to_basket(self):
        self.click(*ProductPageLocators.ADD_TO_BASKET_BTN)

    def get_product_name(self):
        return self.get_element_text(*ProductPageLocators.PRODUCT_NAME_TEXT)

    def get_product_price(self):
        return self.get_element_text(*ProductPageLocators.PRODUCT_PRICE_TEXT)

    def check_basket_product_name_message(self, product_name):
        self.check_success_alert_message(f"{product_name} has been added to your basket.")

    def check_basket_total_price_message(self, product_price):
        self.check_info_alert_message(f"Your basket total is now {product_price}")

    def check_success_alert_message(self, message):
        messages = self.get_elements_text(*ProductPageLocators.ADDED_PRODUCT_TEXT)
        assert message in messages, f"Success message '{message}' is not presented"

    def check_info_alert_message(self, message):
        messages = self.get_elements_text(*ProductPageLocators.INFO_MESSAGE)
        assert message in messages, f"Info message '{message}' is not presented"

    def add_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()
        BasePage.solve_quiz_and_get_code(self)

    def add_to_basket_without_calc(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()

    def should_be_added_to_basket(self, product_name):
        assert product_name == self.browser.find_element(
            *ProductPageLocators.ADDED_PRODUCT_TEXT).text, "The name of the product differs"

    def should_be_product_price(self, product_price):
        assert product_price == self.browser.find_element(
            *ProductPageLocators.BASKET_PRICE_TEXT).text, "The price in the basket differs"

    def get_product_name_and_price(self):
        product = {}
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_TEXT).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_TEXT).text
        product['product_name'] = product_name
        product['product_price'] = product_price
        return product

    def add_product_to_favorites(self):
        add_product_to_favorites_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_FAVORITES)
        add_product_to_favorites_btn.click()

    # https://stepik.org/lesson/478334/step/5?unit=469293
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_PRODUCT_TEXT), \
            "Success message is presented, but should not be"

    # https://stepik.org/lesson/478334/step/5?unit=469293
    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_PRODUCT_TEXT), \
            "Success message is presented, but should not be"

    def should_be_product_successfully_add_to_favorites(self):
        assert self.is_element_present(
            *ProductPageLocators.TEXT_SUCCESSFUL_ADD_TO_FAVORITES), "Error. product not added to favorites"
