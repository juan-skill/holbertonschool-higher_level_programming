#!/usr/bin/python3
""" Define State class """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """ This is the State class """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement="auto", unique=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return "<State(id='%s', name='%s')>" % (self.id, self.name)
