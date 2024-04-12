#!/usr/bin/python3
"""This module defines a class DBStorage"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """Define private class attributes"""
    __engine = None
    __session = None

    def __init__(self):
        """Method to create a new instance of DBStorage"""
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            user, password, host, database), pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Method to query all objects from the current database session"""
        classes = [User, State, City, Amenity, Place, Review]
        if cls:
            objs = self.__session.query(cls).all()
        else:
            objs = []
            for classname in classes:
                objs.extend(self.__session.query(classname).all())
        dict = {f"{obj.__class__.__name__}.{obj.id}": obj for obj in objs}
        return dict

    def new(self, obj):
        """Method to add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Method to commit all changes of the current database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Method to delete the object from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Method to create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Method to close the current session"""
        self.reload()
        self.__session.close()
