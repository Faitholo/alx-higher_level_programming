#!/usr/bin/python3
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    connection = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    search = sys.argv[4]
    eng = create_engine(connection.format(user_name, password, db_name),
                        pool_pre_ping=True)
    Session = sessionmaker(bind=eng)
    session = Session()
    query = (session.query(State).
             filter_by(name=search).order_by(State.id).all())
    if len(query) == 0:
        print("Not found")
    for item in query:
        print("{}".format(item.id))
