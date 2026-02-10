from training_pyton.ebay_project.pages.home_page import HomePage
from training_pyton.ebay_project.pages.cart_page import CartPage
from training_pyton.ebay_project.pages.product_page import ProductPage
from playwright.sync_api import expect


def test_search_product(page):


    home_page = HomePage(page)
    home_page.open()
    home_page.is_opened()

    results_page = home_page.search_product("laptop")
    results_page.has_results()


def test_open_product_and_check_price(page):


    home_page = HomePage(page)
    home_page.open()

    results_page = home_page.search_product("headphones")
    results_page.has_results()
    results_page.open_first_product()

    product_page = ProductPage(page)
    product_page.has_price()


def test_open_cart_page(page):


    cart_page = CartPage(page)
    cart_page.open()
    cart_page.is_opened()


def test_search_button_is_visible(page):
    home_page = HomePage(page)
    home_page.open()

    expect(home_page.search_button).to_be_visible()


def test_search_input_is_visible(page):


    home_page = HomePage(page)
    home_page.open()

    assert home_page.search_input.is_visible()
