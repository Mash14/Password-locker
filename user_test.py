import unittest
from user import User

class TestUser(unittest.TestCase):

    """
    Test class that defines test clases for the user class behaviour.
    
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """


    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_user = User("Alan","Mash","MashAlonzo","Moringa") #create user object


    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """

        self.assertEqual(self.new_user.first_name,"Alan")
        self.assertEqual(self.new_user.last_name,"Mash")
        self.assertEqual(self.new_user.user_name,"MashAlonzo")
        self.assertEqual(self.new_user.password,"Moringa")
    

    def test_save_user(self):
        """
        test_save_user test case to test if the user object is saved in the user list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)


    def tearDown(self):
        """
        teardown method that does clean up after each test case has run
        """
        User.user_list = []


    def test_find_user_by_password(self):
        """
        test_find_user_by_password test case is to check if we can find the users account and then login
        """
        self.new_user.save_user()
        test_user = User("Mark","Njenga","Mnjenga","Pridemark")
        test_user.save_user()

        found_user = User.find_by_password("Pridemark")

        self.assertEqual(found_user.password,test_user.password)


    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("Mark","Njenga","Mnjenga","Pridemark") # new user
        test_user.save_user()

        user_exists = User.user_exist("Pridemark")

        self.assertTrue(user_exists)

