from pages.base_page import BasePage
from locators.login_locators import LoginLocators


class LoginPage(BasePage):

    def login(self, email, password):
        self.fill(LoginLocators.EMAIL_INPUT, email)
        self.fill(LoginLocators.PASSWORD_INPUT, password)
        self.click(LoginLocators.SIGNIN_BUTTON)

        # small wait for UI update (avoid networkidle issue)
        self.page.wait_for_timeout(3000)

    def get_error(self):
        # try generic error text
        try:
            error = self.page.locator("text=Invalid")
            if error.first.is_visible():
                return error.first.text_content()
        except:
            pass

        # fallback locator
        try:
            error = self.page.locator(LoginLocators.ERROR_MESSAGE)
            error.wait_for(state="visible", timeout=3000)
            return error.text_content()
        except:
            pass

        return None