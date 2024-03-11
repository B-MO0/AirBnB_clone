"""Module for  Place CLS"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Place subclass of BaseModel"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = float(0.0)
    longitutude = float(0.0)
    amenity_ids = []
