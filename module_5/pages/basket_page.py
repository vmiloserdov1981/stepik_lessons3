from .base_page import BasePage
from .locators import BasketPageLocators



class BasketPage(BasePage):

    def should_be_no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS_HEADER), \
            "There are some items in the basket"

    def should_be_text_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), \
            "The basket is not empty"