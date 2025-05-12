#!/usr/bin/python3

"""
contains the class definition of a State and an instance Base
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base, relationship

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """State class inheriting from Base"""
    __tablename__ = "states"
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state')
