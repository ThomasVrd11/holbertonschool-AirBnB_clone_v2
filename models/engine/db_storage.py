#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import create_engine
import os
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage():
    """dbstorage class engine"""
    __engine = None
    __session = None

    def __init__(self):
        """initialise the dbstorage"""
        hbnb_usr = os.getenv("HBNB_MYSQL_USER")
        hbnb_pwd = os.getenv("HBNB_MYSQL_PWD")
        hbnb_host = os.getenv("HBNB_MYSQL_HOST", "localhost")
        hbnb_db = os.getenv("HBNB_MYSQL_DB")
        hbnb_env = os.getenv("HBNB_ENV")

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(hbnb_usr, hbnb_pwd,
                                              hbnb_host, hbnb_db,
                                              pool_pre_ping=True))

        if hbnb_env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query all objects by class name,or all if cls=None"""
        class_map = {
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }

        list_objects = {}
        if cls:
            if isinstance(cls, str):
                cls = class_map.get(cls, None)
                if cls is None:
                    print("** class doesn't exist **")
                    return list_objects
            self.query_session(cls, list_objects)
        else:
            for cls_obj in class_map.values():
                self.query_session(cls_obj, list_objects)
        return list_objects

    def query_session(self, cls, list_objects):
        """handle the query and populate the dictionary,called by all"""
        query_result = self.__session.query(cls).all()
        for obj in query_result:
            key = "{}.{}".format(cls.__name__, obj.id)
            list_objects[key] = obj

    def new(self, obj):
        """Add the object to currend database session"""
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current db session obj if not none"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Reload all tables from the db and recreate the session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
        