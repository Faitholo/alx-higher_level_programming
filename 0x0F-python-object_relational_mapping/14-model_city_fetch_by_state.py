#!/usr/bin/python3
'''
a script that lists all State objects
'''


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                        argv[2],
                                                        argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    c = session.query(City, State).filter(City.state_id == State.id)\
        .order_by(City.id).all()
    for cty, st in c:
        print("{}: ({}) {}".format(st.name, cty.id, cty.name))
    session.close()
