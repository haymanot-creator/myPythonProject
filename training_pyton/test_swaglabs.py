

class TestSwagLabs(object):

    def test_swaglabs_correct_login(self , setup_playwright ):
        print("into test_swaglabs_correct_login")
        page = setup_playwright()
        page.goto("https://www.saucedemo.com")
        user = page.locator("[id='user-name']")
        user.fill('standard_user')
        password = page.locator("[id='password']")
        password.type("secret_sauce")
        login_button = page.locator("[name='login_button']")
        login_button.click()
        print(f"current url is{page.url}")
        current_url = page.url
        assert current_url == "https://www.saucedemo.com/inventory.html","current url is not expected"
        print("test end")

    def test_swag_labs_incorrect_password_logout(self,setup_playwright):
        print("into test_swag_labs_incorrect_password_logout")
        page = setup_playwright
        page.goto("https://www.saucedemo.com")
        user = page.locator("[id='user-name']")
        user.fill('standard_user')
        password = page.locator("[id='password']")
        password.type("fail")
        login_button = page.locator("[name='login_button']")
        login_button.click()
        print(f"current url is{page.url}")
        current_url = page.url
        assert current_url == "https://www.saucedemo.com ,current url is not expected"
        print("test end")
