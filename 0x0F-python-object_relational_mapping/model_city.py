#!/usr/bin/python3

"""
contains the class definition of a City.
"""
from sqlalchemy import Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base



class City(Base):
    """State class inheriting from Base"""
    __tablename__ = "cities"
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
