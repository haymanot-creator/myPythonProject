from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    current_url = page.url
    assert current_url == "https://www.saucedemo.com/" , "current url is unexpected"
    page.close()
    browser.close()
    print("### Test end ###")
