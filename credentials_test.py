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
        self.new_credential = Credentials("Twitter","Victoria045","x354yrz21") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.account_name,"Twitter")
        self.assertEqual(self.new_credential.username,"Victoria045")
        self.assertEqual(self.new_credential.password,"x354yrz21")



if __name__ == '__main__':
    unittest.main()