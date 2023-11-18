#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(string(128), nullable=False)
    cities = relationship('city', backref='state' cascade='all, delete')
    name = ""
    def cities(self):
     """
        Getter attribute for retrieving related City instances in FileStorage.

        Returns:
            list: A list of City instances associated with the current State.

        Notes:
            This getter uses the FileStorage to retrieve all City instances and
            filters them to include only those with state_id matching the current
            State's id.
    """
    from model.city import City
    from models import storage
    cities_list = []
    cities_all = storage.all(City)
    for city in cities_all.values():
        if city.state_id == self.id:
            cities_list.append(city)
            return cities_list
