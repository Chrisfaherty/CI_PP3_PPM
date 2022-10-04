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


def create_master_account():
    """
    create the master password and user name for your
    personal password manager account
    """
    while True:
        name = input("Input your name: ")
        print("Hi " + name + ", Welcome to your personal password manager!")

        master_username = input("Create your account username: ")
        print("saving username...\n")

        master_password = input("create your account password: ")
        print("saving password...\n")

        master_account_details = [name, master_username, master_password]

        print(master_account_details)

    return master_password