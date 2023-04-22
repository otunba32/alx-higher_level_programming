#!/usr/bin/python3
"""a file that contains the class definition of a State and an instance Base"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):

    """State class that inherits from Base declarative"""

    __tablename__ = 'states'
    id = Column(
            Integer,
            autoincrement=True,
            unique=True,
            nullable=False,
            primary_key=True
            )

    name = Column(String(128), nullable=False)
