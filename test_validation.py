"""
This function is to test the main inputs run.py recieves from the user.
"""

import unittest
import run


class TestRun(unittest.TestCase):
    """
    Verification of master username and password
    """
    def test_username(self):
        """
        Test the username input
        """
        self.assertTrue(run.setup('create account'), True)


if __name__ == '__main__':
    unittest.main()
