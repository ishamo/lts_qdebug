# coding: utf-8

import markdown
from tornado.web import HTTPError
from tornado.web import authenticate

import model
from .base import BaseHandler
from utils.session import DBSession


class Node(BaseHandler):
    def get(self, node_id):
        pass

    @authenticate
    def post(self):
        pass
