#-*- coding:utf-8 -*-

from sqlalchemy import Column, Integer, String
from utils.datastore import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), unique=True)
    description = Column(String(128))
    type = Column(Integer, default=1)

    def __repr__(self):
        return "<User('%s','%s','%s')>" % (self.name, self.description, self.type)
