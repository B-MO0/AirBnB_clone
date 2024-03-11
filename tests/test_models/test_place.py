"""Test for Place class"""

import unittest
from models.place import Place

place = Place()


class TestPlace(unittest.TestCase):
    """Tests for place.py"""

    def test_city_id(self):
        """Checks that city_id is working"""
        self.assertTrue(type(place.city_id) is str)

    def test_user_id(self):
        """Checks that user_id is working"""
        self.assertTrue(type(place.user_id) is str)

    def test_name(self):
        """Checks that name is working"""
        self.assertTrue(type(place.name) is str)

    def test_description(self):
        """Checks that description is working"""
        self.assertTrue(type(place.description) is str)

    def test_number_rooms(self):
        """number_rooms is an int"""
        self.assertTrue(type(place.number_rooms) is int)

    def test_number_bathrooms(self):
        """number_bathrooms is an int"""
        self.assertTrue(type(place.number_bathrooms) is int)

    def test_max_guest(self):
        """Checks that max_guest is an int"""
        self.assertTrue(type(place.max_guest) is int)

    def test_price_by_night(self):
        """Checks that price_by_night is an int"""
        self.assertTrue(type(place.price_by_night) is int)

    def test_latitude(self):
        """Checks that latitude is a float"""
        self.assertTrue(type(place.latitude) is float)

    def test_longitude(self):
        """Checks that longitude is a float"""
        self.assertTrue(type(place.longitude) is float)

    def test_amenity_ids(self):
        """Checks that amenity_ids is a list"""
        self.assertTrue(type(place.amenity_ids) is list)


if __name__ == '__main__':

    unittest.main()
