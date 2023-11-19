#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from models.review import Review
from os import getenv


storage_type = getenv("HBNB_TYPE_STORAGE")

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    if storage_type == 'db':
        city_id = column(string(60), nullable=False, ForeignKey("cities.id"))
        user_id = column(string(60), nullable=False, ForeignKey('users.id'))
        name = column(string(128), nullable=False)
        description = column(string(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', cascade="all,delete", backref="place")

    else:

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def reviews(self):
        """getter document"""
        for models import storage
        reviewsList = []
        reviewsALL = storage.all(Review)
        for review in reviewsALL.values():
            if reviews.place_id == self.id:
                reviewsList.append(review)
        return reviewsList
