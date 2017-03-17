# coding: utf-8

import contextlib
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from model import Base


engine = create_engine("msyql://%s:%s@localhost:3306/%s" % (settings['user'], settings['password'], settings['dbname']))

Session = sessionmaker(engine)


@contextlib.contextmanager
def DBSession():
    yield
    session.remove()


