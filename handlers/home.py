# coding: utf-8

import markdown
from tornado.web import HTTPError
from tornado.web import authenticate

import model
from .base import BaseHandler
from utils.session import DBSession


class Home(BaseHandler):
    def get(self):
        return self.render('home.html')
