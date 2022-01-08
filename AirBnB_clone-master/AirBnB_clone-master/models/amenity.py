#!/usr/bin/python3
""" Amenity class """

import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity class """
    name = ""
