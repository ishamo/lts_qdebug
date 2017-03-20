# coding: utf-8

from sqlalchemy import create_engine, Column, text
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base

from pbkdf2 import crypt


Base = declarative_base()


def calc_password_hash(password, salt, algorithm='pbkdf2'):
        return '%s:%s:%s' %(algorithm, salt, crypt(password, salt))


class User(Base):
    __tablename__ = "user"
    id_ = Column(Integer, primary_key=True)
    username = Column(Unicode(8), nullable=False)
    password = Column(Unicode(16), nullable=False)
    email = Column(Unicode(64))
    role = Column(Enum('admin', 'normal'), default='normal')
    bio = Column(Unicode(128))
    created_at = Column(DateTime, server_default=text('NOW()'))
    updated_at = Column(DateTime, server_default=text('NOW()'), onupdate=text('NOW'))

    def check_password(self, password, salt):
        salt = self.password[:8]
        return calc_password_hash(password, salt) == self.password

    def _generate_password(self, password):
        salt = os.urandom(8).uncode('hex')
        return calc_password_hash(password, salt)

    def __init__(self, *args, **kwargs):
        if 'password' in kwargs:
            password = kwargs.pop('password')
            password = self._generate_password(password)
            kwargs['password'] = password

        for k, v in kwargs.items():
            setattr(self, k, v)

        super(User, self).__init__(self, *args, **kwargs)


class Token(Base):
    __tablename__ = 'token'
    id_ = Column(Integer, primary_key=True)
    token_string = Column(Unicode(64))
    user_id = Column(Integer)


class Post_(Base):
    __tablename__ = 'post_'
    id_ = Column(Integer, primary_key=True)
    title = Column(Unicode(32))
    html = Column(UnicodeText)
    markdown = Column(UnicodeText)
    created_at = Column(DateTime, server_default=text('NOW()'))
    updated_at = Column(DateTime, server_default=text('NOW()'), onupdate=text('NOW'))
    user_id = Column(Integer)
    node_id = Column(Integer)


class Post_Topic(Base):
    __tablename__ = 'post_topic'
    id_ = Column(Integer, primary_key=True)
    post_id = Column(Integer)
    topic_id = Column(Integer)

class Topic(Base):
    __tablename__ = 'topic'
    id_ = Column(Integer, primary_key=True)
    slug = Column(Unicode(8), nullable=False)


class Node(Base):
    __tablename__ = 'node'
    id_ = Column(Integer, primary_key=True)
    label = Column(Unicode(8), nullable=False)


class Answer(Base):
    __tablename__ = 'answer'
    id_ = Column(Integer, primary_key=True)
    text = Column(UnicodeText)
    user_id = Column(Integer)
    post_id = Column(Integer)
