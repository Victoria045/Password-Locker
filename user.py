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