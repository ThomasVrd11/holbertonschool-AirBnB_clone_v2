#!/usr/bin/python3
"""This module defines a class FileStorage"""
import json


class FileStorage:
    """Define private class attributes"""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Method to return the dictionary of objects"""
        if cls:
            cls_objects = {}
            for key, value in FileStorage.__objects.items():
                if cls == value.__class__:
                    cls_objects[key] = value
            return cls_objects
        return FileStorage.__objects

    def new(self, obj):
        """Method to add an object to the storage dictionary"""
        self.all().update({obj.to_dict()["__class__"] + "." + obj.id: obj})

    def save(self):
        """Method to save the storage dictionary to a file"""
        with open(FileStorage.__file_path, "w") as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f, indent=4)

    def reload(self):
        """Method to load the storage dictionary from a file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    "BaseModel": BaseModel, "User": User, "Place": Place,
                    "State": State, "City": City, "Amenity": Amenity,
                    "Review": Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, "r") as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val["__class__"]](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Method to delete an object from the storage dictionary"""
        if not obj:
            return
        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        if obj_key in FileStorage.__objects:
            del FileStorage.__objects[obj_key]

    def close(self):
        """Method to reload the storage dictionary"""
        self.reload()
        