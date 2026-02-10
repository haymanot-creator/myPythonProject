from playwright.sync_api import expect

from training_pyton.ebay_project.pages.base_page import BasePage


class HomePage(BasePage):
    URL = "https://www.ebay.com"

    def __init__(self, page):
        super().__init__(page)
        self.search_input = page.locator("#gh-ac")
        self.search_button = page.locator("#gh-btn")

    def open(self):
        self.page.goto(self.URL)
        self.page.wait_for_load_state("domcontentloaded")

    def search_product(self, text: str):
        expect(self.search_input).to_be_visible(timeout=15000)
        self.search_input.fill(text)


        expect(self.search_button).to_be_visible(timeout=15000)
        self.search_button.click()

        from .results_page import ResultsPage
        return ResultsPage(self.page)
