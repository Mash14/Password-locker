import pyperclip


class Account:
    '''
    Class that generates new instances of the objects
    '''

    account_list = []

    def __init__(self,account_name,account_username,account_password):
        '''
        __init__ method that helps us define the properties for our objects
        
        Args:
            account_name: New account name
            account_username: New persons account username
            password: New account password
        '''
        self.name = account_name
        self.username = account_username
        self.password = account_password

    def save_account(self):
        '''
        save_account method saves the account objects into the account_list
        '''
        Account.account_list.append(self)

    def delete_account(self):
        '''
        delete_account method deletes a saved account from the account list
        '''
        Account.account_list.remove(self)

    @classmethod
    def display_account(cls):
        '''
        method that returns a list of all saved accounts
        '''
        return cls.account_list

    @classmethod
    def find_account_by_name(cls,name):
        '''
        method that finds an acount by its name
        Args:
            name: name of the account
        '''
        for account in cls.account_list:
            if account.name == name:
                return account

    @classmethod
    def account_exists(cls,name):
        '''
        method to check if the account exists
        Args:
            name: name of the account
        '''
        for account in cls.account_list:
            if account.name == name:
                return True

        return False
    
    @classmethod
    def copy_credentials(cls,name):
        '''
        Method that copies the credentials to clipboard
        Args:
            name: name of the account
        '''
        account = cls.find_account_by_name(name)
        pyperclip.copy(account.password)
