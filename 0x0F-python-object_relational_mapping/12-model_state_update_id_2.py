#!/usr/bin/python3
""" changes the name of a State object from the database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()

    state = session.query(State)\
        .filter_by(id=2) .first()
    session.add(State(name="New Mexico"))
    session.commit()
    session.close()
