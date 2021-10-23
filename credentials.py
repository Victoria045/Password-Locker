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