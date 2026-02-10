import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def setup_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.ebay.com")
        yield page
        browser.close()


