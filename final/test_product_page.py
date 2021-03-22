import time
import pytest
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


class TestProductPage:

    @pytest.mark.parametrize('promo_offer',
                             ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                              pytest.param("offer7", marks=pytest.mark.xfail), "offer8",
                              "offer9"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        # Данные
        link = f"coders-at-work_207/?promo={promo_offer}"
        page = ProductPage(browser, link)

        # Подготовка
        page.open()
        product = page.get_product_name_and_price()

        # Действия
        page.add_to_basket()

        # Проверка
        page.should_be_added_to_basket(product.get('product_name'))
        page.should_be_product_price(product.get('product_price'))

    @pytest.mark.xfail(reason="invalid test case")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        # Данные
        link = "coders-at-work_207/"
        page = ProductPage(browser, link)

        # Подготовка
        page.open()
        page.add_to_basket()

        # Проверка
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        # Данные
        link = "coders-at-work_207/"
        page = ProductPage(browser, link)

        # Подготовка
        page.open()

        # Проверка
        page.should_not_be_success_message()

    @pytest.mark.xfail(reason="invalid test case")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        # Данные
        link = "coders-at-work_207/"
        page = ProductPage(browser, link)

        # Подготовка
        page.open()

        # Действия
        page.add_to_basket()

        # Проверка
        page.should_be_disappeared()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        # Данные
        link = "coders-at-work_207/"
        page = ProductPage(browser, link)

        # Подготовка
        page.open()

        # Проверка
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        # Данные
        link = "coders-at-work_207/"
        page = ProductPage(browser, link)

        # Подготовка
        page.open()

        # Действия
        page.go_to_login_page()

        # Проверка
        login_page = LoginPage(browser)
        login_page.should_be_login_page()


@pytest.mark.user_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # Данные
        page = LoginPage(browser)

        # Подготовка
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())

        # Действия
        page.register_new_user(email, password)

        # Проверка
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        # Данные
        link = "coders-at-work_207/"
        page = ProductPage(browser, link)

        # Подготовка
        page.open()
        product = page.get_product_name_and_price()

        # Действия
        page.add_to_basket_without_calc()

        # Проверка
        page.should_be_added_to_basket(product.get('product_name'))
        page.should_be_product_price(product.get('product_price'))

    def test_user_cant_see_success_message(self, browser):
        # Данные
        link = "coders-at-work_207/"
        page = ProductPage(browser, link)

        # Подготовка
        page.open()

        # Проверка
        page.should_not_be_success_message()
