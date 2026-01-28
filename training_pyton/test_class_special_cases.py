class Test Swaglabs Example():

    def test_swaglabs_correct_user_login_with_class(self, setup_playwright):
        print("into test_class_correct_login")
        page = setup_playwright
        page.goto("https://www.saucedemo.com/")
        elements_with_spaces = page.query_selector_all(".input_error.form_input")  # example how to handle spaces in class

        elements_partial = page.query_selector_all("[class*=input_error]")

    def test_swaglabs_correct_password_login(self, setup_playright):
        print("into test_swag_labs_correct_password_login")
        page = setup_playright
        page.goto("https://www.saucedemo.com/")
        elements_with_spaces = page.query_selector_all("[class*=input_error]")


        elements_partial = page.query_selector_all("[class*=input_error]")
