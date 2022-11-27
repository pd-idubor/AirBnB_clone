#!/usr/bin/python3

"""
    Describes the class storage class
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review


class FileStorage:
    """
        Serializes instances to a JSON file and
        deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            Returns the _object dictionary
        """
        return (FileStorage.__objects)

    def new(self, obj):
        """
            Adds obj to _object dictionary
        """
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
            Serializes __objects to the JSON file
        """
        obj_dict = {}
        for key, val in FileStorage.__objects.items():
            obj_dict[key] = val.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='UTF-8') as n_file:
            json.dump(obj_dict, n_file)

    def reload(self):
        """
            Deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path) as op:
                FileStorage.__objects = json.load(op)

            for val in FileStorage.__objects.values():
                cls = val["__class__"]
                del val["__class__"]
                self.new(eval(cls)(**val))

        except FileNotFoundError:
            pass
