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

    # https://stepik.org/lesson/478334/step/5?unit=469293
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_PRODUCT_TEXT), \
            "Success message is presented, but should not be"

    # https://stepik.org/lesson/478334/step/5?unit=469293
    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_PRODUCT_TEXT), \
            "Success message is presented, but should not be"