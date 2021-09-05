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