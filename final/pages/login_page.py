from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, browser):
        self.page_url = "accounts/login"
        super().__init__(browser, BasePage.site_url + "/" + self.page_url)

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PROVE_PASS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BTN).click()

    def login_fake_user(self, false_email, false_password):
        self.browser.find_element(*LoginPageLocators.LOGIN_FORM_EMAIL_ADDRESS_LOCATOR).send_keys(false_email)
        self.browser.find_element(*LoginPageLocators.LOGIN_FORM_PASSWORD_LOCATOR).send_keys(false_password)
        self.browser.find_element(*LoginPageLocators.LOGIN_FORM_BUTTON_LOCATOR).click()

    def result_login_face_user(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_RESULT_FAILED_LOCATOR), "An incorrect message is displayed to the fake user"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert LoginPageLocators.login_url in self.browser.current_url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.login_form), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.register_form), "Register form is not presented"
