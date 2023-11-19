#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    if storage_type == "db":
        name = Column(string(128), nullable=False)
        state_id = Column(string(60), nullable=False, ForeignKey("states.id"))
        places = relationship("Place", cascade="all,delete", backref="cities")
    else:
    state_id = ""
    name ="" 
