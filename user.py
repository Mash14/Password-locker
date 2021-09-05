class User:
    """
    Class that generates new instance of the users
    """

    user_list = [] #empty user list

    def __init__(self,first_name,last_name,user_name,password):

        """
        __init__method that helps to define properties of our objects
        
        Args:
            first_name: New user first name
            last_name: New user last name
            user_name: New user login name
            password: New user password
        """

        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password


    def save_user(self):
        """
        save_user method saves user objects into the user_list
        """

        User.user_list.append(self)