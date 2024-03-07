import uuid
from datetime import datetime
from time import sleep

class BaseModel:

    def __init__(self, *args, **kwargs):

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now().isoformat()
            self.updated_at = datetime.now().isoformat()

    def __str__(self):
        return f"[ {self.__class__.__name__} ] ({self.id}) {self.__dict__}"
    
    def save(self):
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        data = self.__dict__
        data["__class__"] = self.__class__.__name__
        return data

my_model = BaseModel(id='58079290-50e6-41aa-80b3-4d94e7ed5d99', created_at='2025-03-07T01:05:24.178672', updated_at='2025-03-07T01:05:24.178672')
my_model2 = BaseModel()

#TESTING
print(my_model.__dict__)

