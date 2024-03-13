#!/usr/bin/python3
""" Module for the BaseModel CLS """

import uuid
from datetime import datetime
import models


class BaseModel:
    """ BaseModel Class """
    def __init__(self, *args, **kwargs):
        """atributes instantiation"""
        obform = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs and len(kwargs):
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        setattr(self, key, datetime.
                                strptime(value, obform))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """string representation of instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ updates when saved """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """creates a dictionary"""
        data = {}
        for key in self.__dict__:
            if key == "created_at" or key == "updated_at":
                value = self.__dict__[key].isoformat()
            else:
                value = self.__dict__[key]
            data[key] = value
        data["__class__"] = self.__class__.__name__
        return data
