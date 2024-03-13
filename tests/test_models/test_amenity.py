#!/usr/bin/python3
"""Tests for Amenity"""

import unittest
from models.amenity import Amenity

amenity = Amenity()


class TestAmenity(unittest.TestCase):
    """Tests for amenity.py"""

    def test_name(self):
        """Checks name"""
        self.assertTrue(type(amenity.name) is str)


if __name__ == '__main__':

    unittest.main()
