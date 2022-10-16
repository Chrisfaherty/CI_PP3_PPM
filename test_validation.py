"""
This function is to test the main inputs run.py recieves from the user.
"""
import unittest
from validate_password import validate_password


class TestValidPassword(unittest.TestCase):
    """
    This function is to test the main inputs run.py recieves from the user.
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

