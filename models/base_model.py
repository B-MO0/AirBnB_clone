""" Module for the BaseModel CLS """

import uuid
from datetime import datetime
import models


class BaseModel:

    def __init__(self, *args, **kwargs):

        if kwargs and len(kwargs):
            for key in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or "updated_at":
                        setattr(self, key, datetime.
                                strptime(kwargs, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return f"[ {self.__class__.__name__} ] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        data = {}
        for key in self.__dict__:
            if key in ("created_at", "updated_at"):
                value = self.__dict__[key].isoformat()
            else:
                value = self.__dict__[key]
            data[key] = value
        data["__class__"] = self.__class__.__name__
        return data
