from .base_page import BasePage
from playwright.sync_api import expect

class ResultsPage(BasePage):
    def has_results(self):
        items = self.page.locator(".s-item")
        expect(items).to_have_count(lambda count: count > 0)

    def open_first_product(self):
        first_item = self.page.locator(".s-item a").first
        expect(first_item).to_be_visible()
        first_item.click()