import unittest
from account import Account

class TestAccount(unittest.TestCase):

    """
    Test class that defines test cases for the contact class behaviours

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """


    def setUp(self):
        """
        Set up method to run before each test cases
        """

        self.new_account = Account("Twitter","twinklestar")


    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """

        self.assertEqual(self.new_account.acc_name,"Twitter")
        self.assertEqual(self.new_account.password,"twinklestar")


    def test_save_account(self):
        """
        test_save_account test case is used to test if the object is being saved in the account list
        """

        self.new_account.save_account()
        self.assertEqual(len(Account.account_list),1)
    

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run
        """

        Account.account_list = []


    def test_save_multiple_accounts(self):
        """
        test_save_multiple_accounts is a test done to check if we can save multiple accounts
        """

        self.new_account.save_account()
        test_account = Account("Insta","Dancemokey")
        test_account.save_account()
        self.assertEqual(len(Account.account_list),2)


