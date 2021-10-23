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
        self.assertEqual(self.new_credential.account,'Twitter')
        self.assertEqual(self.new_credential.userName,'Victoria_Beryl')
        self.assertEqual(self.new_credential.password,'1@xy%zw!')

# second test <-- calls save_contact method to the newly generated object-->
    def test_save_credential(self):
        """
        test case to test if the credential object is saved into the credentials list

        """
        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)