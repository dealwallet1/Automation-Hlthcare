
from pages.base_page import BasePage
from locators.login_locators import LoginLocators


class LoginPage(BasePage):

    def login(self, email, password):
        self.fill(LoginLocators.EMAIL_INPUT, email)
        self.fill(LoginLocators.PASSWORD_INPUT, password)
        self.click(LoginLocators.SIGNIN_BUTTON)

        self.page.wait_for_timeout(2000)

    def is_error_visible(self, locator):
        element = self.page.locator(locator)
        try:
            element.wait_for(state="visible", timeout=3000)
            return True
        except:
            return False