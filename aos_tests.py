import unittest
import aos_locators as locators
import aos_methods as methods

class AOSAppPositiveTestCases(unittest.TestCase):  #create class

    @staticmethod              #signals to unittest that this is a static method
    #def test_create_new_user():
    def test_aos():
        methods.setUp()
        methods.check_homepage()
        methods.create_new_account()
        methods.validate_new_account()
        print(f'------New account is created, Username is {locators.new_user_name}')
        methods.logout()
        methods.login()
        # Validate New User can login (see if you can reuse New Account Validation)
        methods.validate_new_account()
        #print(f'------New user {locators.new_user_name} can log in!')
        methods.logger('created')
        methods.checkout()
        # Logout
        methods.logout()
        #print(f'------New user {locators.new_user_name} can log out successfully!')
        methods.login()
        methods.validate_new_account()
        methods.view_cart()
        methods.cancel_order()
        methods.delete_account()
        methods.tearDown()

    # def test_homepage(self):
    #     methods.setUp()
    #     methods.check_homepage_text()
    #     methods.check_shopnow_button()
    #     methods.check_main_menu()
    #     methods.check_mainlogo()
    #     methods.contact_us()
    #     methods.check_socialmedia_link()
    #     methods.tearDown

# setUp()
# # Create New Account
# create_new_account()
# # Validate New Account is created
# validate_new_account()
# print(f'------New account is created, Username is {locators.new_user_name}')
# # Logout
# logout()
# sleep(0.5)
# # Login
# login()
# # Validate New User can login (see if you can reuse New Account Validation)
# validate_new_account()
# print(f'------New user {locators.new_user_name} can log in!')
# logger('created')
# # Logout
# logout()
# print(f'------New user {locators.new_user_name} can log out successfully!')
# sleep(0.25)
# tearDown()
