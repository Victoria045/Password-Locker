import unittest # Importing the unittest module
from user import User # Importing the user class

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


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.account_name,"Twitter")
        self.assertEqual(self.new_user.username,"Victoria045")
        self.assertEqual(self.new_user.password,"x354yrz21")


# second test <-- calls save_user method to the newly generated object-->
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)


# Third test <-- Helps us get accurate test results every time a new test case-->
    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("instagram","Vee@123","*1@3#675") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

    def test_save_multiple_contact(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("instagram","Vee@123","*1@3#675") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)


# Fourth test
    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = User("instagram","Vee@123","*1@3#675") # new user
            test_user.save_user()

            self.new_user.delete_user()# Deleting a user object
            self.assertEqual(len(User.user_list),1)


# Fifth test
    def test_find_user_by_accont_name(self):
        '''
        test to check if we can find a user by account name and display information
        '''

        self.new_user.save_user()
        test_user = User("instagram","Vee@123","*1@3#675") # new contact
        test_user.save_user()

        found_user = User.find_by_account_name("instagram")

        self.assertEqual(found_user.password,test_user.password)


# checking to see if a user object actually exixts
    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("instagram","Vee@123","*1@3#675") # new user
        test_user.save_user()

        user_exists = User.user_exist("instagram")

        self.assertTrue(user_exists)


# test to check if we receive the list of the saved users
    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(User.display_users(),User.user_list)


if __name__ == '__main__':
    unittest.main()