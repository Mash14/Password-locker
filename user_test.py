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
