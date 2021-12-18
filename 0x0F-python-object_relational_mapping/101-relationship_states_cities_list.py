#!/usr/bin/python3
import sys
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    connection = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine(connection.format(user_name, password, db_name))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).order_by(State.id).all()
    for row in query:
        print("{}: {}".format(row.id, row.name))
        for related_row in row.cities:
            print("\t{}: {}".format(related_row.id, related_row.name))
