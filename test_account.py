import unittest
from account import Account
import pyperclip


class TestAccount(unittest.TestCase):
    """
    st class that defines test cases for the contact class behaviours
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases 
    """
    def setUp(self):
        '''
        Set up method to run before each test cases
        '''
        self.new_account = Account("TikTok","Dens","!@#$")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run
        '''
        Account.account_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_account.name,"TikTok")
        self.assertEqual(self.new_account.username,"Dens")
        self.assertEqual(self.new_account.password,"!@#$")

    def test_save_account(self):
        '''
        test_save_account test case is used to test if the object is being saved in the account list
        '''
        self.new_account.save_account()
        self.assertEqual(len(Account.account_list),1)

    def test_save_multiple_account(self):
        '''
        test_save_multiple_accounts is a test done to check if we can save multiple accounts
        '''
        self.new_account.save_account()
        second_account = Account("Twitter","Mark","1234")
        second_account.save_account()
        self.assertEqual(len(Account.account_list),2)

    def test_delete_method(self):
        '''
        test_delete_account is to test if we can remove an account from the account_list
        '''
        self.new_account.save_account()
        second_account = Account("Twitter","Mark","1234")
        second_account.save_account()
        second_account.delete_account()
        self.assertEqual(len(Account.account_list),1)

    def test_display_accounts(self):
        '''
        test_display_account is a method that returns a list of accounts saved
        '''
        
        self.assertEqual(Account.display_account(),Account.account_list)

    def test_find_account_by_name(self):
        '''
        test_find_account_by_name is a method that returns a list of accounts saved
        '''
        self.new_account.save_account()
        second_account = Account("Twitter","Mark","1234")
        second_account.save_account()
        found_account = Account.find_account_by_name("Twitter")
        self.assertEqual(found_account.username,second_account.username)
     
    def test_account_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the account.
        '''
        self.new_account.save_account()
        second_account = Account("Twitter","Mark","1234")
        second_account.save_account()
        account_exist = Account.account_exists(second_account.name)
        self.assertTrue(account_exist)

# python3 -m pip install pyperclip
    def test_copy_to_clipboard(self):
        '''
        Test to confirm that we are copying the assword from a users account
        '''
        self.new_account.save_account()
        second_account = Account("Twitter","Mark","1234")
        second_account.save_account()
        Account.copy_credentials("Twitter")
        self.assertEqual(second_account.password,pyperclip.paste())

if __name__ == '__main__':
    unittest.main()





