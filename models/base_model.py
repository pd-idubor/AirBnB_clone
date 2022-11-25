#!/usr/bin/python3
"""
    Defines BaseModel class.
"""
import models
from datetime import datetime
import uuid


class BaseModel:
    """
        Represents the BaseModel class
    """
    def __init__(self, *args, **kwargs):
        """
            Initialization
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        if (len(kwargs) != 0):
            for k, v in kwargs.items():
                if (k == 'created_at' or k == 'updated_at'):
                    self.__dict__[k] = datetime.strptime(v, t_format)
                else:
                    if (k != '__class__'):
                        self.__dict__[k] = v
        else:
            models.storage.new(self)

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
        models.storage.save()

    def to_dict(self):
        """
            Returns a dictionary
            containing all keys/values of the instance
        """
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        in_dct = dict(self.__dict__)
        in_dct['__class__'] = self.__class__.__name__
        in_dct['created_at'] = self.created_at.strftime(t_format)
        in_dct['updated_at'] = self.updated_at.strftime(t_format)

        return (in_dct)
