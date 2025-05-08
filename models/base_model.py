#!/usr/bin/python3
"""BaseModel that defines all common attribute/methods."""
import uuid
from datetime import datetime

class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self):
        """Initializes new instances of BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return string: [<class name>] (<id>) <__dict__>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update updated_at to the current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary of the instances in ISO format."""
        final = self.__dict__.copy()
        final["__class__"] = self.__class__.__name__
        final["created_at"] = self.created_at.isoformat()
        final["updated_at"] = self.updated_at.isoformat()
        return final
