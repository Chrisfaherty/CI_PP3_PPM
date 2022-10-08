"""
These module were imported to allow the code to connect with the google
sheet.
"""
import gspread
from google.oauth2.service_account import Credentials
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('ci_pp3_ppm')

# welcome message

# welcome message
name = input("Input your name: ")
print("Hi " + name + ", Welcome to your personal password manager!")


def create_master_account():
    """create the master password and user name for your personal password manager account"""
    master_account_username = input("Create your manager accounts user name: ")
    print(f"Storing username {master_account_username}...\n")

    master_account_password = input("create your master accounts password: ")
    print(f"Storing password {master_account_password}...\n")


create_master_account()