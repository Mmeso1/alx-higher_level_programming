#!/usr/bin/python3
"""
This module runs a script to list all State object
from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)()
    session = Session()

    for state in db.query(State).order_by(State.id):
        print("{:d}: {:s}".format(state.id, state.name))
