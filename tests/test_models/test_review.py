"""Tests for Review class"""

import unittest
from models.review import Review

review = Review()


class TestReview(unittest.TestCase):
    """Tests for review.py"""

    def test_place_id(self):
        """place_id is working"""
        self.assertTrue(type(review.place_id) is str)

    def test_user_id(self):
        """user_id is working"""
        self.assertTrue(type(review.user_id) is str)

    def test_text(self):
        """text is working"""
        self.assertTrue(type(review.text) is str)


if __name__ == '__main__':

    unittest.main()
