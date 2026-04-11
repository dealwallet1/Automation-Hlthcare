import pytest
from core.browser_manager import BrowserManager
from utils.config import BASE_URL, HEADLESS


@pytest.fixture
def page():
    browser = BrowserManager()
    page = browser.start(headless=HEADLESS)

    page.goto(BASE_URL)

    yield page

    browser.stop()