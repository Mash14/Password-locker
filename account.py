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

    def save_account(self):
        """
        save_account method saves the account objects into the account_list
        """

        Account.account_list.append(self)

    def delete_account(self):
        """
        delete_account method deletes a saved account from the account list
        """

        Account.account_list.remove(self)

    @classmethod
    def display_account(cls):
        """
        method that returns a list of all saved accounts
        """

        return cls.account_list