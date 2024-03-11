
"""Tests for User class"""

import unittest
from models.user import User

usr = User()


class TestUser(unittest.TestCase):
    """Tests for user.py"""

    def test_email(self):
        """email test"""
        self.assertTrue(type(usr.email) == str)

    def test_password(self):
        """password test"""
        self.assertTrue(type(usr.password) == str)

    def test_first_name(self):
        """first_name test"""
        self.assertTrue(type(usr.first_name) == str)

    def test_last_name(self):
        """last_name test"""
        self.assertTrue(type(usr.last_name) == str)

if __name__ == '__main__':
    unittest.main()
