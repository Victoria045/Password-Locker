import unittest
from user import User
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    """
    A test class that defines test cases for credentials class

    """ 

# First test <-- Testing if our objects are instantiated correctly-->
    def setUp(self):
        """
        Method that runs before each individual credentials test methods run

        """
        self.new_credential = Credentials('Twitter','Victoria_Beryl','1@xy%zw!')

    def test_init(self):
        """
        Test case to check if a new Credentials instance has been initialized correctly
        """
        self.assertEqual(self.new_credential.account_name,'Twitter')
        self.assertEqual(self.new_credential.user_name,'Victoria_Beryl')
        self.assertEqual(self.new_credential.password,'1@xy%zw!')

# second test <-- calls save_contact method to the newly generated object-->
    def test_save_credential(self):
        """
        test case to test if the credential object is saved into the credentials list

        """
        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run
        '''
        Credentials.credentials_list = []

    def test_save_many_accounts(self):
        '''
        test to check if we can save multiple credentials objects to our credentials list
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials("Instagram","VeeB","x3wyt13s") 
        test_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

# Fourth test
    def test_delete_credential(self):
        """
        test method to test if we can remove an account credentials from our credentials_list
        """
        self.new_credential.save_credentials()
        test_credential = Credentials("Instagram","VeeB","x3wyt13s")
        test_credential.save_credentials()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

# Fifth test
    def test_find_credential(self):
        """
        test to check if we can find a credential entry by account name and display the details of the credential
        """
        self.new_credential.save_credentials()
        test_credential = Credentials("Instagram","VeeB","x3wyt13s") 
        test_credential.save_credentials()

        the_credential = Credentials.find_credential("Instagram")

        self.assertEqual(the_credential.account_name,test_credential.account_name)

# checking to see if a credntial object actually exixts
    def test_credential_exist(self):
        """
        test to check if we can return a true or false based on whether we find or can't find the credential.
        """
        self.new_credential.save_credentials()
        the_credential = Credentials("Instagram","VeeB","x3wyt13s")  
        the_credential.save_credentials()
        credential_is_found = Credentials.if_credential_exist("Instagram")
        self.assertTrue(credential_is_found)


    def test_display_all_saved_credentials(self):
        '''
        method that displays all the credentials that has been saved by the user
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

if __name__ == "__main__":
    unittest.main()