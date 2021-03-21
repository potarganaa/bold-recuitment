from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
import pytest
from ddt import ddt, data, unpack
import time

from bold_configuration import Configuration
from bold_login_page import LoginPage
from bold_main_page import MainPage

@ddt
class TestLoginPage:
    driver: WebDriver

    def setup_method(self):
        self.config = Configuration()
        self.driver = self.config.open_application()
        self.login_page = LoginPage(self.driver)
        self.main_page = MainPage(self.driver)

    def test_interview(self):
        file_name = "CV - TEST"

        self.login_page.log_in(username=self.config.DEFAULT_LOGIN,
                          password=self.config.DEFAULT_PASS)
        if_cv_test_present = self.main_page.is_cv_test_present()
        assert if_cv_test_present == True, f"File {file_name} cannot be found."

    def test_is_correct_sadface_error_present_for_locked_out_user(self, predef_user="locked"):
        self.login_page.log_in(username=self.config.USERS[predef_user]["username"],
                          password=self.config.USERS[predef_user]["password"])

        actual_error = self.login_page.get_epic_sadface_error_content_text()
        expected_error = self.config.LOCKED_OUT_USER_ERROR_TEXT

        assert actual_error == expected_error, f"Actual error text: '{actual_error}' is differed than expected error " \
                                               f"text: '{expected_error}'."

    @data(("bla", "blabla"), (" @#$$@# ", " $!@$ "), (5, 3))
    @unpack
    def test_is_correct_sadface_error_present_incorrect_login_data(self, username=None, password=None):
        self.login_page.log_in(username, password)

        actual_error = self.login_page.get_epic_sadface_error_content_text()
        expected_error = self.config.INCORRECT_LOGIN_DATA_ERROR_TEXT

        assert actual_error == expected_error, f"Actual error text: '{actual_error}' is differed than expected error " \
                                               f"text: '{expected_error}'."

    @data(("", ""), ("", "test"))
    @unpack
    def test_is_correct_sadface_error_present_missing_username(self, username=None, password=None):
        self.login_page.log_in(username, password)

        actual_error = self.login_page.get_epic_sadface_error_content_text()
        expected_error = self.config.MISSING_USERNAME_ERROR_TEXT

        assert actual_error == expected_error, f"Actual error text: '{actual_error}' is differed than expected error " \
                                               f"text: '{expected_error}'."

    @data(("test", ""), ("342", ""))
    @unpack
    def test_is_correct_sadface_error_present_missing_password(self, username=None, password=None):
        self.login_page.log_in(username, password)

        actual_error = self.login_page.get_epic_sadface_error_content_text()
        expected_error = self.config.MISSING_PASSWORD_ERROR_TEXT

        assert actual_error == expected_error, f"Actual error text: '{actual_error}' is differed than expected error " \
                                               f"text: '{expected_error}'."

    @data(("test", ""), ("", "test"), ("", ""))
    @unpack
    def test_is_sadface_error_can_be_closed(self, username=None, password=None):
        self.login_page.log_in(username, password)
        self.login_page.use_error_button()

        error_disappearance = self.login_page.is_epic_sadface_error_disappear()

        assert error_disappearance is True, "Sadface error does not dissapeard after close button has been used."

    def test_are_proper_login_credentials_displayed(self):
        page_login_credentials = self.login_page.get_login_credentials()

        assert page_login_credentials == self.config.USERS_CREDENTIALS_LIST, f"Credentials on page: {page_login_credentials} are different than proper credentials: {self.config.USERS_CREDENTIALS_LIST}."

    def test_are_proper_login_password_displayed(self):
        page_login_password = self.login_page.get_login_password()

        assert page_login_password == self.config.DEFAULT_PASS, f"Password on page: {page_login_password} are different than proper password: {self.config.DEFAULT_PASS}."

    def teardown_method(self):
        self.driver.quit()

    if __name__ == '__main__':
        pytest.main(args=[__file__])
