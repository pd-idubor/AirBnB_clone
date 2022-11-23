#!/usr/bin/python3
"""
    Defines BaseModel class.
"""
from datetime import datetime
import uuid


class BaseModel:
    """
        Represents the BaseModel class
    """
    def __init__(self):
        """
            Initialization
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """
            Printable string representation
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__))

    def save(self):
        """
            Updates the public instance attribute 'updated_at'
        """
        self.updated_at = datetime.today()

    def to_dict(self):
        """
            Returns a dictionary
            containing all keys/values of the instance
        """
        in_dct = dict(self.__dict__)
        in_dct['__class__'] = self.__class__.__name__
        in_dct['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        in_dct['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        return (in_dct)
