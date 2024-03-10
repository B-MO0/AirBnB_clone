import json


class File_storage:

    __file_path = "file.json"
    __objects = dict()

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = str(obj.__dict__)

    def save(self):
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f, indent=2)

    def reload(self):
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass
