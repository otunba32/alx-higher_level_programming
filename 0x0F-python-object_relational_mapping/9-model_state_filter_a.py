#!/usr/bin/python3
"""Script that lists all State objects that contains
letter a from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    eng = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True
            )
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    row = session.query(State).filter(State.name.like('%a%')) \
        .order_by(State.id)
    for ol in row:
        print(f"{ol.id}: {ol.name}")
    session.close()
