#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship(
            "City",
            backref="state",
            cascade="all, delete")
    else:
        @property
        def cities(self):
            """Getter for cities"""
            list_cities = []
            for c in models.storage.all(City).values():
                if c.state_id == self.id:
                    list_cities.append(c)
            return list_cities
