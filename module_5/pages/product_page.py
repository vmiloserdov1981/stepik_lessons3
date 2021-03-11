from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()
        BasePage.solve_quiz_and_get_code(self)

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