class TestCredentials(unittest.TestCase):
    """
    A test class that defines test cases for credentials class

    """ 

    def setUp(self):
        """
        Method that runs before each individual credentials test methods run

        """
        self.new_credential = Credentials('Twitter','Victoria_Bryl','1@xy%zw!')