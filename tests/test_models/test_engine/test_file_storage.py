#!/usr/bin/python3

""" unitest for file_storage.py """

import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from os import path, remove

flst = FileStorage()


class TestFileStorage(unittest.TestCase):
    """ Tests for file_storage.py """

    def test_filepath(self):
        """ Tests for __file_path """
        self.assertTrue(type(flst._FileStorage__file_path) is str)
        tmp = FileStorage()
        try:
            remove("file.json")
        except FileNotFoundError:
            pass
        tmp.save()
        self.assertTrue(path.exists("file.json"))

    def test_object(self):
        """ Tests for __objects """
        tmp = FileStorage()
        self.assertTrue(type(tmp._FileStorage__objects) is dict)
        self.assertTrue(type(tmp.all()) is dict)

    def test_new(self):
        """ Tests for new """
        tmp = flst.all().copy()
        BaseModel()
        self.assertFalse(tmp == flst.all())

    def test_save(self):
        """ Tests for save """
        try:
            remove("file.json")
        except FileNotFoundError:
            pass
        base = BaseModel()
        base.save()
        with open("file.json") as f:
            tmp = json.load(f)
        self.assertTrue(type(tmp) is dict)

    def test_reload(self):
        """ Tests for reload """
        flst1 = FileStorage()
        flst1.save()
        flst1.reload()
        tmp = flst1.all()
        BaseModel()
        flst1.save()
        flst1.reload()
        self.assertNotEqual(tmp, flst1.all())


if __name__ == '__main__':

    unittest.main()
