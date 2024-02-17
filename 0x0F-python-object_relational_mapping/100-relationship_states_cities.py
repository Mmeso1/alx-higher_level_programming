#!/usr/bin/python3
""" creates the State “California” with the City
“San Francisco” from the database
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    db = sessionmaker(bind=engine)()

    cal_state = State(name="Carlifornia")
    san_city = City(name="San Francisco", state=cal_state)

    db.add(san_city)
    db.commit()
    db.close()
