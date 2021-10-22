import unittest # Importing the unittest module
from credentials import Credentials # Importing the credentials class

class TestContact(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

# First test <-- Testing if our objects are instantiated correctly-->
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Twitter","Victoria045","x354yrz21") # create user object


if __name__ == '__main__':
    unittest.main()