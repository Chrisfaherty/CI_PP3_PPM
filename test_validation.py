"""
This function is to test the validate_password function.
"""
import unittest
from validate_password import validate_password


class TestValidPassword(unittest.TestCase):
    """
    Testing if the passwords are valid and include the required characters.
    At least 1 uppercase, lowercase, digit and @$_ is required.
    The password also has to be 8 characters or longer.
    """

    def test_password_3(self):
        self.assertFalse(validate_password("userpass"))

    def test_password_4(self):
        self.assertFalse(validate_password("userpass1"))

    def test_password_5(self):
        self.assertFalse(validate_password("userpass_1"))

    def test_password_6(self):
        self.assertTrue(validate_password("User_pass1"))

    def test_password_7(self):
        self.assertTrue(validate_password("User_pass2022"))

    def test_password_8(self):
        self.assertTrue(validate_password("User_pass@2022"))


class TestPasswordLength(unittest.TestCase):
    """
    Testing if the passwords are long enough.
    The password has to be 8 characters or longer.
    """

    def test_password_length_1(self):
        self.assertFalse(validate_password(""))

    def test_password_length_2(self):
        self.assertFalse(validate_password("user"))

    def test_password_length_3(self):
        self.assertFalse(validate_password("userpa"))

    def test_password_length_4(self):
        self.assertTrue(validate_password("Userpass_1"))


if __name__ == '__main__':

    unittest.main()
