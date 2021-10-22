class User:
    """
    User class that generates new instances of users
    """

    user_list = [] #Empty user list


    def __init__(self, account_name, username, password):
        self.account_name = account_name
        self.username = username
        self.password = password

    def save_user(self):
        """
        save_user method saves user objects into user_list
        """
        User.user_list.append(self)


 # checking to see if user object actually exixts
    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_contact()
        test_user = User("instagram","Vee@123","*1@3#675") # new user
        test_user.save_user()

        user_exists = User.user_exist("0711223344")

        self.assertTrue(user_exists)


    @classmethod
    def display_user(cls):
        return cls.user_list

    def delete_user(self):
        '''
        delete_user method deletes a  saved user from the list
        '''
        User.user_list.remove(self)

    @classmethod    
    def find_by_account_name(cls,account_name):
        '''
        Method that takes in account name and returns credentials that matches that name if it exists.

        Args:
            name: Account name to search for
        Returns :
            Credentials of account that matches the name.
        '''

        for user in cls.user_list:
            if user.account_name == account_name:
                 return user
        return False


    @classmethod
    def display_users(cls):
        '''
        method that returns the contact list
        '''
        return cls.user_list