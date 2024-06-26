#!/usr/bin/python3
"""
lists all Cities objects from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == '__main__':
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]
                ), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(State,
                           City).join(City, State.id == City.state_id).all()

    for city in cities:
        print(
              "{}: ({}) {}".format
              (city.State.name, city.City.id, city.City.name))

    session.close()
