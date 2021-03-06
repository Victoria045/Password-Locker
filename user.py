class User:
    """
    Create User class that generates new instances of a user

    """
    user_list = []

    def __init__(self, username, password):
        """
        method that defines the properties of a user
        """
        self.username = username
        self.password = password

    def save_user(self):
        """
        save_user method that saves user objects into the user list
        """
        User.user_list.append(self) 

    @classmethod
    def verify_user(cls,username, password):
        """
        method to verify whether the user is in our user_list or not
        """
        existing_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                return True 
        return False
    

    @classmethod
    def display_user(cls):
        return cls.user_list

    def delete_user(self):
        '''
        delete_account method deletes a  saved account from the list
        '''
        User.user_list.remove(self)