"""
These module were imported to allow the code to connect with the google
sheet.
"""
import pprint
import time
import gspread
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
    and Font in cyan.
    """
    print(" ")
    print(Fore.CYAN + " Welcome to:")
    print(" ")
    print(Fore.GREEN + " _______________________________________________ ")
    print(Fore.GREEN + "|    ____    __                  __   _____     |")
    print(Fore.GREEN + "|   / __ \   \ \                / /  |  __  \   |")
    print(Fore.GREEN + "|  | /  \ |   \ \      __      / /   | |   \ \  |")
    print(Fore.GREEN + "|  | \__/ |    \ \    /  \    / /    | |   | |  |")
    print(Fore.GREEN + "|  |  ___/      \ \  / /\ \  / /     | |   | |  |")
    print(Fore.GREEN + "|  | |           \ \/ /  \ \/ /      | |__/ /   |")
    print(Fore.GREEN + "|  |_|            \__/    \__/       |_____/    |")
    print(Fore.GREEN + "|_______________________________________________|")
    print(" ")
    print(" ")
    print(Fore.CYAN + " Your Personal Password Manager")
    print(" ")
    print(" ")
    time.sleep(1)


logo()
name = input(" Input your name: \n ").lower()
print(Fore.MAGENTA + " Hi " + name + ", Welcome to your\
 personal password manager! \n")


def setup() -> str:
    """
    To get input from the user if they want to create account or log in
    """
    print(Fore.MAGENTA + " Create an account if you have\
 not yet created one.\n")
    print(Fore.MAGENTA + " Step 1: Create an account.")
    print(Fore.MAGENTA + " Step 2: Login.")
    print(Fore.MAGENTA + " You only need to create an account once \n")
    print(Fore.CYAN + " To continue type: ")
    answer = input(" 'Create account' or 'Login': \n ").lower()
    return answer


def check_for_master_account() -> str:
    """
    To get input from the user if they want to create account or log in
    """
    settings_worksheet = SHEET.worksheet('settings')
    check_for_account = settings_worksheet.acell('B2').value
    return check_for_account


def login() -> str:
    """
    This function allows you to login to the account.
    """
    print(Fore.CYAN + " To login input your master details below: \n")
    login_username = input(' Input your username: \n ').lower()
    login_password = input(' Input your password: \n ')
    settings_worksheet = SHEET.worksheet('settings')
    actual_username = settings_worksheet.acell('B2').value
    actual_password = settings_worksheet.acell('C2').value
    return login_username, login_password, actual_username, actual_password


def view_passwords() -> str:
    """
    This Function is used to pull the passwords from
    the database and display them in the terminal.
    """
    print(Fore.MAGENTA + " Retriving passwords!... ")
    all_passwords = SHEET.worksheet("password_manager").get_all_values()
    return all_passwords


def add_passwords() -> str:
    """
    Add new websites to the google sheet
    """
    new_website = input(Fore.CYAN + " Input the website: \n ").lower()
    password_manager_worksheet = SHEET.worksheet('password_manager')
    current_stored_website = password_manager_worksheet.find(
        new_website)
    return new_website, current_stored_website


def update_password_manager_worksheet(new_data):
    """
    Update password_manager worksheet
    with the master data
    """
    password_manager_worksheet = SHEET.worksheet('password_manager')
    password_manager_worksheet.append_row(new_data)
    print(Fore.GREEN + " password manager updated sucessfully.\n")


def edit_passwords() -> str:
    """
    Edit the passwords in the google sheet
    """
    find_account = \
        input(Fore.CYAN + " Website's password to edit: \n ").lower()
    password_manager_worksheet = SHEET.worksheet('password_manager')
    cell_of_account = str(
        password_manager_worksheet.find(find_account))
    print(find_account)
    if find_account in cell_of_account:
        if (cell_of_account[8]) == 'C':
            column_of_account = int(cell_of_account[9]) + 2
            row_of_account = cell_of_account[7]
        else:
            column_of_account = int(cell_of_account[10]) + 2
            row_of_account = cell_of_account[7:9]
        new_password = input(" New password: \n ")
        password_manager_worksheet.update_cell(
            row_of_account, column_of_account, new_password)
    else:
        print(Fore.RED + "This account does not exsist")


def edit_master_password() -> str:
    """
    Edit the master password in the google sheet
    """
    find_account = input(Fore.CYAN + " Enter your name: \n ").lower()
    settings_worksheet = SHEET.worksheet('settings')
    cell_of_account = str(settings_worksheet.acell('A2').value)
    if find_account in cell_of_account:
        new_password = input(" New password: \n ")
        settings_worksheet.update('C2', new_password)
    else:
        print(Fore.RED + "This account does not exsist \n ")
        print(Fore.RED + "Please try again")


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
                    print(Fore.CYAN + " Create a username below:")
                    master_account_username = input(" Username: \n").lower()
                    print(Fore.CYAN + " Create a password below: \n")
                    print(Fore.WHITE + " Must be 8 characters or more:")
                    print(Fore.WHITE + " Must contain one of each:")
                    print(Fore.WHITE + " Lowercase, Uppercase")
                    print(Fore.WHITE + " Number & special '@$_' \n")
                    master_account_password =\
                        input(Fore.CYAN + " Password: \n")
                    password_to_validate = master_account_password
                    if validate_password(password_to_validate):
                        print(Fore.GREEN + " Password Stored \n")
                        print(Fore.WHITE + 'Remember the details to login \n')
                        print(Fore.WHITE + "Only 1 account can be stored: \n")

                        return name, master_account_username,\
                            master_account_password
                else:
                    print(Fore.RED + " Account already set up try log in")
                    break

        def update_settings_worksheet(master_data):
            """Update settings worksheet with the master data"""
            settings_worksheet = SHEET.worksheet('settings')
            settings_worksheet.append_row(master_data)

        master_data = create_master_account()
        print(master_data)
        update_settings_worksheet(master_data)
        main()

    elif answer == "login":
        login_username, login_password, actual_username, actual_password\
            = login()
        if login_username == actual_username\
                and login_password == actual_password:
            print(Fore.GREEN + " logged in")
        else:
            print(Fore.RED + " Username and password didn't match our records")
            main()

        def options() -> str:
            """Function used to return to the option input"""
            print(Fore.MAGENTA + " Type 1: View, 2: Add, 3: Edit,")
            print(Fore.MAGENTA + " 4: Edit master pwd, 5: Exit \n")
            print(Fore.MAGENTA + " First store a password in option: 2. \n")
            option = input(Fore.CYAN + ' Type 1, 2, 3, 4 or 5: \n ')
            if option == "1":
                print(Fore.YELLOW + " Viewing your passwords \n")
                all_passwords = view_passwords()
                pprint.pprint(all_passwords)
                options()

            elif option == "2":
                print(Fore.YELLOW + " Adding a new Website \n")
                new_website, current_stored_website = add_passwords()
                if str(new_website) in str(current_stored_website):
                    print(Fore.RED + f" {new_website} already exists. \n")
                    print(Fore.RED + ' Try adding a digit after the name')
                    print(Fore.RED + ' Make it different to the others \n')
                    options()

                else:

                    def store_password():
                        """
                        store a new website, username & password
                        into the database.
                        """
                        new_username = input(Fore.CYAN + " Input username: \n")

                        while True:
                            print(Fore.WHITE + " Password requirements:")
                            print(Fore.WHITE + " Must be 8 characters + :")
                            print(Fore.WHITE + " Must contain one of each:")
                            print(Fore.WHITE + " Lowercase, Uppercase")
                            print(Fore.WHITE + " Number & special '@$_' \n")
                            new_password = input(" Input password: \n ")
                            password_to_validate = new_password
                            if validate_password(password_to_validate):
                                break
                        return new_website, new_username, new_password

                    new_data = store_password()
                    update_password_manager_worksheet(new_data)
                    print(new_data)
                    options()

            elif option == "3":
                print(Fore.YELLOW + " Editing a password: \n")
                edit_passwords()
                print(Fore.GREEN + " Password Updated \n")
                options()

            elif option == "4":
                print(Fore.YELLOW + " Editing master password: \n")
                edit_master_password()
                print(Fore.GREEN + " Password Updated \n")
                options()

            elif option == "5":
                print(Fore.YELLOW + " Loging out. Thank you, Good Bye! \n")
                main()
            else:
                print(Fore.RED + " You did not enter a valid response!.\n")
                options()
        options()
    else:
        print(Fore.RED + " You did not enter a valid response!. \n")
        main()


if __name__ == "__main__":
    main()
