from user import User 
from credentials import Credentials

print('*'*100)
def pattern():
	print('               ______                        __                       __   ___              ')
	print('              |   _  \                      |  |                     |  | /  /              ')
	print('              |  |_)  ) ____  ___   ___     |  |      _____    _____ |  |/__/               ')
	print('              |   _ _/ / _  |/ __  / __     |  |     /  _  \  /  __  |  |\  \               ')
	print('              |  |    / (_| |\__ \ \__ \    |  |___ (  (_)  )(  (__  |  | \  \              ')
	print('              |__|    \_____| ___/  ___/    |______) \_____/  \_____ |__|  \__\             ')
pattern()
print ('\n')
print('*'*100)


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
def authenticate_user(username, password):
        """
        method to authenticate user whether the user is in our user_list or not
        """
        return User.verify_user(username,password)
def display_user():
    '''
    Function to display existing user
    '''
    return User.display_user()

def signin_user(username,password):
    '''
    function that checks whether a user exist and then signs in the user
    '''
  
    check_user = Credentials.verify_user(username,password)
    return check_user

def create_new_credential(account_name,user_name,password):
    '''
    Function that creates new credentials for a given user account
    '''
    new_credential = Credentials(account_name,user_name,password)
    return new_credential

def save_credentials(credentials):
    '''
    Function to save Credentials to the credentials list
    '''
    credentials.save_credentials()

def display_accounts_details():
    '''
    Function that returns all the saved credential.
    '''
    return Credentials.display_credentials()

def delete_credential(credentials):
    '''
    Function to delete a Credentials from credentials list

    '''
    credentials.delete_credentials()


def find_credential(account_name):
    '''
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    '''
    return Credentials.find_credential(account_name)


def check_credentials(account_name):
    '''
    Function that check if a Credentials exists with that account name and return true or false

    '''
    return Credentials.if_credential_exist(account_name)


def generate_Password():
    '''
    generates a random password for the user.
    '''
    random_password=Credentials.generatePassword()
    return random_password


def copy_password(account_name):
    '''
    A function that copies the password using the pyperclip framework
    We import the framework then declare a function that copies the emails.
    '''
    return Credentials.copy_password(account_name)


def main():
    print('Hello Welcome to your Accounts Password Locker...\n\n Please enter one of the following short codes to proceed.\n CA ---  Create New Account  \n SI ---  Already Have An Account?  \n')
    short_code=input("").strip()
    if short_code == 'ca' or short_code == 'CA':
        print('Create Account')
        print('*' * 50)
        username = input('Username: ')
        while True:
            print('Please enter one of the following short codes to continue...\n KP - To key in your own pasword\n GP - To generate a random Password')
            selected_password = input().strip()
            if selected_password == 'kp' or selected_password == 'KP':
                password = input("Enter Password\n")
                break
            elif selected_password == 'gp' or selected_password == 'GP':
                password = generate_Password()
                break
            else:
                print('Invalid password please try again')

        save_user(create_new_user(username,password))
        print ('\n')
        print('*'*90)
        print('\n')
        print(f'Hello {username}, Your account has been created succesfully! Your password is: {password}')
        print('\n')
        print("*"*90)
        print ('\n')

    elif short_code == 'si':
        print('*'*65)
        print('Please enter your Username and your Password to sign in:')
        print('*' * 65)
        username_input = input('Username: ')
        password_input = input('password: ')

    while True:
        print('Sign in to continue...')
        username_input = input('Username: ')
        password_input = input('password: ')
        if authenticate_user(username_input,password_input):
            print(f'You are successfully signed in {username_input}!!!')  
            print('\n')
            break
            
        else:
            print('Invalid credentials! Please try again')
        

    while True:
        print('Use these short codes to continue:\n CC - Create a new credential \n DC - Display Credentials \n FC - Find a credential \n GP - Generate A randomn password \n DD - Delete credential \n EX - Exit the application \n')
        short_code = input().lower().strip()
        if short_code == 'cc':
            print("Create A New Account Credential")
            print("*"*32)
            print("Account name....")
            account_name = input().lower()
            print('\n')
            print("Your Account username....")
            user_name = input()
            print('\n')
            while True:  
                print('Please enter one of the following short codes to proceed.....\n KP - To key in your own pasword if you already have an account\n GP - To generate random Password')
                print('\n')
                selected_password = input().lower().strip()
                if selected_password == 'kp':
                    password = input('Enter Your Own Password\n')
                    break
                elif selected_password == 'gp':
                    password = generate_Password()
                    break
                else:
                    print('Invalid password please try again')
            save_credentials(create_new_credential(account_name,user_name,password))
            print('*'*100)
            print('\n')
            print(f'Account Credential for: {account_name}....  Username: {user_name}  Password: {password} created succesfully!!!')
            print('\n')
            print('*'*100)
            print('\n')

        elif short_code == 'dc':
            if display_accounts_details():
                print("Here's your list of acounts: ")
                print('*' * 30)
                print('_'* 30)
                for account_name in display_accounts_details():
                    print(f' Account:{account_name.account_name} \n Username:{username}\n Password:{password}')
                    print('_'* 30)
                print('*' * 30)
                print('\n')
            else:
                print("Ooops!You don't have any credentials saved yet.....")


        elif short_code == "fc":
            print('Enter the Account Name you want to search for')
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print('\n')
                print(f'Account Name : {search_credential.account_name}')
                print('*' * 50)
                print(f' Username: {search_credential.user_name}\n Password :{search_credential.password}')
                print('*' * 50)
                print('\n')
            else:
                print('That Credential does not exist')
                print('\n')

        elif short_code == "dd":
            print('Enter the account name of the Credentials you want to delete')
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("*"*65)
                search_credential.delete_credentials()
                print('\n')
                print(f'Your credentials for : {search_credential.account_name} successfully deleted!!!')
                print('\n')

            else:
                print('That Credential you want to delete does not exist')

        elif short_code == 'gp':

            password = generate_Password()
            print(f'Your {password} has been generated succesfull. You can proceed to use it to your account')
        elif short_code == 'ex':
            print('Thank you for using accounts password locker...')

            print('*'*100)
            def pattern():
              print('               ______    ___    ___   __ _____        __              ')
              print('              |   _  \   \  \  /  /  |  |            |  |             ')
              print('              |  |_)  )   \  \/  /   |  |            |  |             ')
              print('              |______/     \    /    |  |___  ....   |  |             ')
              print('              |   _   \     |  |     |  |            |__|             ')
              print('              |  |_)   )    |  |     |  |             __              ')
              print('              |_______/     |__|     |__|_____       |__|             ')
            pattern()
            print ('\n')
            print('*'*100)
            break

        else:
            print('Wrong entry... Check your entry again and let it match those in the menu')
    
    else:
        print('Please enter a valid input to continue')

if __name__ == '__main__':
    main()