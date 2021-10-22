class Credentials:
    """
    Credentials class that generates new instances of credentials
    """

    credentials_list = [] #Empty credentials list


    def __init__(self, account_name, username, password):
        self.account_name = account_name
        self.username = username
        self.password = password

    def save_details(self):
        """
        saves a new credential to the credentials list
        """
        Credentials.credentials_list.append(self)