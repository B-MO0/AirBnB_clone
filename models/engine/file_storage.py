import json
from models.base_model import BaseModel


class FileStorage:

    __file_path = "file.json"
    __objects = dict()

    def all(self):
        return self.__objects

    def new(self, obj):
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        with open(self.__file_path, "w") as f:
            dtosave = {}
            for key in FileStorage.__objects.keys():
                dtosave[key] = FileStorage.__objects[key].__str__()
            json.dump(dtosave, f, indent=2)

    def reload(self):
        try:
            with open(self.__file_path, "r") as f:
                FileStorage.__objects = json.load(f)
        except FileNotFoundError:
            pass
