#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from models.review import Review
from os import getenv


storage_type = getenv("HBNB_TYPE_STORAGE")


place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column(
        "place_id",
        String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "amenity_id",
        String(60),
        ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False,
    ),
)



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
        amenities = relationship("Amenity", secondary=place_amenity,
                                viewonly=False,
                                back_populates="place_amenities")


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

    @property
    def amenities(self):
        """Getter docuemnt"""
        from models import storage
        amenitiesList = []
        amenitiesAll = storage.all(Amenity)
        for amenity in amenitiesAll.values():
            if amenity.id in self.amenity_ids:
                amenitiesList.append(amenity)
        return amenitiesList

    
    @property
    def reviews(self):
        """getter document"""
        for models import storage
        reviewsList = []
        reviewsALL = storage.all(Review)
        for review in reviewsALL.values():
            if reviews.place_id == self.id:
                reviewsList.append(review)
        return reviewsList

    @amenities.setter
    def amenities(self, amenity):
        """Setter document"""
        if isinstance(amenity, Amenity):
            self.amenity_ids.append(amenity.id)
