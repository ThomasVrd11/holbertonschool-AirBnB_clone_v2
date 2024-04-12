#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os

storage_type = os.getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if storage_type == 'db':
        cities = relationship("City", back_populates="state", cascade="all",
                              passive_deletes=True)
    else:
        @property
        def cities(self):
            """Return the list of City instances with state.id equal to
            current State.id for filestorage
            """
            from models import storage
            from models.city import City

            state_cities_list = []
            all_cities = storage.all(City)

            for city in all_cities.values():
                if city.state_id == self.id:
                    state_cities_list.append(city)
            return state_cities_list
