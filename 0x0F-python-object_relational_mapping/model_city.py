#!/usr/bin/python3


from sqlalchemy import Column, Integer, String, ForeingnKey
from model_state import Base, State


class City(Base):
    '''
    class city
    '''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
