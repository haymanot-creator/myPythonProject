

class TestSwaglabs :

    def test_swaglabs_correct_login(self ,setup_playwright):
        print("into test_swaglabs_correct_login")
        page = setup_playwright
        page.goto("https://www.saucedemo.com/")


        user = page.locator("[id='user-name']")
        user.fill('standard_user')
        password = page.locator("[id='password']")
        password.type("secret_sauce")
        login_btn =page.get_by_text("login")
        login_btn.click()
        current_url = page.url
        assert current_url == "https://www.saucedemo.com/inventory.html","current url is not expected"
        print("test end")

