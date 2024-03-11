"""Tests for State class"""

import unittest
from models.state import State

state = State()


class TestState(unittest.TestCase):
    """Tests for state.py"""

    def test_name(self):
        """name is working"""
        self.assertTrue(type(state.name) == str)

if __name__ == '__main__':
    unittest.main()
