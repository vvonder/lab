#-*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from bottle.ext.sqlalchemy import SQLAlchemyPlugin

import settings

engine = create_engine(settings.DB_URL, echo=settings.DEBUG)
DBSession = sessionmaker(bind=engine)
Base = declarative_base(bind=engine)


def create_sqla_plugin():
    return SQLAlchemyPlugin(engine, Base.metadata, create=True, create_session=DBSession)


def create_tables():
    return Base.metadata.create_all()


def drop_tables():
    return Base.metadata.drop_all()
