#!/usr/bin/python3
"""Module for  City CLS"""

from models.base_model import BaseModel


class City(BaseModel):
    """City subclass of BaseModel"""
    state_id = ""
    name = ""
