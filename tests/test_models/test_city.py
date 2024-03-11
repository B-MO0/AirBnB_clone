"""Test for City class"""

import unittest
from models.city import City

city = City()


class TestCity(unittest.TestCase):
    """Tests for city.py"""

    def test_state_id(self):
        """Checks that state_id is working"""
        self.assertTrue(type(city.state_id) is str)

    def test_name(self):
        """Checks that name is working"""
        self.assertTrue(type(city.name) is str)


if __name__ == '__main__':

    unittest.main()
