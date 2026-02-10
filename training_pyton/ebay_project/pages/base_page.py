from playwright.sync_api import expect
import re

class BasePage:
    def __init__(self, page):
        self.page = page

    def is_opened(self, url_part: str):
        expect(self.page).to_have_url(re.compile(url_part))