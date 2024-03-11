"""Module for User CLS  """

from models.base_model import BaseModel


class User(BaseModel):
    """User subclass of Basemodel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
