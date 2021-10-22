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


    @classmethod
    def display_user(cls):
        return cls.user_list

    def delete_user(self):
        '''
        delete_user method deletes a  saved user from the list
        '''
        User.user_list.remove(self)