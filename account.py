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

    @classmethod
    def find_by_account_name(cls,acc_name):
        '''
        Method that takes in the account name and returns a account that matches that name.

        Args:
            acc_name: Account name to search for
        Returns :
            Account that matches the name.
        '''

        for account in cls.account_list:
            if account.acc_name == acc_name:
                return account

    @classmethod
    def account_exist(cls,acc_name):
        '''
        Method that checks if an account exists from the account list.
        Args:
            acc_name: Account name to search if it exists
        Returns :
            Boolean: True or false depending if the account exists
        '''
        for account in cls.account_list:
            if account.acc_name == acc_name:
                    return True

        return False