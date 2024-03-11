from models.base_model import BaseModel


class Review(BaseModel):
    """State subclass of BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
