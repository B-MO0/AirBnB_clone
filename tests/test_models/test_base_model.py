""" unittests for base_models.py """

import unittest
from models.base_model import BaseModel
from datetime import datetime
import os


MyModel = BaseModel()


class TestBase(unittest.TestCase):
    """ Tests for base_model.py """
    def test_save(self):
        """ Tests for save """
        orig = MyModel.updated_at
        MyModel.save()
        self.assertFalse(MyModel.updated_at == orig)
        os.remove("file.json")
        MyModel.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_to_dict(self):
        """ Test for to_dict """
        dict_result = MyModel.to_dict()
        self.assertTrue(type(dict_result) is dict)
        self.assertEqual(dict_result["__class__"], "BaseModel")
        self.assertTrue(type(dict_result["created_at"]) is str)

    def test_id(self):
        """ Test id is correct """
        self.assertTrue(type(MyModel.id) is str)

    def test_created_at(self):
        """ Test for created_at """
        self.assertTrue(type(MyModel.created_at) is datetime)

    def test_str(self):
        """ Test for __str__ """
        self.assertEqual(str(MyModel), "[{}] ({}) {}".format(
            MyModel.__class__.__name__, MyModel.id, MyModel.__dict__))


if __name__ == '__main__':

    unittest.main()
