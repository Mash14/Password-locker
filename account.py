class Account:
    """
    Class that generates new instances of accounts
    """

    account_list = []
    
    def __init__(self,account_name,password):
        """
        __init__ method that helps us define the properties for our objects
        
        Args:
            account_name: New account name
            password: New account password
        """

        self.acc_name = account_name
        self.password = password