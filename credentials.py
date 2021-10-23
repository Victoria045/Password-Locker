import random
import pyperclip
import user from User

class Credentials:
    """
    Class that generates new instances of credentials
    """
    credentials_list = []


    @classmethod
    def verify_user(cls,username, password):
        """
        method to verify whether the user is in our user_list or not
        """
        existing_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                    existing_user == user.username
        return existing_user


    def __init__(self,account_name,userName, password):
        """
        method that defines user account credentials to be stored
        """
        self.account_name = account_name
        self.user_name = user_name
        self.password = password

    def save_credentials(self):
        """
        save_credentials method to save credentials object to the credentials list
        """
        Credentials.credentials_list.append(self)


    def delete_credentials(self):
        """
        delete_credentials method that deletes an account credentials from the credentials_list
        """
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_credential(cls, account_name):
        """
        Method that takes in a account_name and returns a credential that matches that account_name.

        Args:
            account_name: account_name to search for
        Returns :
            username and password of person that matches the number.
        """

        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return credential

    @classmethod
    def copy_password(cls,account_name):
        found_credentials = Credentials.find_credential(account_name)
        pyperclip.copy(found_credentials.password)