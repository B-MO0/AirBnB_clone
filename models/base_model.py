import uuid
from datetime import datetime
from time import sleep

class BaseModel:

    def __init__(self):
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

my_model = BaseModel()
my_model2 = BaseModel()

#TESTING
print(my_model.__str__())

