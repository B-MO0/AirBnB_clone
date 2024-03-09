import uuid
from datetime import datetime
from models import storage

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
            storage.new(self)
            

    def __str__(self):
        return f"[ {self.__class__.__name__} ] ({self.id}) {self.__dict__}"
    
    def save(self):
        self.updated_at = datetime.now().isoformat()
        storage.save()
        

    def to_dict(self):
        data = self.__dict__
        data["__class__"] = self.__class__.__name__
        return data



