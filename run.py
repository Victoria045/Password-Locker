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