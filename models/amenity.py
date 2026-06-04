#!/usr/bin/python3
"""This module defines the Amenity class."""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """Represents an Amenity.

    Attributes (DBStorage):
        __tablename__ (str): The MySQL table name.
        name (Column): Amenity name — max 128 chars, required.
        place_amenities: Many-to-Many back-reference from Place via backref.

    Attributes (FileStorage):
        name (str): The amenity name.
    """

    __tablename__ = "amenities"

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
    else:
        name = ""
