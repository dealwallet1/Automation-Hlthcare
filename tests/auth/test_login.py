from pages.login_page import LoginPage
from utils.data_reader import read_test_data

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
        assert "signin" in page.url


    def test_empty_email_password(self, page):
        login = LoginPage(page)
        login.login(
            data["empty_user"]["email"],
            data["empty_user"]["password"]
        )
        assert "signin" in page.url


    def test_invalid_email_format(self, page):
        login = LoginPage(page)
        login.login(
            data["invalid_email_format"]["email"],
            data["invalid_email_format"]["password"]
        )
        assert "signin" in page.url


    def test_empty_password(self, page):
        login = LoginPage(page)
        login.login(
            data["empty_password"]["email"],
            data["empty_password"]["password"]
        )
        assert "signin" in page.url


    def test_empty_email(self, page):
        login = LoginPage(page)
        login.login(
            data["empty_email"]["email"],
            data["empty_email"]["password"]
        )
        assert "signin" in page.url