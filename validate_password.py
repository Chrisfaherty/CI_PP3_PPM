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
            l, u, p, d = 0, 0, 0, 0
            s = password_to_validate
            capitalalphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            smallalphabets = "abcdefghijklmnopqrstuvwxyz"
            specialchar = "$@_"
            digits = "0123456789"
            if (len(s) >= 8):
                for i in s:
            
                    # counting lowercase alphabets
                    if (i in smallalphabets):
                        l += 1           
            
                    # counting uppercase alphabets
                    if (i in capitalalphabets):
                        u += 1           
            
                    # counting digits
                    if (i in digits):
                        d += 1           
            
                    # counting the mentioned special characters
                    if(i in specialchar):
                        p += 1       
            if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(s)):
                print("Valid Password")
            else:
                print("Invalid Password")
                print("Must be 8 + char, lower, upper & special char @$_")
                return False
            
            return True