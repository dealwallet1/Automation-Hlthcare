
from pages.login_page import LoginPage
from utils.data_reader import read_test_data
from locators.login_locators import LoginLocators

data = read_test_data("test_data/login_data.json")


class TestLogin:

    def test_valid_login(self, page):
        login = LoginPage(page)
        login.login(
            data["valid_user"]["email"],
            data["valid_user"]["password"]
        )
        assert "member" in page.url


    def test_invalid_login(self, page):
        login = LoginPage(page)
        login.login(
            data["invalid_user"]["email"],
            data["invalid_user"]["password"]
        )

        assert login.is_error_visible(LoginLocators.INVALID_CREDENTIALS)


    def test_empty_email_password(self, page):
        login = LoginPage(page)
        login.login("", "")

        assert login.is_error_visible(LoginLocators.EMAIL_REQUIRED)


    def test_invalid_email_format(self, page):
        login = LoginPage(page)
        login.login(
            data["invalid_email_format"]["email"],
            data["invalid_email_format"]["password"]
        )

        assert login.is_error_visible(LoginLocators.INVALID_EMAIL)


    def test_empty_password(self, page):
        login = LoginPage(page)
        login.login("test@gmail.com", "")

        assert login.is_error_visible(LoginLocators.PASSWORD_REQUIRED)


    def test_empty_email(self, page):
        login = LoginPage(page)
        login.login("", "Password123")

        assert login.is_error_visible(LoginLocators.EMAIL_REQUIRED)