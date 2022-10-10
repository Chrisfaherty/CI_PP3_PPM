def validate_password(password_to_validate):
    """
    Inside the try, checks to make sure the password contains a
    capital letter, lowercase letter & a special character.
    Raises ValueError if the password does not contain 
    a lowercase & uppercase,mor if there aren't more than 6 values.
    credits geeksforgeeks.org
    """
    low, upp, spec, dgt = 0, 0, 0, 0
    s = password_to_validate
    capitalalphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    smallalphabets = "abcdefghijklmnopqrstuvwxyz"
    specialchar = "$@_"
    digits = "0123456789"
    if (len(s) >= 8):
        for i in s:
            # counting lowercase alphabets
            if (i in smallalphabets):
                low += 1           
            # counting uppercase alphabets
            if (i in capitalalphabets):
                upp += 1           
            # counting digits
            if (i in digits):
                dgt += 1           
            # counting the mentioned special characters
            if (i in specialchar):
                spec += 1       
        if (low >= 1 and upp >= 1 and spec >= 1 and dgt >= 1 and
                low + spec + upp + dgt == len(s)):
            print("Valid Password")
        else:
            print("Invalid Password")
            print("Must be 8 + characters, lower, upper, number & special @$_")
            return False

        return True

