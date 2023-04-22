#!/usr/bin/python3
"""Module that contains the class definition of city and instance Base"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class that inherits from Base"""
    __tablename__ = 'cities'
    id = Column(
            Integer,
            autoincrement=True,
            unique=True,
            nullable=False,
            primary_key=True
            )
    name = Column(string(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
