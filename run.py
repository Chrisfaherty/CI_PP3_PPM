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
name = input("Input your name: ")
print("Hi " + name + ", Welcome to your personal password manager!")

"""
This if statemant will be used for the log in screen to see if
they want to create an account or login to an existing account
"""
answer = input("Create account or Login ").lower()

if answer == "create account":

    def create_master_account():
        """create the master pwd and username for your personal pwd manager acc"""

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

    """The functions below here will be for the steps that will occure once logged in. """
elif answer == "login":
    print("login.....")
    print("Type 1 to View, 2 to add, 3 to edit & 4 to edit master pwd")

    option = input('Type 1, 2, 3 or 4: ')

    if option == "1":
        print("View Passwords")

    elif option == "2":
        print("You selected add password")

        def store_password():
            """store a new password"""
            new_website = input("Input the website: ")
            print(f"Storing website {new_website} ...\n")

            new_username = input("Input your username: ")
            print(f"Storing username {new_username} ...\n")

            while True:
                new_password = input("Input your password: ")
                if validate_password(new_password):
                    print(f"Storing password {new_password} ...\n")
                    break

            return new_website, new_username, new_password
        

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


        def update_password_manager_worksheet(new_data):
            """Update password_manager worksheet with the master data"""
            print("Updating password_manager worksheet ...\n")
            password_manager_worksheet = SHEET.worksheet('password_manager')
            password_manager_worksheet.append_row(new_data)
            print("password manager updated sucessfully.\n")


        new_data = store_password()
        print(new_data)
        update_password_manager_worksheet(new_data)


    elif option == "3":
        print("Edit Password")

    elif option == "4":
        print("Edit Master Password")

    else:
        print("You did not enter a valid response!. ")


else:
    print("You did not enter a valid response!. ")

