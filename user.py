class User:
    """
    Class that generates new instances of the user
    """

    user_list = [] # Empty list of users

    def __init__(self,first_name,last_name,username,password):
        """"
        __init__ method that defines properties for our objects

        Args:
            first_name: new user first name
            last_name: new user last name
            username: new user username
            password: new user password
        """
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

        
    def save_user(self):
        """
        save_user method saves user objects into the user_list
        """
        User.user_list.append(self)

    @classmethod
    def find_user(cls,username,password):
        """
        Method that takes in a password and returns the user details that match that password
        
        Args:
            username: username of the user's account
            password: password of the user's account
        
        Returns: 
            User details of the person that matches the password
        """
        for user in cls.user_list:
            if user.username == username and user.password == password:
                return user

    @classmethod
    def user_exists(cls,username,password):
        """
        Method that checks if a user exists from the user list.
        Args:
            username: username to search if it exists
            password: password to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        """
        for user in cls.user_list:
            if user.username == username and user.password == password:
                return True

        return False