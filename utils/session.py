# coding: utf-8

import contextlib
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from model import Base

import settings


engine = create_engine(settings.MYSQL_CONF)

Session = sessionmaker(engine)

session = Session()


@contextlib.contextmanager
def DBSession():
    yield
    session.close()


