# coding: utf-8

import markdown
from tornado.web import HTTPError
from tornado.web import authenticated

import model
from .base import BaseHandler
from utils.session import DBSession
from utils.identity import admin_required


class Topic(BaseHandler):
    def get(self, topic_id):
        pass

    @admin_required
    def post(self):
        pass

    @admin_required
    def put(self, topic_id):
        pass

    @admin_required
    def delete(self,topic_id):
        pass



urls = [
        (r'/topics', Topic),
]

