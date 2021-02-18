from selenium import webdriver


main_page_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

string_email_address_locator = "#id_login-username"
string_password_locator = "#id_login-password"
login_button_locator = ".btn.btn-lg"
registration_result_failed_locator = "#login_form > div:nth-child(4)"
search_text = "Please enter a correct username and password. Note that both fields may be case-sensitive."
#search_text = "abc"

def login_fake_data():
    # Data
    false_email_address = "dfdfdgdgd@yandex.ru"
    false_password = "111111111$%@"

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)

        # Act
        email_data_entry = browser.find_element_by_css_selector(string_email_address_locator)
        email_data_entry.clear()
        email_data_entry.send_keys(false_email_address)

        password_entry = browser.find_element_by_css_selector(string_password_locator)
        password_entry.clear()
        password_entry.send_keys(false_password)

        login_button_entry = browser.find_element_by_css_selector(login_button_locator)
        login_button_entry.click()


        # Assert
        result_login_text_face_user = browser.find_element_by_css_selector(registration_result_failed_locator)
        assert search_text in result_login_text_face_user.text, \
            "An incorrect message is displayed to the fake user"

    finally:

        browser.quit()

login_fake_data()