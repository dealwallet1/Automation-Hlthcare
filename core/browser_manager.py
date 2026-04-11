from playwright.sync_api import sync_playwright

class BrowserManager:

    def start(self, headless=False):
        self.p = sync_playwright().start()
        self.browser = self.p.chromium.launch(headless=headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        return self.page

    def stop(self):
        self.browser.close()
        self.p.stop()