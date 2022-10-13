"""
These module were imported to allow the code to connect with the google
sheet.
"""
import pprint
import gspread
import time
from colorama import Fore
from google.oauth2.service_account import Credentials
from validate_password import validate_password

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('ci_pp3_ppm')


def logo():
    """
    Display password logo in green
    """
    print(" ")
    print(Fore.BLUE + "Welcome to:")
    print(" ")
    print(Fore.GREEN + " ____________________________________________________________________________________________________ ")
    print(Fore.GREEN + "|    ____       ___          ___        ___    __                  __     ___     _____      ____    |")
    print(Fore.GREEN + "|   / __ \     /   \        /    \     /    \  \ \                / /   / __ \   |  __  \   |  _ \   |")
    print(Fore.GREEN + "|  | /  \ |   /  _  \      /  /\__\   /  /\__\  \ \      __      / /   / /  \ \  | |  | |   | | \ \  |")
    print(Fore.GREEN + "|  | \__/ |  /  /_\  \     \  \       \  \       \ \    /  \    / /   | |    | | | |__| |   | |  | | |")
    print(Fore.GREEN + "|  |  ___/  /   ___   \   __ \  \   __ \  \       \ \  / /\ \  / /    | |    | | |  __  \   | |  | | |")
    print(Fore.GREEN + "|  | |     /  /     \  \  \ \/  /   \ \/  /        \ \/ /  \ \/ /      \ \__/ /  | |  \  \  | |_/ /  |")
    print(Fore.GREEN + "|  |_|    /__/       \__\  \___/     \___/          \__/    \__/        \____/   |_|   \__\ |____/   |")
    print(Fore.GREEN + "|____________________________________________________________________________________________________|")
    print(" ")
    print(" ")
    print(Fore.BLUE + "Your Personal Password Manager")
    print(" ")
    print(" ")
    time.sleep(1)


logo()
# welcome message
name = input("Input your name: ").lower()
print("Hi " + name + ", Welcome to your personal password manager!")

# This if statemant will be used for the log in screen to see if
# they want to create an account or login to an existing account.


def setup() -> str:
    answer = input("Create account or Login ").lower()
    return answer


def check_for_master_account():
    settings_worksheet = SHEET.worksheet('settings')
    check_for_account = settings_worksheet.acell('B2').value
    return check_for_account


def login():
    login_username = input('Input your username: ')
    login_password = input('Input your password: ')
    settings_worksheet = SHEET.worksheet('settings')
    actual_username = settings_worksheet.acell('B2').value
    actual_password = settings_worksheet.acell('C2').value
    return login_username, login_password, actual_username, actual_password


def view_passwords():
    """
    This Function is used to pull the passwords from
    the database and display them in the terminal.
    """
    print("Retriving passwords!... ")
    all_passwords = SHEET.worksheet(
        "password_manager").get_all_values()
    return all_passwords


def add_passwords():
    new_website = input("Input the website: ").lower()
    password_manager_worksheet = SHEET.worksheet(
        'password_manager')
    current_stored_website = password_manager_worksheet.find(
        new_website)
    return new_website, current_stored_website


def edit_passwords():
    find_account = input("Account you would like to edit \
the password: ").lower()
    password_manager_worksheet = SHEET.worksheet(
        'password_manager')
    cell_of_account = str(
        password_manager_worksheet.find(find_account))
    if (cell_of_account[8]) == 'C':
        column_of_account = int(cell_of_account[9]) + 2
        row_of_account = cell_of_account[7]
    else:
        column_of_account = int(cell_of_account[10]) + 2
        row_of_account = cell_of_account[7:9]
    new_password = input("input your new password: ")
    # update cell of account
    password_manager_worksheet.update_cell(
        row_of_account, column_of_account, new_password)


def main():
    """
    This function it to return the user to the create account
    or login screen if they have an account already set up.
    """
    answer = setup()

    if answer == "create account":     

        def create_master_account():
            """
            Create the master pwd and username for your
            personal pwd manager account
            """
            check_for_account = check_for_master_account()
            while True:
                if check_for_account is None:
                    master_account_username = input("Create your\
                        manager username: ")
                    print(f"Storing username {master_account_username} ...\n")
                    while True:
                        master_account_password = input("create your\
                             master password: ")
                        password_to_validate = master_account_password
                        if validate_password(password_to_validate):
                            print(f"Storing password \
                                {master_account_password} ...\n")
                            break
                else:
                    should_restart = True
                    break

                return name, master_account_username, master_account_password
            if should_restart:
                print("Account already set up try log in")
                main()

        def update_settings_worksheet(master_data):
            """Update ssettings worksheet with the master data"""
            settings_worksheet = SHEET.worksheet('settings')
            settings_worksheet.append_row(master_data)
        master_data = create_master_account()
        print(master_data)
        update_settings_worksheet(master_data)

    # The functions below here will be for the steps
    # that will occure once logged in.
    elif answer == "login":
        login_username, login_password, actual_username,\
            actual_password = login()
        if login_username == actual_username\
                and login_password == actual_password:
            print("login.....")
        else:
            print("Username and password didn't match our records")
            main()

        def options():
            """function used to return to the option input"""
            print("Type 1 to View, 2 to add, 3 to edit,\
4 to edit master pwd & 5 to exit")
            option = input('Type 1, 2, 3, 4 or 5: ')
            if option == "1":
                print("You selected to view your passwords")
                all_passwords = view_passwords()
                pprint.pprint(all_passwords)
                options()

            elif option == "2":
                print("You selected to add a new password")
                new_website, current_stored_website = add_passwords()
                if str(new_website) in str(current_stored_website):
                    print(f"{new_website} already exsists.")
                    print('Try adding a digit aftwer the name to \
differenciate it from the others')
                    options()

                else:

                    def store_password():
                        """
                        store a new website, username & password 
                        into the database.
                        """
                        
                        print(f"Storing website {new_website} ...\n")
                        new_username = input("Input your username: ")
                        print(f"Storing username {new_username} ...\n")

                        while True:
                            new_password = input("Input your password: ")
                            password_to_validate = new_password
                            if validate_password(password_to_validate):
                                print(f"Storing password \
                                    {new_password} ...\n")
                                break
                        return new_website, new_username, new_password

                    def update_password_manager_worksheet(new_data):
                        """
                        Update password_manager worksheet
                        with the master data
                        """
                        print("Updating password_manager worksheet ...\n")
                        password_manager_worksheet = SHEET.worksheet(
                            'password_manager')
                        password_manager_worksheet.append_row(new_data)
                        print("password manager updated sucessfully.\n")

                    new_data = store_password()
                    print(new_data)
                    update_password_manager_worksheet(new_data)
                    options()

            elif option == "3":
                print("You selected to edit a password")
                edit_passwords()
                options()

            elif option == "4":
                print("You selected to edit master password")
                find_account = input("Account name you would like\
to edit the password: ").lower()
                settings_worksheet = SHEET.worksheet('settings')
                cell_of_account = str(settings_worksheet.find(find_account))
                column_of_account = int(cell_of_account[9]) + 2
                row_of_account = cell_of_account[7]
                new_password = input("input your new password: ")
                # update cell of account
                settings_worksheet.update_cell(
                    row_of_account, column_of_account, new_password)
                options()

            elif option == "5":
                print("you have selected to log it. Thank you, Good Bye!")
                main()
            else:
                print("You did not enter a valid response!. ")
                options()
        options()
    else:
        print("You did not enter a valid response!. ")
        main()


main()
