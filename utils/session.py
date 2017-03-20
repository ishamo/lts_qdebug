# coding: utf-8

import contextlib
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from model import Base

import settings


engine = create_engine("mysql://%s:%s@localhost:3306/%s" % 
        (settings.MYSQL_USER, settings.MYSQL_PASSWORD, settings.MYSQL_DBNAME))

Session = sessionmaker(engine)


@contextlib.contextmanager
def DBSession():
    yield
    session.remove()


