#!/usr/bin/python3

"""
    Describes the class storage class
"""
import json


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
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """
            Serializes __objects to the JSON file
        """
        obj_dict = FileStorage.__objects

        with open(FileStorage.__file_path, 'w', encoding='UTF-8') as n_file:
            json.dump(obj_dict, n_file)

    def reload(self):
        """
            Deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path) as op:
                FileStorage.__objects = json.load(op)

        except FileNotFoundError:
            pass
