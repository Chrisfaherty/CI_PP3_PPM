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

if answer == "Create account":

    def create_master_account():
        """create the master pwd and username for your personal pwd manager acc"""
        # welcome message
        name = input("Input your name: ")
        print("Hi " + name + ", Welcome to your personal password manager!")
        master_account_username = input("Create your manager accounts user name: ")
        print(f"Storing username {master_account_username} ...\n")

        while True:
            master_account_password = input("create your master accounts password: ")
            if validate_password(master_account_password):
                print(f"Storing password {master_account_password} ...\n")
                break

        return name, master_account_username, master_account_password


    def validate_password(password_to_validate):
        """
        Inside the try, checks to make sure the password contains a capital letter,
        lowercase letter & a special character.
        Raises ValueError if the password does not contain a lowercase & uppercase,
        or if there aren't more than 6 values. credits geeksforgeeks.org
        """
        l, u, p, d = 0, 0, 0, 0
        s = password_to_validate
        capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        smallalphabets="abcdefghijklmnopqrstuvwxyz"
        specialchar="$@_"
        digits="0123456789"
        if (len(s) >= 8):
            for i in s:
        
                # counting lowercase alphabets
                if (i in smallalphabets):
                    l+=1           
        
                # counting uppercase alphabets
                if (i in capitalalphabets):
                    u+=1           
        
                # counting digits
                if (i in digits):
                    d+=1           
        
                # counting the mentioned special characters
                if(i in specialchar):
                    p+=1       
        if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):
            print("Valid Password")
        else:
            print("Invalid Password")
            print("Must be 8 + characters, lowercase, uppercase & special character @$_")
            return False
        
        return True


    def update_settings_worksheet(master_data):
        """Update sales worksheet with the master data"""
        print("Updating settings worksheet ...\n")
        settings_worksheet = SHEET.worksheet('settings')
        settings_worksheet.append_row(master_data)
        print("Settings updated sucessfully.\n")


    master_data = create_master_account()
    print(master_data)
    update_settings_worksheet(master_data)


else:
    