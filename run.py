from user import User 
from credentials import Credentials

print("*"*100)
def pattern():
	print("               ______                        __                       __   ___              ")
	print("              |   _  \                      |  |                     |  | /  /              ")
	print("              |  |_)  ) ____  ___   ___     |  |      _____    _____ |  |/__/               ")
	print("              |   _ _/ / _  |/ __  / __     |  |     /  _  \  /  __  |  |\  \               ")
	print("              |  |    / (_| |\__ \ \__ \    |  |___ (  (_)  )(  (__  |  | \  \              ")
	print("              |__|    \_____| ___/  ___/    |______) \_____/  \_____ |__|  \__\             ")
pattern()
print ('\n')
print("*"*100)


def create_new_user(username,password):
    '''
    Function to create a new user with a username and password
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    Function to save a new user
    '''
    user.save_user()

def display_user():
    """
    Function to display existing user
    """
    return User.display_user()

def login_user(username,password):
    """
    function that checks whether a user exist and then logs in the user
    """
  
    check_user = Credentials.verify_user(username,password)
    return check_user

def create_new_credential(account_name,user_name,password):
    """
    Function that creates new credentials for a given user account
    """
    new_credential = Credentials(account_name,user_name,password)
    return new_credential