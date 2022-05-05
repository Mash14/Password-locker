import unittest
from user import User


class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the user class behaviours

    Args:
        unittest.Testcase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Denise","Wanjiru","DensTheLion","!@#$")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_init(self):
        '''
        Test case to see if objects are initialized properly
        '''
        self.assertEqual(self.new_user.first_name,"Denise")
        self.assertEqual(self.new_user.last_name,"Wanjiru")
        self.assertEqual(self.new_user.username,"DensTheLion")
        self.assertEqual(self.new_user.password,"!@#$")

    def test_save_user(self):
        '''
        Test case to test if the user object is saved into
        the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_users(self):
        '''
        Test case to test if we can save multiple users to the user list
        '''
        self.new_user.save_user()
        second_user = User("Lan","Mac","LaMa","1234")
        second_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_find_my_account(self):
        """
        Test case to find a users account by username and password
        """
        self.new_user.save_user()
        second_user = User("Lan","Mac","LaMa","1234")
        second_user.save_user()
        found_user = User.find_user("LaMa","1234")
        self.assertEqual(found_user.first_name,second_user.first_name)

    def test_user_exists(self):
        """
        Test case to find if the user really exists
        """
        self.new_user.save_user()
        user_exist = User.user_exists("DensTheLion","!@#$")
        self.assertTrue(user_exist)

if __name__ == '__main__':
    unittest.main()