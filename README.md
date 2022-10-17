# Personal Password Manager
(Developer: Christopher Faherty)

![This is an screenshot of the responsive design image](./docs/ppm_welcome_screen.png)

[Live Webpage](https://ci-pp3-ppm.herokuapp.com/)

## About

This is a command line verson of a password manager.

This password manager allows the user to store one main account. It then allows that user to view, add and edit their passwords.

With the pace of everything going digital and everyone having different accounts for everything, its human nature to take the easy route and use the same password for every account. This has a huge impact on your security and shows why password managers are vital today more than ever.

## Table of Contents

1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requirements and Expectations](#user-requirements-and-expectations)
    3. [User Manual](#user-manual)
    4. [User Stories](#user-stories)
3. [Technical Design](#technical-design)
    1. [Flowchart](#flowchart)
4. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Framework and Tools](#framework-and-tools)
    3. [libraries](#libraries)
5. [Features](#features)
6. [Testing](#testing)
    1. [Validator Testing](#validator-testing)
    2. [Testing user stories](#testing-user-stories)
8. [Bugs](#bugs)
9. [Deployment](#deployment)
10. [Credits](#credits)
11. [Acknowledgements](#acknowledgements)

## Project Goals

### User Goals
* Storing my passwords and connecting them to a username and website,
* View all my passwords in the terminal,
* Add new passwords as required,
* Find and edit a specific password,
* Edit the master accounts password.


### Site Owner Goals
* Create a password managar that I would use myself,
* Create an easy flow for the user to navigate the terminal,
* Provide feedback when the user inputs incorrect information.


## User Experience

### Target Audience
* People that find it hard to remember a lot of passwords,
* People with a lot of online accounts,
* People looking to improve their online security.

### User Requirements and Expectations
* A welcome screen with a short description of what the site is,
* A easy to follow flow of information,
* Feedback if the incorrect value in input,
* Passwords to be presented in an easy to read format,
* Color codeing to help guide the User,

### User Manual
<details><summary>Instructions</summary>

#### Welcome
On the welcome screen the project logo is displayed and it explains that this is a personal password manager.
The first thing you have to do in input your name in the field and press enter.

#### Main
After entering your name you in the welcome screen you are greeted. The next step is to create your account assuming this is the first time using this password manager. 
To create an account type "create account" into the prompt window. It is importing to have the space in between create and account.

#### Create account
The first thing you have to do is create a user name and press enter. Next you have to create a password. The program displays the password criteria. 
The password must be longer than 8 characters, it must contain at least 1 uppercase and lowercase character, it must have at least one number and include one of the following special characters "@$_". This is to ensure you create a strong password. Once the password is created and you press enter it will let you know if the password was correct and stored. 
It will also give a reminder that only one user is stored as it is your personal password manager so you have to remember your login details and keep them safe.
Note: Make sure to write down your user name and password exactly or you will not be able to log into the password manager if you forget them.

#### Login function
After creating your account you are returned to the main screen. This gives you 2 options to create an account or to log in. By this point your account should be created so you can login.
Type login into the prompt. To login you will first be asked to enter your user name that you created for your master account. Once you enter your username it will ask you to enter your password.
Once you enter your password and press enter it will say your logged in if everything was correct and take you to the login function screen. 
The login function screen is where you get to choose what to do next. View your passwords, add a new website, edit your passwords, edit your master password & exit to the main screen.
If this is your first time in the password manager you should go to option 2 first and add a few websites you want to store the passwords for.

#### Adding a website
After you entered 2 into the prompt the program began the process to add a new website. The first thing you are asked to do is enter the website you want to store a password for and press enter. 
Now type in your username for that account and press enter. Now you create a password for this account. The password criteria is displayed, once the password is created press enter. 
If everything is ok it will display valid password and that the password manager updated sucessfully. Then you are returned to the login function screen.
You can repeat these steps a couple of times to enter all your websites.
Note: You can't enter the same website twice or it will give an error. The best thing to do is to add a number to the end of the website if you want to add a few accounts for the same website (facebook, facebook1, facebook2, ....).

#### Viewing passwords
After adding your passwords you will be able to view them by entering 1 in the login function screen where you have options 1 - 5.
Once you hit enter the program will pull all your stored passwords and display them on the screen for you. 
It then returns you back to the login function.

#### Editing passwords
You can also edit your passwords if you enter 3 in the login function screen. 
The first thing you are asked is to enter the website for the password you want to edit.
If the website you entered is stored in the system it will then ask you to enter a new password.
Once the new password is created and it meets the password criteria it will let you know if the password was updated and return you to the login function screen.

#### Editing the master password
To edit your master password you need to enter 4 at the login function screen.
The program will ask you to enter your name "This is not your username".
After your name is accepted it will ask you to enter a new password.
If your password meets the criteria it will display a message saying password updated.
You will then be returned to the login function screen.

#### Exit 
Once you are finished in your password manager you gan enter 5 in the login function screen. This will return you to the main screen.

</details>

[Back to Table Of Contents](#table-of-contents)

### User Stories

#### First-time  User
1. I want to the password manager to flow and be easy to follow,
2. I want to be able to create a master username and password to protect my passwords,
3. I want to have clear options displayed when dicisions are to be made,
4. I want to be able to view all my passwords in an organised form,
5. I want to be able to easly add new passwords,
6. I want to be able to edit my master password or user passwords if required,
7. I want to be able to get feedback if i enter something incorrectly, 

#### Site Owner
8. I want users to enjoy the experiance to make their personal password manager,
9. I want users to easily navigate the site,
10. I want users to be able to use the functions with out an issue,
11. I want users to know if there was an issue and how to resolve it,

## Technical Design

### Flowchart

The following flowchart sumerises the structure of the password manager.
<details><summary>Overview</summary>
<img src="docs/features/ppm_flow_main.png">
</details>

<details><summary>Options</summary>
<img src="docs/features/ppm_flow_option_1.png">
<img src="docs/features/ppm_flow_option_2.png">
<img src="docs/features/ppm_flow_option_3.png">
<img src="docs/features/ppm_flow_option_4.png">
</details>

<details><summary>Exit Loop</summary>
<img src="docs/features/ppm_flow_option_5.png">
</details>

## Technologies Used

### Languages
* [Python](https://www.python.org/) The language used for the logic of the project.

### Framework and Tools
* [Git](https://git-scm.com/) Used for version control to push the code to GitHub.
* [GitHub](https://github.com/) Used as a repository to store the projects code.
* [lucidchart](https://www.lucidchart.com/) Used to create the project flow.
* [Google Cloud Platform](https://cloud.google.com/cloud-console/) Used to manage access and permissions Google auth & sheets to google services.
* [Google Sheets](https://www.google.co.uk/sheets/about/) Used to store the passwords.
* [Heroku Platform](https://www.heroku.com) Used to deploy the project.

### Libraries

#### Python Libraries
* [Time](https://docs.python.org/3/library/time.html) - Used to delay the user input after the welcome message is displayed.
* [PrettyPrinter](https://docs.python.org/3/library/pprint.html) - Used pprint to display the passwords in a organised format for option 1.
* [Pycodestyle](https://pypi.org/project/pycodestyle/) - Used to check Python code against some of the style conventions in PEP 8.

#### Third Party Libraries
* [colorama](https://pypi.org/project/colorama/) JUSTIFICATION: Colorama was used add color to the Welcome message. It was also used to help the user notice if something was sucessful with green and an error with red.
* [gspread](https://docs.gspread.org/) JUSTIFICATION: I used gspread to add and manipulate data in my Google spreadsheet and to interact with Google APIs. This was required to store the passwords and user details and edit them.
* [google.oauth2.service_account](https://google-auth.readthedocs.io/en/master/) JUSTIFICATION: Used to set up the authentification needed to access the Google API and connect my Service Account with the Credentials function. A creds.json file was created with all details the API needs to access the google account.


## Features


### Existing Features

* Welcome Screen
    * This welcome screen includes a logo front and center and a place to input your name to make it personal.
    * User story: 1, 8.

![This is an screenshot of the Welcome Screen](docs/ppm_welcome_screen.png)

* Main Screen
    * The main screen is where the user is welcomed to the password manager.
    * Information is displayed to explain what steps the user should take. 
    * It also asks for the user to input its next step.
    * User stories: 1, 3, 9.

![This is an screenshot of the main screen](docs/features/main_screen.png)

* Create Account Screen & Google Sheet
    * This is the process flow the user goes down when it selects create account at the main screen.
    * The user is prompted to create a username and a password. 
    * The user recieves criteria around what has to be included in the password for it to be valid.
    * The user then is noitfied if the password is valid.
    * The user is warned to make sure to remember their account details and it shows the account details for the last time.
    * User stories: 2, 3, 10.

![This is an screenshot of the create account screen](docs/features/create_account_screen.png)

![This is an screenshot of the settings google sheet](docs/features/settings_google_sheet.png)

* Login Function Screen
    * The login function prompts the user to input the username and password they created.
    * Then it gives feedback if it was correct.
    * Then it gives 5 options for the user to choose. 
    * User stories: 1, 3, 9, 10.

![This is an screenshot of the login in screen](docs/features/login_screen.png)

* Adding a website screen, Option 2:
    * To get to this point the User input 2 in the login function screen.
    * The user is prompted to input a website, a username and a password.
    * The user is presented with the criteria to create a valid password.
    * User stories: 3, 5, 9, 10.

![This is an screenshot of option 2](docs/features/adding_new_website_screen.png)
![This is an screenshot of the google sheet](docs/features/password_manager_google_sheet.png)

* Viewing passwords screen, Option 1:
    * To get to this point the user selected 1 in the login function screen.
    * This function pulls the passwords that the user stored and displays them in the terminal.
    * There is also a prompt to store a password if you have not yet done so.
    * User stories: 3, 4, 9, 10.

![This is an screenshot of the viewing passwords screen](docs/features/view_passwords_screen.png)

 * Editing passwords screen, Option 3:
    * To get to this point the user selected 3 in the login function screen.
    * The function is used to edit / change a password on one of the stored websites.
    * The user is requested to input the website they want to change the password for.
    * The user then is prompted to input the new password.
    * User stories: 3, 6, 9, 10.

![This is an screenshot of the editing passwords screen](docs/features/edit_password_screen.png)
![This is an screenshot of the updated settings sheet](docs/features/edit_password_example.png)

 * Editing master password screen, Option 4:
    * To get to this point the user selected 4 in the login function screen.
    * This function is used to edit the master password.
    * The user is prompted to enter their name,
    * Then they are prompted to enter the new password.
    * They are then notified if the password was updated.
    * User stories: 3, 6, 9, 10.

![This is an screenshot of the edit master password screen](docs/features/edit_master_password_screen.png)
![This is an screenshot of the updated settings excel sheet](docs/features/updated_settings_google_sheet.png)

 * Exiting to the login screen, Option 5:
    * To get to this point the user selected 5 in the login function screen.
    * This function returns the user to the main screen.
    * User stories: 9, 10.

![This is an screenshot of the exit option screen](docs/features/edit_master_password_screen.png)

 * Error message for passwords:
    * This is the prompt that shows if the user does not follow the create password criteria.
    * User stories: 3, 7, 11.

![This is an screenshot of the exit option screen](docs/features/invalid_password_error_message.png)

* Error message for invalid input:
    * This is the prompt that shows if the user inputs an incorrect value.
    * User stories: 3, 7, 11.

![This is an screenshot of the exit option screen](docs/features/invalid_input_error_message.png)

[Back to Table Of Contents](#table-of-contents)



## Testing

* Testing was condicted in three ways.
    * Testing the code with the pycodestyle extension.
    * Testing the code manually with the user stories.
    * Testing the password validation code with unit testing.

### Validator Testing
* pycodestyle
    * No errors were found when passing the site pages through the [pycodestyle validator](https://pypi.org/project/pycodestyle/)
    * Warnings were noted in the run.py file with the logo. This was due to the code thinking it was an excape sequance when using slashed.

    <details><summary>pycodestyle</summary>
    <img src="docs/testing/pycodestyle_ci_pp3_ppm.png">
    </details>

    <details><summary>run.py</summary>
    <img src="docs/testing/run_code_pep8.png">
    </details>

    <details><summary>validate_password.py</summary>
    <img src="docs/testing/validate_password_code_pep8.png">
    </details>

    <details><summary>test_validation.py</summary>
    <img src="docs/testing/test_validation_code_pep8.png">
    </details>


### Testing user stories
1. I want to the password manager to flow and be easy to follow.

| **Feature** | **Action** | **Expected Results** | **Actual Result** |
|-------------|------------|----------------------|-------------------|
| Main screen | Input your name | User is presented with options on how to proceed | Works as expected |
| Login Function screen | Input login | User is asked to input their user name and password | Works as expected |
| Login Function screen | Input username & password | User is given 5 options to choose from along with information on what should be done first | Works as expected |

<details><summary>Screenshots</summary>
<img src="docs/testing/user_story_1_1.png">
<img src="docs/testing/user_story_1_2.png">
<img src="docs/testing/user_story_1_3.png">
<img src="docs/testing/user_story_1_4.png">
</details>

2. I want to be able to create a master username and password to protect my passwords.

| **Feature** | **Action** | **Expected Results** | **Actual Result** |
|-------------|------------|----------------------|-------------------|
| Main screen | Input your name | User is presented with options on how to proceed | Works as expected |
| Login Function screen | Input create account | User is asked to create their user name and password | Works as expected |
| Create account screen| Create username & password | User is asked to create their username and password. Criteria is given to create a secure password | Works as expected |

<details><summary>Screenshots</summary>
<img src="docs/testing/user_story_1_1.png">
<img src="docs/testing/user_story_2_1.png">
<img src="docs/testing/user_story_2_2.png">
</details>

3. I want to have clear options displayed when dicisions are to be made.

| **Feature** | **Action** | **Expected Results** | **Actual Result** |
|-------------|------------|----------------------|-------------------|
| Main screen | Input your name | User is presented with options on how to proceed | Works as expected |
| Login Function screen | Input login | User is asked to input their user name and password | Works as expected |
| Login Function screen | Input username & password | User is given 5 options to choose from along with information on what should be done first | Works as expected |

<details><summary>Screenshots</summary>
<img src="docs/testing/user_story_1_1.png">
<img src="docs/testing/user_story_1_2.png">
<img src="docs/testing/user_story_1_3.png">
<img src="docs/testing/user_story_1_4.png">
</details>

4. I want to be able to view all my passwords in an organised form.

| **Feature** | **Action** | **Expected Results** | **Actual Result** |
|-------------|------------|----------------------|-------------------|
| Main screen | Input your name | User is presented with options on how to proceed | Works as expected |
| Login Function screen | Input login | User is asked to input their user name and password | Works as expected |
| Login Function screen | Input username & password | User is given 5 options to choose from along with information on what should be done first | Works as expected |
| Login Function screen | Input option 1 | User is presented with the stored passwords | Works as expected |

<details><summary>Screenshots</summary>
<img src="docs/testing/user_story_1_1.png">
<img src="docs/testing/user_story_1_2.png">
<img src="docs/testing/user_story_1_3.png">
<img src="docs/testing/user_story_1_4.png">
<img src="docs/testing/user_story_4_1.png">
</details>

5. I want to be able to easly add new passwords.

| **Feature** | **Action** | **Expected Results** | **Actual Result** |
|-------------|------------|----------------------|-------------------|
| Main screen | Input your name | User is presented with options on how to proceed | Works as expected |
| Login Function screen | Input login | User is asked to input their user name and password | Works as expected |
| Login Function screen | Input username & password | User is given 5 options to choose from along with information on what should be done first | Works as expected |
| Login Function screen | Input option 2 | User is presented with the stored passwords | Works as expected |
| Adding a website screen | Input the website, username & password | notice password stored sucessfully and details displayed | Works as expected |

<details><summary>Screenshots</summary>
<img src="docs/testing/user_story_1_1.png">
<img src="docs/testing/user_story_1_2.png">
<img src="docs/testing/user_story_1_3.png">
<img src="docs/testing/user_story_1_4.png">
<img src="docs/testing/user_story_5_1.png">
<img src="docs/testing/user_story_5_2.png">
</details>

6. I want to be able to edit my master password or user passwords if required.
| **Feature** | **Action** | **Expected Results** | **Actual Result** |
|-------------|------------|----------------------|-------------------|
| Main screen | Input your name | User is presented with options on how to proceed | Works as expected |
| Login Function screen | Input login | User is asked to input their user name and password | Works as expected |
| Login Function screen | Input username & password | User is given 5 options to choose from along with information on what should be done first | Works as expected |
| Login Function screen | Input option 3 for user password & 4 for master password | User is presented with the stored passwords | Works as expected |
| Adding a website screen | Input the name & password | notice password updated displayed | Works as expected |

<details><summary>Screenshots</summary>
<img src="docs/testing/user_story_1_1.png">
<img src="docs/testing/user_story_1_2.png">
<img src="docs/testing/user_story_1_3.png">
<img src="docs/testing/user_story_1_4.png">
<img src="docs/testing/user_story_6_1.png">
<img src="docs/testing/user_story_6_2.png">
</details>

7. I want to be able to get feedback if i enter something incorrectly.  

| **Feature** | **Action** | **Expected Results** | **Actual Result** |
|-------------|------------|----------------------|-------------------|
| Main screen | Input your name | User is presented with options on how to proceed | Works as expected |
| Login Function screen | Input login | User is asked to input their user name and password | Works as expected |
| Login Function screen | Input username & incorrct password | User is told it did not match our records and prompted to try again | Works as expected |


<details><summary>Screenshots</summary>
<img src="docs/testing/user_story_1_1.png">
<img src="docs/testing/user_story_1_2.png">
<img src="docs/testing/user_story_7_1.png">
</details>

8. I want users to enjoy the experiance to make their personal password manager.

| **Feature** | **Action** | **Expected Results** | **Actual Result** |
|-------------|------------|----------------------|-------------------|
| Main screen | Input your name | User is  welcomed and presented with options on how to proceed | Works as expected |

<details><summary>Screenshots</summary>
<img src="docs/testing/user_story_1_1.png">
<img src="docs/testing/user_story_1_2.png">
</details>

9. I want users to easily navigate the site.

| **Feature** | **Action** | **Expected Results** | **Actual Result** |
|-------------|------------|----------------------|-------------------|
| Main screen | Input your name | User is presented with options on how to proceed | Works as expected |
| Login Function screen | Input login | User is asked to input their user name and password | Works as expected |
| Login Function screen | Input username & password | User is given 5 options to choose from along with information on what should be done first | Works as expected |

<details><summary>Screenshots</summary>
<img src="docs/testing/user_story_1_1.png">
<img src="docs/testing/user_story_1_2.png">
<img src="docs/testing/user_story_1_3.png">
<img src="docs/testing/user_story_1_4.png">
</details>

10. I want users to be able to use the functions with out an issue.

| **Feature** | **Action** | **Expected Results** | **Actual Result** |
|-------------|------------|----------------------|-------------------|
| Main screen | Input your name | User is presented with options on how to proceed | Works as expected |
| Login Function screen | Input login | User is asked to input their user name and password | Works as expected |
| Login Function screen | Input username & password | User is given 5 options to choose from along with information on what should be done first | Works as expected |
| Login Function screen | Input option 2 | User is presented with the stored passwords | Works as expected |
| Adding a website screen | Input a website already stored | Notice the website is already stored and a sugestion to avoid this error | Works as expected |

<details><summary>Screenshots</summary>
<img src="docs/testing/user_story_1_1.png">
<img src="docs/testing/user_story_1_2.png">
<img src="docs/testing/user_story_1_3.png">
<img src="docs/testing/user_story_1_4.png">
<img src="docs/testing/user_story_10_1.png">
</details>

11. I want users to know if there was an issue and how to resolve it.

| **Feature** | **Action** | **Expected Results** | **Actual Result** |
|-------------|------------|----------------------|-------------------|
| Main screen | Input your name | User is presented with options on how to proceed | Works as expected |
| Login Function screen | Input login | User is asked to input their user name and password | Works as expected |
| Login Function screen | Input username & password | User is given 5 options to choose from along with information on what should be done first | Works as expected |
| Login Function screen | Input option 2 | User is presented with the stored passwords | Works as expected |
| Adding a website screen | Input a website already stored | Notice the website is already stored and a sugestion to avoid this error | Works as expected |

<details><summary>Screenshots</summary>
<img src="docs/testing/user_story_1_1.png">
<img src="docs/testing/user_story_1_2.png">
<img src="docs/testing/user_story_1_3.png">
<img src="docs/testing/user_story_1_4.png">
<img src="docs/testing/user_story_10_1.png">
</details>

[Back to Table Of Contents](#table-of-contents)

### Unit Testing

#### Password validator

* These unit tests were writen using the unittest library.
* They are to check if a password is long enough and if the password is valid.

##### Valid password

* This unit test was writed to check if the code below is working correctly and checking if they are valid.
* A valid password must be 8+ characters and have at least 1 of each of the following:
    * Uppercase,
    * Lowercase,
    * Digit,
    * Special character "@$_".
* The unit test inputs in 6 different tests and they app passed.

<details><summary>Screenshots</summary>
<img src="docs/testing/test_valid_password_code.png">
<img src="docs/testing/test_valid_password_result.png">
</details>


##### Password length

* This unit test was writed to check if the code below is working correctly and checking the length is valid.
* The valid length password is 8 characters or more.
* The unit test inputs in 4 different tests and they passed. 

<details><summary>Screenshots</summary>
<img src="docs/testing/test_password_length_code.png">
<img src="docs/testing/test_password_length_result.png">
</details>

## Bugs

### Fixed Bugs
* When edinting the master password if you intered the user name instead of the name it would print the new password in the incorrect cell.
    * FIX: Change the function to focus on the one cell as this cell will not change.
* When locating the specific row and column for edit password the function would break if the coordinates where past row 9.
    * FIX: An if else statement was added so the formula changes once the cell is past row 9.
* When adding websites you could add the same one a few times but then to change the password it would change the first one it found.
    * FIX: A function was created to search for that website before adding a new one to the spread sheet. If there was one in the sheet already it would give a prompt to change the name so it is different to what is currently stored.
* When trying to edit a password that is not in the google sheet it would say dose not exsist but also triger the password updated print.
    * FIX: Moved the "password updated" from the main function to the edit password function.

## Deployment

### Deploying to Heroku
* Go to the heroku.com site.
    <details><summary>Screenshots</summary>
    <img src="docs/deployment/heroku_1.png">
* Click the signup button in the top right.
    <details><summary>Screenshots</summary>
    <img src="docs/deployment/heroku_2.png">
* Create an account on heroku.com,
    <details><summary>Screenshots</summary>
    <img src="docs/deployment/heroku_3.png">
* Confirm your account in the email heroku sent to your inbox,
    <details><summary>Screenshots</summary>
    <img src="docs/deployment/heroku_4.png">
* Create a password,
    <details><summary>Screenshots</summary>
    <img src="docs/deployment/heroku_5.png">
* Click and proceed,
    <details><summary>Screenshots</summary>
    <img src="docs/deployment/heroku_6.png">
* Accept the terms of service,
    <details><summary>Screenshots</summary>
    <img src="docs/deployment/heroku_7.png">
* Create a new app, create a name for your app "ci_pp3_ppm" and choose your region,
    <details><summary>Screenshots</summary>
    <img src="docs/deployment/heroku_8.png">
* Go to the settings section,
    <details><summary>Screenshots</summary>
    <img src="docs/deployment/heroku_9.png">
* Click Reveal Config Vars,
    <details><summary>Screenshots</summary>
    <img src="docs/deployment/heroku_10.png">
* Input your .json file. name in the 'Key' field, copy the .json file and paste it in 'Value' field. Also add a key 'PORT' and value '8000'.
    <details><summary>Screenshots</summary>
    <img src="docs/deployment/heroku_11.png">
* In the build packs section click add buildpack. For this project, I added 2 buildpacks 'Python' and 'node.js'. Make sure the Python build pack is above the Nodejs buildpack.
    <details><summary>Screenshots</summary>
    <img src="docs/deployment/heroku_12.png">
* Go to "Deploy" in "Deployment method" select "GitHub",
    <details><summary>Screenshots</summary>
    <img src="docs/deployment/heroku_13.png">
* Click 'Search' (Enter in your projects name that you have in your github repositry)and then 'Connect'. This project is connected to Chrisfaherty/CI_PP3_PPM.
    <details><summary>Screenshots</summary>
    <img src="docs/deployment/heroku_14.png">
* Choose the branch you want to buid your app from "main" .
* If prefered, click on "Enable Automatic Deploys", which keeps the app up to date when you push to git hub. Automatic deployments is turned on for this project.
    <details><summary>Screenshots</summary>
    <img src="docs/deployment/heroku_15.png">
* If the project doesn't deploy after selecting automatic deploy . In the Manual deploy section click Deploy Branch to deploy your code, this is what I had to do.
    <details><summary>Screenshots</summary>
    <img src="docs/deployment/heroku_16.png">
* Once the code is deployed it will show a button that you can click to view the deployed site. Then the project has sucessfully been deployed.

### Forking the GitHub Repository
* Go to the GitHub repository,
* In the top right hand corner you can click on the fork button,
* This will fork the repositry.

## Credits
* The Code Institute Love running project for the guidance with connecting the terminal to a googal sheet through gspread.
* [Tech with Tim](https://www.youtube.com/watch?v=DLn3jOsNRVE) For the inspiration to create a password manager.
* [Tech with Tim](https://www.youtube.com/watch?v=u51Zjlnui4Y) For the guidance on how to use colorama.
* [Geeks for geeks](geeksforgeeks.org) For the guidance on validating & checking that a strong password is created.
* [Otu Michael](https://dev.to/otumianempire/custom-password-validation-in-python-unit-test-the-function-for-password-validation-4l7b) For the guidance with unit testing the password validator.

## Acknowledgements
I would like to take the opertunity to thank:
* My Mentor Mo Shami for the great feedback productive meetings and guiding me to finishing this project.
* I would also like to thank the Code institute team for all the support and material to assist with this project.
* The code institute Tutors for being available when ever guidance was required.

[Back to Table Of Contents](#table-of-contents)