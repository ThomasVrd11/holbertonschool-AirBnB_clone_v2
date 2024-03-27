#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import os 
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base

htypes = os.getenv('HBNB_TYPE_STORAGE')


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if htypes == 'db':
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            """getter attribute cities that returns the list of City instances with state_id"""
            from models import storage
            from models.city import City
            cities_list = []
            for city in storage.all(City).values():
                """ if the city.state_id is equal to the current State.id, append it to the list """
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
