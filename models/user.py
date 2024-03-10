from models.base_model import BaseModel


class User(BaseModel):
    """User sub class of Basemodel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
