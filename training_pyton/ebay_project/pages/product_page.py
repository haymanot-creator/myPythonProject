from .base_page import BasePage
from playwright.sync_api import expect

class ProductPage(BasePage):
    def has_price(self):
        price = self.page.locator("[itemprop='price']")
        expect(price).to_be_visible()