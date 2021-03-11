import time
from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

class TestProductPage:
    def test_guest_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        time.sleep(1)
        product = page.get_product_name_and_price()
        page.add_to_basket()
        time.sleep(1)
        page.should_be_added_to_basket(product.get('product_name'))
        time.sleep(1)
        page.should_be_product_price(product.get('product_price'))
