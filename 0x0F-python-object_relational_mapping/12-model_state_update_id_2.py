#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
            .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session() = sessionmaker(bind=engine)()
    session = Session()

    state = db.query(State).filter_by\
            (State.id=2).first()
    db.add(state.name="New Mexico")
    session.commit()
    session.close()
