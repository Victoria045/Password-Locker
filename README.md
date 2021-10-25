# Password Locker

# Author 
Built by: [Victoria Beryl](https://github.com/Victoria045)

## Description
Password locker is a terminal run python application that generates new passwords and helps in the management of passwords for various accounts.

## Setup/Installation Requirements

#### Prerequisites 
* python3.6
* pip
* pyperclip

#### Cloning
* Open Terminal:

        $ git clone https://github.com/Victoria045/Password-Locker.git
        $ cd Password-Locker
        $ code . or atom . based on your text editor 

### Running the Application
* To run the application, open the cloned repo in terminal and run the following commands:

        $ chmod +x run.py
        $ ./run.py

### Testing the Application       
* To run tests for the class application and check if it functions well:

        $ python3 credentials_test.py
        $ python3 user_test.py

## User Stories
Behaviours the application implements for the user:
* Create an account for the application or log into the application if already have account.
* Store existing acounts login credentials.
* Application generates new password for a new account/credential.   
* Option to delete stored account login credentials that is no longer needed.
* Option to copy credentials to the clipboard.

## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Open the application on the terminal | In terminal: ```$python3 ./run.py```|Hello Welcome to your Accounts Password Locker <br> CA* ...  Create A New Account<br>  SI* ...  Already Have An Account? |
|Enter: CA| Enter username and password| Hello ```username```, Your account has been created succesfully! Your password is: ```password```|
|Enter: SI  | Enter password and username you signed up with| Short codes menu to help you navigate through the application|
|Create a new credential in the application| Enter ```CC```|Enter Account name, username, password<br>choose ```kp``` to key in your password or ```gp``` for the application to generate a password |
|Display all stored credentials | Enter ```DC```|Displays a list of all stored credentials |
|Find a stored credential based on account name|Enter ```FC```| Enter the Account Name you want to find for which returns the accountd details |
|Delete an existing credential that you don't want anymore|Enter ```DD```|Enter the account name of the Credentials you want to delete |
|Exit the application| Enter ```ex```| The application exits |

## Technologies Used
* python3.6

* markdown

## Support and contact details
Incase of any issues at hand, please email me at victoriaberyl45@gmail.com

### License
MIT License. 