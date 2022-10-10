def validate_password(password_to_validate):
    """
    Inside the try, checks to make sure the password
    contains a capital letter,
    lowercase letter & a special character.
    Raises ValueError if the password does not contain 
    a lowercase & uppercase,
    or if there aren't more than 6 values. 
    credits geeksforgeeks.org
    """
    lower, upper, special, digit = 0, 0, 0, 0
    s = password_to_validate
    capitalalphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    smallalphabets = "abcdefghijklmnopqrstuvwxyz"
    specialchar = "$@_"
    digits = "0123456789"
    if len(s) >= 8:
        for i in s:
            # counting lowercase alphabets
            if i in smallalphabets:
                lower += 1           
            # counting uppercase alphabets
            if i in capitalalphabets:
                upper += 1           
            # counting digits
            if i in digits:
                digit += 1           
            # counting the mentioned special characters
            if i in specialchar:
                special += 1       
            if lower >= 1 and upper >= 1 and special >= 1 and \
                    digit >= 1 and lower + special + upper + digit == len(s):
                print("Valid Password")
            else:
                print("Invalid Password")
                print("Must be 8 + char, lower, upper & special char @$_")
                return False
            
            return True