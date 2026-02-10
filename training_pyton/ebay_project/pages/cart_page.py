from .base_page import BasePage
from playwright.sync_api import expect

class CartPage(BasePage):
    URL = "https://cart.ebay.com"

    def open(self):
        self.page.goto(self.URL)

    def is_opened(self):
        expect(self.page).to_have_url(self.URL)