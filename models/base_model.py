#!/usr/bin/python3
"""BaseModel class"""

from uuid import uuid4
from datetime import datetime

class BaseModel:
    
    def __init__(self, *args, **kwargs):    
        
        tf = "%Y-%m-%dT%H:%M:%S.%f" 
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict