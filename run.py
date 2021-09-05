#!/usr/bin/env python3.6
import random
from user import User
from account import Account

def create_user(fname,lname,uname,pword):
    """
    function to create a new user account
    """
    new_user = User(fname,lname,uname,pword)
    return new_user

def save_user(user):
    """
    function to save user
    """
    user.save_user()

def find_user(password):
    """
    function to allow entry to the password locker
    """
    return User.find_by_password(password)

def check_existing_users(password):
    """
    function to check if the user exists
    """
    return User.user_exist(password)    

def create_account(acc_name,password):
    """
    function to create a new account
    """
    new_account = Account(acc_name,password)
    return new_account

def save_account(account):
    """
    function to save an account
    """
    account.save_account()

def display_account():
    """
    function to display the saved accounts
    """
    return Account.display_account()

def find_account(acc_name):
    """
    function to find an account using its name
    """
    return Account.find_by_account_name(acc_name)

def check_existing_accounts(acc_name):
    """
    function to check if the account exists
    """
    return Account.account_exist(acc_name) 

def del_account(account):
    """
    function to delete a saved account
    """
    account.delete_account()

def main():
    print("Welcome to the Password-Locker")
    print("\n")
    

    while True:
        print("Would you like to sign up or to log in")

        print("Use short codes: su -to sign up, li -to log in or ex -to exit")

        short_code = input().lower()

        if short_code == 'su':
            print("New user account")
            print("-"*10)

            print("First name ....")
            f_name = input()

            print("Last name ....")
            l_name = input()

            print("Username....")
            u_name = input()

            print("Password....")
            print("Do not share with anybody")
            pword = input()


            save_user(create_user(f_name,l_name,u_name,pword)) #create and save new user account
            print('\n')
            print(f"{f_name} {l_name}, you have successfully signed up")
            print("You can now log in and experience the password-locker")
            print("\n")

        elif short_code == 'li':
            print("Enter your username")
            u_name = input()
            print("Enter your password")
            pword_input = input()
            if check_existing_users(pword_input):
                search_user = find_user(pword_input)
                print(f"{search_user.first_name} {search_user.last_name} you have successfully logged in")
                print('-'*10)
                
                while True:
                    print(f"{search_user.first_name}, what would you like to do?")
                    print("-"*10)
                    print("\n")
                    print("Use the following short codes: ca - create a password-locker account of an existing credential account, na - create a new password-locker account of a new credential account, da - display your saved accounts, fa - find an account, del - delete an account, ex - exit")
                    print("\n")
                    
                    short_codes = input().lower()

                    if short_codes == 'ca':
                        print("New Credentials Account")
                        print("-"*10)

                        print("Name of the account")
                        a_name = input()

                        print("Account password")
                        psword = input()

                        save_account(create_account(a_name,psword))
                        print('\n')
                        print('Your credentials account has been saved')
                        print("*"*10)
                        print('\n')

                    elif short_codes == 'na':
                        print('Creating a new account')
                        print('Input your new account name')
                        ac_name = input()

                        print('Would you like create you own password (Write "own") or let us generate one for you (Write "gen")')
                        ans = input()
                        if ans == 'own':
                            print("Input password")
                            passwrd = input()

                            save_account(create_account(ac_name,passwrd))
                            print("\n")
                            print("Your credential account has been succesfully created")
                            print("*"*10)

                        elif ans == 'gen':
                            choices = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                            length = len(choices)
                            print("Give the length to your password: Use numbers not words")
                            lent = int(input())
                            passwd = "".join(random.sample(choices,lent))
                            print('\n')
                            
                            print("Your new password is:")
                            print(passwd)
                            save_account(create_account(ac_name,passwd))
                            print("Your credential account has been successfully created")
                            print("*"*10)


                    elif short_codes == 'da':

                        if display_account():
                            print('Here is a list of all your credential accounts:')
                            print('\n')

                            for account in display_account():
                                print(f"{account.acc_name} ----- {account.password}")
                                print("*"*10)
                                print('\n')
                        
                        else:
                            print('You dont have any accounts yet')
                            print('\n')
                        
                   
                    elif short_codes == 'del':
                        print("Enter the following:")
                        print("Account name")
                        acnt_name = input()

                        if check_existing_accounts(acnt_name):
                            deleted_account = find_account(acnt_name)
                            del_account(deleted_account)

                            print(f"{deleted_account.acc_name} has been succesfully deleted")
                            print('*'*10)

                        else:
                            print("Could not find that credential")
                    
                    
                    elif short_codes == "fa":
                        print("Enter the account you would like to search for")

                        search_account = input()
                        if check_existing_accounts(search_account):
                            search_account = find_account(search_account)
                            print(f"{search_account.acc_name} ------- {search_account.password}")
                            print('*' * 10)
                        else:
                            print("That account does not exist")

                    elif short_codes == "ex":
                        print("Bye ...Till next time")
                        break

                    else:
                        print("I really didn't get that. Please use the short codes provided")


            else:
                print("\n")
                print("You have inputted the wrong username or password")


        elif short_code == 'ex':
            print("Bye")
            break


        else:
            print("I really did not get that. Please use the short codes")


if __name__ == '__main__':

    main()
