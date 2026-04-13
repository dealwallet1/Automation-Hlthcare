# from pages.base_page import BasePage
# from locators.login_locators import LoginLocators


# class LoginPage(BasePage):

#     def login(self, email, password):
#         self.fill(LoginLocators.EMAIL_INPUT, email)
#         self.fill(LoginLocators.PASSWORD_INPUT, password)
#         self.click(LoginLocators.SIGNIN_BUTTON)

#         # small wait for UI update (avoid networkidle issue)
#         self.page.wait_for_timeout(3000)

#     def get_error(self):
#         error = self.page.locator(LoginLocators.ERROR_MESSAGE)

#         try:
#             error.wait_for(state="visible", timeout=5000)
#             return error.text_content()
#         except:
#             return None
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