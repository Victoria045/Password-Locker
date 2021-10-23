import unittest # Importing the unittest module
from user import User # Importing the user class


class TestClass(unittest.TestCase):
    """
    Test class that defines test cases for the User class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

# First test <-- Testing if our objects are instantiated correctly-->
    def setUp(self):
        """
        Method that runs before each individual test methods run.
        """
        self.new_user = User('Victoria045','z3123@56')

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.username,'Victoria045')
        self.assertEqual(self.new_user.password,'z3123@56')

# second test <-- calls save_user method to the newly generated object-->
    def test_save_user(self):
        """
        test_save_user test case to test if a new user instance has been saved into the user list

        """
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)

if __name__ == "__main__":
    unittest.main()