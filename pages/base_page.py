class BasePage:
    def __init__(self, page):
        self.page = page

    def fill(self, locator, value):
        self.page.locator(locator).fill(value)

    def click(self, locator):
        self.page.locator(locator).click()

    def get_text(self, locator):
        element = self.page.locator(locator)
        try:
            element.wait_for(state="visible", timeout=5000)
            return element.text_content()
        except:
            return None