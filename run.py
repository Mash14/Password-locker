#!/usr/bin/env python3.8
import random
from user import User
from account import Account
import pyperclip

def create_user(f_name,l_name,u_name,p_word):
    '''
    function to create a new user account
    '''
    new_user = User(f_name,l_name,u_name,p_word)
    return new_user

def save_users(user):
    '''
    Function to save new users
    '''
    user.save_user()

def find_users(u_name,p_word):
    '''
    function to users by username and password the returns that user
    '''
    return User.find_user(u_name,p_word)

def user_exist(u_name,p_word):
    '''
    Function to check if the user exists
    '''
    return User.user_exists(u_name,p_word)

def create_account(acc_name,user_name,password):
    '''
    Function to create a new account
    '''
    new_account = Account(acc_name,user_name,password)
    return new_account

def save_account(account):
    '''
    Function to save a new account
    '''
    account.save_account()

def del_account(account):
    '''
    Fuction to delete an account
    '''
    account.delete_account()

def display_accounts():
    '''
    Function to display all accounts
    '''
    return Account.display_account()

def find_account(acc_name):
    '''
    Function to find an account with its name
    '''
    return Account.find_account_by_name(acc_name)

def check_account_exists(acc_name):
    '''
    Function to see if an account exists
    '''
    return Account.account_exists(acc_name)

def copy_password(name):
    '''
    Function to copy an accounts password to email
    '''
    found_acc = Account.find_account_by_name(name)
    pyperclip.copy(found_acc.password)
    return pyperclip.paste()



def main():
    print('Welcome to the PASSWORD LOCKER')
    print('\n')

    while True:
        print("Would you like to sign up or login?")
        print("Use short codes: su - to sign up, li - to log in or ex - to exit")

        short_code = input().lower()

        if short_code == 'su':
            print("New user account")
            print('-'*10)

            print("First name ....")
            fname = input()

            print("Last name ....")
            lname = input()

            print("Username ....")
            uname = input()

            print("Password ....(8+ Characters for a strong password)")
            pword = input()

            save_users(create_user(fname,lname,uname,pword))
            print('\n')
            print(f"{fname} {lname}, you have successfully signed up")
            print("You can now log in and experience the password-locker")
            print("\n")

        elif short_code == 'li':
            print("Enter your username:")
            u_name = input()
            print("Enter Password:")
            p_word = input()

            if user_exist(u_name,p_word):
                searched_user = find_users(u_name,p_word)
                print(f"{searched_user.first_name} {searched_user.last_name}, you have successfully logged in")
                print('-'*10)

                while True:
                    print("\n")
                    print(f"{searched_user.first_name}, what would you like to do?")
                    print("-"*10)
                    print("\n")

                    print("Use the following short codes: ca - create a password-locker account, da - display your saved accounts, fa - find an account, del - delete an account, copy - copy an accounts password or ex - exit")
                    print("\n")

                    short_code = input().lower()

                    if short_code == 'ca':

                        print("ea - create from an existing credentials account or na - create new credentials")
                        codes = input().lower()

                        if codes == 'ea':
                            print("Credentials Account")
                            print('-'*10)

                            print("Name of the account")
                            a_name = input()

                            print("Account Username")
                            usname = input()

                            print("Account password")
                            psword = input()

                            save_account(create_account(a_name,usname,psword))
                            print('\n')
                            print(f"{a_name} {usname} {psword}")
                            print('Your credential\'s account has been saved')
                            print("*"*10)
                            print('\n')

                        elif codes == 'na':
                            print("Credentials Account")
                            print('-'*10)

                            print("Name of the account")
                            a_name = input()

                            print("Account Username")
                            usname = input()
                            print("Would you like to create your own password or be generated one?")
                            print("own - Create your own password or gen - Be generated a password")
                            answ = input().lower()
                            
                            if answ == "own":
                                print("8+ characters for a strong password")
                                psword = input()

                            elif answ == 'gen':
                                choices = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+'
                                length = len(choices)
                                print("Give the length to your password: Use numbers not words")
                                if int:
                                    lent = int(input())
                                else:
                                    print("Use numbers not words")
                                    lent = int(input())
                                psword = "".join(random.sample(choices,lent))
                                print(f"Your new password is '{psword}'")
                            else:
                                print("Use the choices given above")

                            save_account(create_account(a_name,usname,psword))
                            print(f"{a_name} {usname} {psword}")
                            print("Your credential account has been successfully created")
                            print("*"*10)

                    elif short_code == 'da':
                        if display_accounts():
                            print("Here is a list of all your credential accounts:")
                            print('\n')

                            for account in display_accounts():
                                print(f"{account.name} -- {account.username} -- {account.password}")
                                print("*"*10)
                                print('\n')

                        else:
                            print('You dont have any accounts yet')
                            print('\n')

                    elif short_code == 'del':
                        print("Enter the following:")
                        print("Account name")
                        acnt_name = input()

                        if check_account_exists(acnt_name):
                            deleted_account = find_account(acnt_name)
                            del_account(deleted_account)

                            print(f"{deleted_account.name} account has been succesfully deleted")
                            print('*'*10)

                        else:
                            print("Could not find that credential")
                                 

                    elif short_code == "fa":
                        print("Enter the account name for the account you would like to search for")

                        search_account = input()
                        print('\n')
                        if check_account_exists(search_account):
                            search_account = find_account(search_account)
                            print(f"{search_account.name} --- {search_account.username} --- {search_account.password}")
                            print('*' * 10)
                        else:
                            print("That account does not exist")

                    elif short_code == 'copy':
                        print('\n')
                        print("Enter account name of the password you would like to copy")
                        ac_name = input()
                        print('\n')
                        if check_account_exists(ac_name):
                            account = find_account(ac_name)
                            copy_password(account.name)
                            print(f"{account.name}'s password copied to clipboard")

                    elif short_code == "ex":
                        print("Bye ...Till next time")
                        print("\n")
                        break

                    else:
                        print("I really didn't get that. Please use the short codes provided")
            else:   
                print("\n")
                print("You have inputted the wrong username or password")
                print("\n")


if __name__ == '__main__':
    main()