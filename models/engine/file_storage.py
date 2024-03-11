#!/usr/bin/python3
"""Module for filestorage CLS"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {'BaseModel': BaseModel, 'User': User, 'State': State, 'City': City,
           'Amenity': Amenity, 'Place': Place, 'Review': Review}


class FileStorage:
    """File storage Class"""
    __file_path = "file.json"
    __objects = dict()
    classes = {'BaseModel': BaseModel,
               'User': User,
               'State': State,
               'City': City,
               'Amenity': Amenity,
               'Place': Place,
               'Review': Review}

    def all(self):
        """Returns Dictionary of objects"""
        return self.__objects

    def new(self, obj):
        """Gives obj to class name plus id"""
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """Serialization of json file"""
        with open(self.__file_path, "w") as f:
            dtosave = {}
            for key in FileStorage.__objects.keys():
                dtosave[key] = FileStorage.__objects[key].to_dict()
            json.dump(dtosave, f, indent=2)

    def reload(self):
        """Deserialisation of json file"""
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = key.split('.')[0]
                    if class_name not in self.classes:
                        self.classes[class_name] = eval(class_name)
                    self.__objects[key] = self.classes[class_name](**value)
        except FileNotFoundError:
            pass
