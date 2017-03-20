# coding: utf-8

import markdown
from tornado.web import HTTPError
from tornado.web import authenticated

import model
from .base import BaseHandler
from utils.session import DBSession


class Signup(BaseHandler):
    def get(self):
        pass

    def post(self):
        pass


class Signin(BaseHandler):
    def get(self):
        pass

    def post(self):
        pass


class Signout(BaseHandler):
    def get(self):
        # todo: delete session and cookie
        pass


urls = [
        (r'/signup', Signup),
        (r'/signin', Signin),
        (r'/signout', Signout),
]
