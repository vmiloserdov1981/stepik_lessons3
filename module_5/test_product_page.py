import time
import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage


class TestProductPage:

    @pytest.mark.parametrize('promo_offer',
                             ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6", "offer7", "offer8",
                              "offer9"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        link = "coders-at-work_207/?promo={promo_offer}"
        page = ProductPage(browser, link)
        page.open()
        time.sleep(1)
        product = page.get_product_name_and_price()
        page.add_to_basket()
        time.sleep(1)
        page.should_be_added_to_basket(product.get('product_name'))
        time.sleep(1)
        page.should_be_product_price(product.get('product_price'))

    @pytest.mark.xfail(reason="invalid test case")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        link = "coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail(reason="invalid test case")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = "coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_be_disappeared()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser)
        login_page.should_be_login_page()


@pytest.mark.user_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        product = page.get_product_name_and_price()
        page.add_to_basket()
        page.should_be_added_to_basket(product.get('product_name'))
        page.should_be_product_price(product.get('product_price'))

    def test_user_cant_see_success_message(self, browser):
        link = "coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
